import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui
import maya.cmds as mc

def maya_useNewAPI():
    pass

class HelloWorldNode(omui.MPxLocatorNode):
    TYPE_NAME = "helloworld"
    TYPE_ID = om.MTypeId(0x0007f7f7)

    def __init__(self):
        super(HelloWorldNode, self).__init__()
    
    @classmethod
    def creator(cls):
        return HelloWorldNode()
    
    @classmethod
    def initialize(cls):
        pass

def initializePlugin(plugin):
    vendor = "Lizzet Clifton"
    version = "1.0.0"
    
    plugin_fn = om.MFnPlugin(plugin, vendor, version)

    try:
        plugin_fn.registerNode(HelloWorldNode.TYPE_NAME, HelloWorldNode.TYPE_ID, HelloWorldNode.creator, HelloWorldNode.initialize, om.MPxNode.kLocatorNode)
    except:
        om.MGlobal.displayError("Failed to register node: {0}".format(HelloWorldNode.TYPE_NAME))

def uninitializePlugin(plugin):
    plugin_fn = om.MFnPlugin(plugin)

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