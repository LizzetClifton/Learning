import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui
import maya.api.OpenMayaRender as omr
import maya.cmds as mc

def maya_useNewAPI():
    pass

class HelloWorldNode(omui.MPxLocatorNode):
    TYPE_NAME = "helloworld" #name of the node
    TYPE_ID = om.MTypeId(0x0007f7f7) #unique id that identifies node
    DRAW_CLASSIFICATION = "drawdb/geometry/helloworld" # draw-specific classification string (VP2.0)
    DRAW_REGISTRANT_ID = "HelloWorldNode" #unique name to identify registration

    def __init__(self):
        super(HelloWorldNode, self).__init__()
    
    #function that returns new instance of class
    @classmethod
    def creator(cls):
        return HelloWorldNode()
    
    #function that will initialize all attributes of node
    @classmethod
    def initialize(cls):
        pass

class HelloWorldDrawOverride(omr.MPxDrawOverride):
    NAME = "HelloWorldDrawOverride"

    def __init__(self, obj):
        super(HelloWorldDrawOverride, self).__init__(obj, None, False)

    def prepareForDraw(self, obj_path, camera_path, frame_context, old_data):
        pass

    def supportedDrawAPIs(self):
        return (omr.MRenderer.kAllDevices)

    def hasUIDrawables(self):
        return True

    def addUIDrawables(self, obj_path, draw_manager, frame_context, data):
        #here, we draw the helloworld text to viewport
        draw_manager.beginDrawable()
        draw_manager.text2d(om.MPoint(100, 100, "Hello World"))
        draw_manager.endDrawable()
    
    @classmethod
    def creator(cls, obj):
        return HelloWorldDrawOverride(obj)

def initializePlugin(plugin):
    vendor = "Lizzet Clifton"
    version = "1.0.0"
    
    plugin_fn = om.MFnPlugin(plugin, vendor, version)

    #registering helloworld node
    try:
        plugin_fn.registerNode(HelloWorldNode.TYPE_NAME, HelloWorldNode.TYPE_ID, HelloWorldNode.creator, HelloWorldNode.initialize, om.MPxNode.kLocatorNode, HelloWorldNode.DRAW_CLASSIFICATION) 
        #om.MPxNode... is the type of node to be registered
    except:
        om.MGlobal.displayError("Failed to register node: {0}".format(HelloWorldNode.TYPE_NAME))
    
    #registering draw override
    try:
        omr.MDrawRegistry.registerDrawOverrideCreator(HelloWorldNode.DRAW_CLASSIFICATION, HelloWorldNode.DRAW_REGISTRANT_ID, HelloWorldDrawOverride.creator)
    except:
        om.MGlobal.displayError("Failed to register draw override: {0}".format(HelloWorldDrawOverride.NAME))

def uninitializePlugin(plugin):
    plugin_fn = om.MFnPlugin(plugin)

    #deregistering draw override
    try:
        omr.MDrawRegistry.deregisterDrawOverrideCreator(HelloWorldNode.DRAW_CLASSIFICATION, HelloWorldNode.DRAW_REGISTRANT_ID)
    except:
        om.MGlobal.displayError("Failed to draw override: {0}".format(HelloWorldDrawOverride.NAME))
    #deregisterind helloworld node
    try:
        plugin_fn.deregisterNode(HelloWorldNode.TYPE_ID)
    except:
        om.MGlobal.displayError("Failed to deregister node: {0}".format(HelloWorldNode.TYPE_NAME))


if __name__ == "__main__":
    #this will create a new scene so that we can unload the plugin
    mc.file(new=True, force=True)

    plugin_name = "helloWorldNode.py"
    mc.evalDeferred('if mc.pluginInfo("{0}", q=True, loaded=True): mc.unloadPlugin("{0}")'.format(plugin_name))
    mc.evalDeferred('if not mc.pluginInfo("{0}", q=True, loaded=True): mc.loadPlugin("{0}")'.format(plugin_name))

    #this will automatically create helloworld node after plugin is reloaded
    mc.evalDeferred('mc.createNode("helloworld")')