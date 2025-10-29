from maya.cmds import cmds
import Rigging_PY as mtool

print ("Maya Tool Menu Module was Loaded")

def CreateToolMenu():


    tool_menu_name = "MyMayaToolMenu"

    if cmds.menu(tool_menu_name, exists=True):
        cmds.deleteUI(tool_menu_name, menu=True)

    custom_tool_menu = cmds.menu(tool_menu_name, label="My Maya Tool Menu", parent="MayaWindow", tearOff = True)

    cmds.menuItem(label="Create Cube", parent=custom_tool_menu, command=lambda val: cmds.polyCube(), image="polyCube.png")

    cmds.menuItem(label="Launch Window", 
                  parent=custom_tool_menu, 
                  command=lambda val: mtool.LaunchNonDockableWindow(), 
                  image="toolSettings.png")
    
    cmds.menuItem(label="Launch Dock Window", 
                  parent=custom_tool_menu, 
                  command=lambda val: mtool.LaunchDockableWindow(), 
                  image="toolSettings.png")
    
CreateToolMenu()