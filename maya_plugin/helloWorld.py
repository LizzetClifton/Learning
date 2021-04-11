#creating and registering a new command
import maya.api.OpenMaya as om
import maya.cmds as mc

def maya_useNewAPI():
    pass

#this extends the maya api mpx class found in the open maya package
class HelloWorldCmd(om.MPxCommand):
    #adding a class variable to store command's name
    #this is what you would call in a script to execute the command
    COMMAND_NAME = "HelloWorld"

    #adding a call to super for the init method
    def __init__(self):
        super(HelloWorldCmd, self).__init__()

    #this do it method is required for all commands
    def doIt(self, args):
        print("Hello World!")

    @classmethod
    def creator(cls):
        return HelloWorldCmd()

def initializePlugin(plugin):
    vendor ="Lizzet Clifton"
    version = "1.0.0"
    
    #storing the plugin function set so we can use it to register the command
    plugin_fn = om.MFnPlugin(plugin, vendor, version)

    try:
        plugin_fn.registerCommand(HelloWorldCmd.COMMAND_NAME, HelloWorldCmd.creator)
    except:
        om.MGlobal.displayError("Failed to register command: {0}".format(HelloWorldCmd))

def uninitializePlugin(plugin):
    plugin_fn = om.MFnPlugin(plugin)
    
    try:
        plugin_fn.deregisterCommand(HelloWorldCmd.COMMAND_NAME)
    except:
        om.MGlobal.displayError("Failed to deregister command: {0}".format(HelloWorldCmd))

if __name__ == "__main__":
    plugin_name = "helloWorld.py"
    
    mc.evalDeferred('if mc.pluginInfo("{0}", q=True, loaded=True): mc.unloadPlugin("{0}")'.format(plugin_name))
    mc.evalDeferred('if not mc.pluginInfo("{0}", q=True, loaded=True): mc.loadPlugin("{0}")'.format(plugin_name))