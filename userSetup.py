print ("Loading userSetup Script")

print ("Loading VSCODE Plugin Command Ports")

import maya.cmds as cmds

import maya.utils

def open_ports():
    import maya.cmds as cmds  
    try:
        for port, stp in [(5678, "python"), (7001, "mel")]:
            port_name = f"localhost:{port}"
            
            if cmds.commandPort(name=f":{port}", q=True):
                cmds.commandPort(name=f":{port}", close=True)
            
            cmds.commandPort(name=port_name, stp=stp)
            print(f"[userSetup] Opened command port: {port_name}")
    except Exception as e:
        print(f"[userSetup] Failed to open command ports: {e}")


maya.utils.executeDeferred(open_ports)


maya.utils.executeDeferred(open_ports)


print ("Loading My Maya Tool")

import Rigging_PY as mTool

def ToolStartup():

    mTool.LaunchToolWindow()
    
    print ("Tool Was Started Successfully!")

ToolStartup()