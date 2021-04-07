import maya.api.OpenMaya as om #2.0
import maya.cmds as mc

#necessary for 2.0
def maya_useNewAPI():
    pass

#required function to initialize
def initializePlugin(plugin): #plugin is the MObject
    #to register things like commands or nodes, we need to create an instance of an MFN plugin (a plugin function set) or we can pass in a vendor (author) name and the version number of the plugin
    vendor ="Lizzet Clifton"
    version = "1.0.0"
    #initialize function set here
    om.MFnPlugin(plugin, vendor, version)

def uninitializePlugin(plugin): #plugin MObject that can be accessed using a function set
    #this is where any nodes, commands, tools, etc. are de-registered
    pass #we use pass for now because we didn't initialize anything

#adding this in order to automatically unload and reload the plugin after a code change (in dev environment)
if __name__ == "__main__":
    plugin_name = "firstPlugin.py"
    #deferring commands, we are passing in python commands as a string
    #checking if loaded, if yes, unload
    mc.evalDeferred('if mc.pluginInfo("{0}", q=True, loaded=True): mc.unloadPlugin("{0}")'.format(plugin_name))
    #loading in
    mc.evalDeferred('if not mc.pluginInfo("{0}", q=True, loaded=True): mc.loadPlugin("{0}")'.format(plugin_name))
    