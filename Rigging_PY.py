import maya.cmds as mc
import maya.cmds as cmds
import maya.mel as mel


print("maya module was loaded")

##---------------------------SkeletonJoints-------------------------------##


def createJoints(pos, alignment, name, suffix, radius=0.1, parent=None):

    if parent:
        mc.select(parent)
    else:
        mc.select(clear=True)

    joint_name = f"{alignment}__{name}__JNT__{suffix}"
    joint = mc.joint(p=pos, n=joint_name, radius=radius)

    print(f"Created joint: {joint} (radius={radius})")
    return joint


def createSkeleton(scale=1.0):

    print("DEBUG scale:", scale, type(scale))

    if not isinstance(scale, (int, float)):
        mc.error("Scale must be a number")

    if cmds.objExists('c_waist_JNT_jnt'):
        cmds.delete('c_waist_JNT_jnt')

    def scaled(pos):
        return (pos[0] * scale, pos[1] * scale, pos[2] * scale)

    #centerjoints
    waist = createJoints(scaled((0,6.108,0)), 'c', 'waist', 'BIND')
    Spine1 = createJoints(scaled((0,6.792,0)), 'c', 'Spine1', 'BIND', parent=waist)
    Spine2 = createJoints(scaled((0,7.743,0)), 'c', 'Spine2', 'BIND', parent=Spine1)
    Spine3 = createJoints(scaled((0,8.701,0)), 'c', 'Spine3', 'BIND', parent=Spine2)
    Neck = createJoints(scaled((0,9.252,0)), 'c', 'Neck', 'BIND', parent=Spine3)
    Head = createJoints(scaled((0,9.87,0)), 'c', 'Head', 'BIND', parent=Neck)
    HeadTop_End = createJoints(scaled((0,11.1,0)), 'c', 'HeadTop_End', 'REF', parent=Head)

    #righarm
    RightShoulder = createJoints(scaled((-0.559,9.028,0)), 'L', 'RightShoulder', 'BIND', parent=Spine3)
    RightArm = createJoints(scaled((-1.212,8.954,0)), 'L', 'RightArm', 'BIND', parent=RightShoulder)
    RightForearm = createJoints(scaled((-2.591,8.939,0)), 'L', 'RightForearm', 'BIND', parent=RightArm)
    RightHand = createJoints(scaled((-4.408,8.969,0)), 'L', 'RightHand', 'REF', parent=RightForearm)

    RightHandThumb1 = createJoints(scaled((-4.589,8.889,0.062)), 'L', 'RightHandThumb1', 'BIND', parent=RightHand)
    RightHandThumb2 = createJoints(scaled((-4.712,8.788,0.168)), 'L', 'RightHandThumb2', 'BIND', parent=RightHandThumb1)
    RightHandThumb3 = createJoints(scaled((-4.85,8.697,0.237)), 'L', 'RightHandThumb3', 'BIND', parent=RightHandThumb2)
    RightHandThumb4 = createJoints(scaled((-5.007,8.616,0.305)), 'L', 'RightHandThumb4', 'END', parent=RightHandThumb3)

    RightHandIndex1 = createJoints(scaled((-4.991,8.96,0.057)), 'L', 'RightHandIndex1', 'BIND', parent=RightHand)
    RightHandIndex2 = createJoints(scaled((-5.218,8.903,0.111)), 'L', 'RightHandIndex2', 'BIND', parent=RightHandIndex1)
    RightHandIndex3 = createJoints(scaled((-5.396,8.868,0.143)), 'L', 'RightHandIndex3', 'BIND', parent=RightHandIndex2)
    RightHandIndex4 = createJoints(scaled((-5.559,8.797,0.152)), 'L', 'RightHandIndex4', 'END', parent=RightHandIndex3)

    RightHandMiddle1 = createJoints(scaled((-5.048,8.986,-0.071)), 'L', 'RightHandMiddle1', 'BIND', parent=RightHand)
    RightHandMiddle2 = createJoints(scaled((-5.279,8.928,-0.079)), 'L', 'RightHandMiddle2', 'BIND', parent=RightHandMiddle1)
    RightHandMiddle3 = createJoints(scaled((-5.437,8.885,-0.071)), 'L', 'RightHandMiddle3', 'BIND', parent=RightHandMiddle2)
    RightHandMiddle4 = createJoints(scaled((-5.663,8.816,-0.038)), 'L', 'RightHandMiddle4', 'END', parent=RightHandMiddle3)

    RightHandRing1 = createJoints(scaled((-5.057,8.998,-0.223)), 'L', 'RightHandRing1', 'BIND', parent=RightHand)
    RightHandRing2 = createJoints(scaled((-5.262,8.966,-0.231)), 'L', 'RightHandRing2', 'BIND', parent=RightHandRing1)
    RightHandRing3 = createJoints(scaled((-5.38,8.92,-0.223)), 'L', 'RightHandRing3', 'BIND', parent=RightHandRing2)
    RightHandRing4 = createJoints(scaled((-5.559,8.843,-0.238)), 'L', 'RightHandRing4', 'END', parent=RightHandRing3)

    RightHandPinky1 = createJoints(scaled((-5.021,8.998,-0.373)), 'L', 'RightHandPinky1', 'BIND', parent=RightHand)
    RightHandPinky2 = createJoints(scaled((-5.139,8.966,-0.381)), 'L', 'RightHandPinky2', 'BIND', parent=RightHandPinky1)
    RightHandPinky3 = createJoints(scaled((-5.257,8.92,-0.373)), 'L', 'RightHandPinky3', 'BIND', parent=RightHandPinky2)
    RightHandPinky4 = createJoints(scaled((-5.418,08.863,-0.388)), 'L', 'RightHandPinky4', 'END', parent=RightHandPinky3)

    #leftarm
    LeftShoulder = createJoints(scaled((0.559,9.028,0)), 'L', 'LeftShoulder', 'BIND', parent=Spine3)
    LeftArm = createJoints(scaled((1.212,8.954,0)), 'L', 'LeftArm', 'BIND', parent=LeftShoulder)
    LeftForearm = createJoints(scaled((2.591,8.939,0)), 'L', 'LeftForearm', 'BIND', parent=LeftArm)
    LeftHand = createJoints(scaled((4.408,8.969,0)), 'L', 'LeftHand', 'REF', parent=LeftForearm)

    LeftHandThumb1 = createJoints(scaled((4.589,8.889,0.062)), 'L', 'LeftHandThumb1', 'BIND', parent=LeftHand)
    LeftHandThumb2 = createJoints(scaled((4.712,8.788,0.168)), 'L', 'LeftHandThumb2', 'BIND', parent=LeftHandThumb1)
    LeftHandThumb3 = createJoints(scaled((4.85,8.697,0.237)), 'L', 'LeftHandThumb3', 'BIND', parent=LeftHandThumb2)
    LeftHandThumb4 = createJoints(scaled((5.007,8.616,0.305)), 'L', 'LeftHandThumb4', 'END', parent=LeftHandThumb3)

    LeftHandIndex1 = createJoints(scaled((4.991,8.96,0.057)), 'L', 'LeftHandIndex1', 'BIND', parent=LeftHand)
    LeftHandIndex2 = createJoints(scaled((5.218,8.903,0.111)), 'L', 'LeftHandIndex2', 'BIND', parent=LeftHandIndex1)
    LeftHandIndex3 = createJoints(scaled((5.396,8.868,0.143)), 'L', 'LeftHandIndex3', 'BIND', parent=LeftHandIndex2)
    LeftHandIndex4 = createJoints(scaled((5.559,8.797,0.152)), 'L', 'LeftHandIndex4', 'END', parent=LeftHandIndex3)

    LeftHandMiddle1 = createJoints(scaled((5.048,8.986,-0.071)), 'L', 'LeftHandMiddle1', 'BIND', parent=LeftHand)
    LeftHandMiddle2 = createJoints(scaled((5.279,8.928,-0.079)), 'L', 'LeftHandMiddle2', 'BIND', parent=LeftHandMiddle1)
    LeftHandMiddle3 = createJoints(scaled((5.437,8.885,-0.071)), 'L', 'LeftHandMiddle3', 'BIND', parent=LeftHandMiddle2)
    LeftHandMiddle4 = createJoints(scaled((5.663,8.816,-0.038)), 'L', 'LeftHandMiddle4', 'END', parent=LeftHandMiddle3)

    LeftHandRing1 = createJoints(scaled((5.057,8.998,-0.223)), 'L', 'LeftHandRing1', 'BIND', parent=LeftHand)
    LeftHandRing2 = createJoints(scaled((5.262,8.966,-0.231)), 'L', 'LeftHandRing2', 'BIND', parent=LeftHandRing1)
    LeftHandRing3 = createJoints(scaled((5.38,8.92,-0.223)), 'L', 'LeftHandRing3', 'BIND', parent=LeftHandRing2)
    LeftHandRing4 = createJoints(scaled((5.559,8.843,-0.238)), 'L', 'LeftHandRing4', 'END', parent=LeftHandRing3)

    LeftHandPinky1 = createJoints(scaled((5.021,8.998,-0.373)), 'L', 'LeftHandPinky1', 'BIND', parent=LeftHand)
    LeftHandPinky2 = createJoints(scaled((5.139,8.966,-0.381)), 'L', 'LeftHandPinky2', 'BIND', parent=LeftHandPinky1)
    LeftHandPinky3 = createJoints(scaled((5.257,8.92,-0.373)), 'L', 'LeftHandPinky3', 'BIND', parent=LeftHandPinky2)
    LeftHandPinky4 = createJoints(scaled((5.418,08.863,-0.388)), 'L', 'LeftHandPinky4', 'END', parent=LeftHandPinky3)

    #right leg 
    RightUpLeg = createJoints(scaled((-0.591,5.377,0)), 'L', 'RightUpLeg', 'BIND', parent=waist)
    RightLeg = createJoints(scaled((-0.806,3.405,0)), 'L', 'RightLeg', 'BIND', parent=RightUpLeg)
    RightFoot = createJoints(scaled((-0.95,0.67,0)), 'L', 'RightFoot', 'BIND', parent=RightLeg)
    RightFootEnd = createJoints(scaled((-1.13,-0.009,0.774)), 'L', 'RightFootEnd', 'END', parent=RightFoot)
 
    #LefLeg
    LeftUpLeg = createJoints(scaled((0.591,5.377,0)), 'L', 'LeftUpLeg', 'BIND', parent=waist)
    LeftLeg = createJoints(scaled((0.806,3.405,0)), 'L', 'LeftLeg', 'BIND', parent=LeftUpLeg)
    LeftFoot = createJoints(scaled((0.95,0.67,0)), 'L', 'LeftFoot', 'BIND', parent=LeftLeg)
    LeftFootEnd = createJoints(scaled((1.13,-0.009,0.774)), 'L', 'LeftFootEnd', 'END', parent=LeftFoot)

    mc.select(clear=True)
    print(f"Skeleton spawned at scale {scale}")

