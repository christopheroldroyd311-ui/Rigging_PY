print ("Loading userSetup Script")

###### For Development with VSCODE #####
print ("Loading VSCODE Plugin Command Ports")

import maya.cmds as cmds

cmds.commandPort(name="localhost:5678", stp="python")
cmds.commandPort(name="localhost:7001", stp="mel")

##### Start up Code for my Tool ######
print ("Loading My Maya Tool")

# import maya.utils

from MTool import Rigging_PY as mTool

def ToolStartup():

    mTool.LaunchToolWindow()
    
    print ("Tool Was Started Successfully!")

ToolStartup()