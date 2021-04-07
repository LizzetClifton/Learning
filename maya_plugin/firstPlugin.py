import maya.api.OpenMaya as om #2.0
import maya.cmds as mc

#necessary for 2.0
def maya_useNewAPI():
    pass

#required function to initialize
def initializePlugin(plugin): #plugin is the MObject
    #to register things like commands or nodes, we need to create an instance of an MFN plugin (a plugin function set) or we can pass in a vendor (author) name and the version numebr of the plugin
    vendor ="Lizzet Clifton"
    version = "1.0.0"
    #initialize function set here
    om.MFnPlugin(plugin, vendor, version)

def uninitializePlugin(plugin): #plugin MObject that can be accessed using a function set
    #this is where any nodes, commands, tools, etc. are de-registered
    pass #we use pass for now because we didn't initialize anything