def lockToCenter():
    mc.select('C_*_JNT')
    selJNTS = mc.Is(sl=True)
    for jnt in selJNTS:
        mc.setAttr(jnt + '.tx', lock = True, keyable = True, channelBox = False)

def UnlockCentre():
    mc.select('C_*_JNT')
    selJNTS = mc.Is(sl=True)
    for jnt in selJNTS:
        mc.setAttr(jnt + '.tx', lock = False, keyable = True, channelBox = False)

def createSkeletonBase():
    createSkeleton()
    createJoints()
    lockToCenter()
    mc.select(cl=True)

##--------------------------------Bind Skin----------------------------------##

def BindSkin():
    sel = mc.ls(selection=True)

    if not sel or len(sel) < 2:
        mc.warning("Select one or more meshes FIRST, then the skeleton root joint(s).")
        return

    # Separate meshes and joints
    meshes = []
    root_joints = []

    for obj in sel:
        shapes = mc.listRelatives(obj, shapes=True, fullPath=True) or []
        if shapes and mc.nodeType(shapes[0]) == "mesh":
            meshes.append(obj)
        elif mc.nodeType(obj) == "joint":
            root_joints.append(obj)

    if not meshes:
        mc.warning("No valid meshes selected.")
        return
    if not root_joints:
        mc.warning("No joints selected.")
        return

    children_joints = mc.listRelatives(allDescendents=True, type='joint')
    mc.select(children_joints, add=True)

    if not children_joints:
        mc.warning("No joints found under selected roots.")
        return

    for mesh in meshes:
        try:
            skin_name = f"{mesh}_skinCluster"
            if mc.objExists(skin_name):
                mc.delete(skin_name)

            mc.select(clear=True)

            mc.skinCluster(
                children_joints,  
                mesh,
                toSelectedBones=False,
                maximumInfluences=4,
                normalizeWeights=1,
                name=skin_name)

            print(f"Bound '{mesh}' to {len(children_joints)} joints successfully.")
        except Exception as e:
            mc.warning(f" Failed to bind")

    print("Skin binding complete.")


##--------------------------------Delete history----------------------------##

def DeleteHistory():
    sel = mc.ls(selection=True)
    cmds.delete(sel, constructionHistory = True)

    print("History has been deleted.")

##--------------------------------Weight painting--------------------------------##

def WeightPaint():
    if not cmds.pluginInfo('artDeformers', query=True, loaded=True):
        try:
            cmds.loadPlugin('artDeformers')
            print(" Loaded 'artDeformers' plugin.")
        except Exception as e:
            cmds.error(f" Could not load 'artDeformers' plugin")
            return

    # ---- Step 2: Get selection ----
    selection = cmds.ls(selection=True, type='transform')
    if not selection:
        cmds.error("Please select one or more skinned meshes.")
        return

    valid_meshes = []

    for obj in selection:
        shapes = cmds.listRelatives(obj, shapes=True, type='mesh') or []
        if not shapes:
            cmds.warning(f"Skipping '{obj}': no mesh shape found.")
            continue

        # Check if it has a skinCluster
        history = cmds.listHistory(obj) or []
        skins = cmds.ls(history, type='skinCluster')
        if not skins:
            cmds.warning(f"Skipping '{obj}': no skinCluster found.")
            continue

        valid_meshes.append(obj)

    if not valid_meshes:
        cmds.error("No valid skinned meshes selected.")
        return

    # ---- Step 3: Open Paint Skin Weights Tool ----
    try:
        mel.eval('artPaintSkinWeightsTool;')
    except Exception as e:
        cmds.error(f" Could not open Paint Skin Weights Tool: {e}")
        return

    # Select the last valid mesh for painting
    cmds.select(valid_meshes[-1])
    print(f" Opened Paint Skin Weights Tool for '{valid_meshes[-1]}'.")


##--------------------------Single Function to Launch Dockable or Non Dockable-----------------------------------##

def LaunchWindow(Dockable = False):
    maya_window_id = "w_maya_ui"

    if Dockable:
        maya_window_id += "_dock"
        if cmds.workspaceControl(maya_window_id, exists=True):
            cmds.deleteUI(maya_window_id)

        cmds.workspaceControl(maya_window_id, label= "My Maya Dockable Tool", widthProperty="fixed", initialWidth=300, retain=False)
    else:
        maya_window_id = 'w_maya_ui'
        if cmds.window(maya_window_id, ex=True):
            cmds.deleteUI(maya_window_id, window = True)

        cmds.window(maya_window_id, title='My Maya Tool', widthHeight=(500,600))
    
    SimpleUI()

    if not Dockable:
        cmds.showWindow(maya_window_id)

def LaunchToolWindow(Dockable = False):
    if Dockable:
        LaunchDockableWindow()
    else:
        LaunchNonDockableWindow()

def LaunchDockableWindow():
    maya_ctrl_window = "w_dock_maya_ui"

    if cmds.workspaceControl(maya_ctrl_window, exists=True):
        cmds.deleteUI(maya_ctrl_window)

    cmds.workspaceControl(maya_ctrl_window, label= "My Maya Dockable Tool", widthProperty="fixed", initialWidth=300, retain=False)

    SimpleUI()

def LaunchNonDockableWindow():
    maya_window = 'w_maya_ui'
    if cmds.window(maya_window, ex=True):
        cmds.deleteUI(maya_window, window = True)

    cmds.window(maya_window, title='My Maya Tool', widthHeight=(500,600))

    SimpleUI()

    # show window
    cmds.showWindow(maya_window)










##--------------------------------UI----------------------------------##

class SimpleUI:
    def __init__(self):

        def BuildWindowUI(parent=None):
            # build main tool UI here
            if cmds.window("simpleUIWin", exists=True):
                cmds.deleteUI("simpleUIWin", menu=True)

            self.window = cmds.window("simpleUIWin", title="Simple Humanoid Rigger", widthHeight=(200, 100))
            cmds.columnLayout(adjustableColumn=True, rowSpacing=10)

            cmds.text(label='<font size="6">Rigging Tool</font>', align='center', bgc=[0.1, 0.1, 0.1])

            cmds.floatSliderGrp(
                "scaleSlider",
                label="Size of skeleton",
                field=True,
                minValue=0.1,
                maxValue=5.0,
                value=1.0,
                step=0.1
            )

            cmds.button(
                label="Spawn Skeleton",
                command=lambda *_: createSkeleton(
                    scale=cmds.floatSliderGrp("scaleSlider", q=True, value=True)
                ),
                height=40
            )

            cmds.button(label="Bind Skin", command=lambda *_: BindSkin(), height=40)
            cmds.button(label="Delete Selected History", command=lambda *_: DeleteHistory(), height=40)
            cmds.button(label="Weight Paint Skin", command=lambda *_: WeightPaint(), height=40)

            cmds.showWindow(self.window)

        def LaunchDockableWindow():
            maya_ctrl_window = "w_dock_maya_ui"

            if cmds.workspaceControl(maya_ctrl_window, exists=True):
                cmds.deleteUI(maya_ctrl_window)

            cmds.workspaceControl(maya_ctrl_window, label="My Maya Dockable Tool",
                                  widthProperty="fixed", initialWidth=300, retain=False)
            BuildWindowUI()

        def LaunchNonDockableWindow():
            maya_window = 'w_maya_ui'
            if cmds.window(maya_window, ex=True):
                cmds.deleteUI(maya_window, window=True)

            cmds.window(maya_window, title='My Maya Tool', widthHeight=(500, 600))
            BuildWindowUI()
            cmds.showWindow(maya_window)

        def LaunchToolWindow(Dockable=False):
            if Dockable:
                LaunchDockableWindow()
            else:
                LaunchNonDockableWindow()

        # launch default window
        LaunchToolWindow(Dockable=False)



# Run the UI
SimpleUI()






