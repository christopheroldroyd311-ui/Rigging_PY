import maya.cmds as mc

def createSkeleton():

    #centerjoints
    waist = createJoints((0,6.108,0), 'c', 'waist', 'BIND')
    Spine1 = createJoints((0,6.792,0), 'c', 'Spine1', 'BIND', parent=waist)
    Spine2 = createJoints((0,7.743,0), 'c', 'Spine2', 'BIND', parent=Spine1)
    Spine3 = createJoints((0,8.701,0), 'c', 'Spine3', 'BIND', parent=Spine2)
    Neck = createJoints((0,9.252,0), 'c', 'Neck', 'BIND', parent=Spine3)
    Head = createJoints((0,9.87,0), 'c', 'Head', 'BIND', parent=Neck)
    HeadTop_End = createJoints((0,11.1,0), 'c', 'HeadTop_End', 'REF', parent=Head)

    #righarm
    RightShoulder = createJoints((-0.559,9.028,0), 'L', 'RightShoulder', 'BIND', parent=Spine3)
    RightArm = createJoints((-1.212,8.954,0), 'L', 'RightArm', 'BIND', parent=RightShoulder)
    RightForearm = createJoints((-2.591,8.939,0), 'L', 'RightForearm', 'BIND', parent=RightArm)
    RightHand = createJoints((-4.408,8.969,0), 'L', 'RightHand', 'REF', parent=RightForearm)

    RightHandThumb1 = createJoints((-4.589,8.889,0.062), 'L', 'RightHandThumb1', 'BIND', parent=RightHand)
    RightHandThumb2 = createJoints((-4.712,8.788,0.168), 'L', 'RightHandThumb2', 'BIND', parent=RightHandThumb1)
    RightHandThumb3 = createJoints((-4.85,8.697,0.237), 'L', 'RightHandThumb3', 'BIND', parent=RightHandThumb2)
    RightHandThumb4 = createJoints((-5.007,8.616,0.305), 'L', 'RightHandThumb4', 'END', parent=RightHandThumb3)

    RightHandIndex1 = createJoints((-4.991,8.96,0.057), 'L', 'RightHandIndex1', 'BIND', parent=RightHand)
    RightHandIndex2 = createJoints((-5.218,8.903,0.111), 'L', 'RightHandIndex2', 'BIND', parent=RightHandIndex1)
    RightHandIndex3 = createJoints((-5.396,8.868,0.143), 'L', 'RightHandIndex3', 'BIND', parent=RightHandIndex2)
    RightHandIndex4 = createJoints((-5.559,8.797,0.152), 'L', 'RightHandIndex4', 'END', parent=RightHandIndex3)

    RightHandMiddle1 = createJoints((-5.048,8.986,-0.071), 'L', 'RightHandMiddle1', 'BIND', parent=RightHand)
    RightHandMiddle2 = createJoints((-5.279,8.928,-0.079), 'L', 'RightHandMiddle2', 'BIND', parent=RightHandMiddle1)
    RightHandMiddle3 = createJoints((-5.437,8.885,-0.071), 'L', 'RightHandMiddle3', 'BIND', parent=RightHandMiddle2)
    RightHandMiddle4 = createJoints((-5.663,8.816,-0.038), 'L', 'RightHandMiddle4', 'END', parent=RightHandMiddle3)

    RightHandRing1 = createJoints((-5.057,8.998,-0.223), 'L', 'RightHandRing1', 'BIND', parent=RightHand)
    RightHandRing2 = createJoints((-5.262,8.966,-0.231), 'L', 'RightHandRing2', 'BIND', parent=RightHandRing1)
    RightHandRing3 = createJoints((-5.38,8.92,-0.223), 'L', 'RightHandRing3', 'BIND', parent=RightHandRing2)
    RightHandRing4 = createJoints((-5.559,8.843,-0.238), 'L', 'RightHandRing4', 'END', parent=RightHandRing3)

    RightHandPinky1 = createJoints((-5.021,8.998,-0.373), 'L', 'RightHandPinky1', 'BIND', parent=RightHand)
    RightHandPinky2 = createJoints((-5.139,8.966,-0.381), 'L', 'RightHandPinky2', 'BIND', parent=RightHandPinky1)
    RightHandPinky3 = createJoints((-5.257,8.92,-0.373), 'L', 'RightHandPinky3', 'BIND', parent=RightHandPinky2)
    RightHandPinky4 = createJoints((-5.418,08.863,-0.388), 'L', 'RightHandPinky4', 'END', parent=RightHandPinky3)

    #leftarm
    LeftShoulder = createJoints((0.559,9.028,0), 'L', 'LeftShoulder', 'BIND', parent=Spine3)
    LeftArm = createJoints((1.212,8.954,0), 'L', 'LeftArm', 'BIND', parent=LeftShoulder)
    LeftForearm = createJoints((2.591,8.939,0), 'L', 'LeftForearm', 'BIND', parent=LeftArm)
    LeftHand = createJoints((4.408,8.969,0), 'L', 'LeftHand', 'REF', parent=LeftForearm)

    LeftHandThumb1 = createJoints((4.589,8.889,0.062), 'L', 'LeftHandThumb1', 'BIND', parent=LeftHand)
    LeftHandThumb2 = createJoints((4.712,8.788,0.168), 'L', 'LeftHandThumb2', 'BIND', parent=LeftHandThumb1)
    LeftHandThumb3 = createJoints((4.85,8.697,0.237), 'L', 'LeftHandThumb3', 'BIND', parent=LeftHandThumb2)
    LeftHandThumb4 = createJoints((5.007,8.616,0.305), 'L', 'LeftHandThumb4', 'END', parent=LeftHandThumb3)

    LeftHandIndex1 = createJoints((4.991,8.96,0.057), 'L', 'LeftHandIndex1', 'BIND', parent=LeftHand)
    LeftHandIndex2 = createJoints((5.218,8.903,0.111), 'L', 'LeftHandIndex2', 'BIND', parent=LeftHandIndex1)
    LeftHandIndex3 = createJoints((5.396,8.868,0.143), 'L', 'LeftHandIndex3', 'BIND', parent=LeftHandIndex2)
    LeftHandIndex4 = createJoints((5.559,8.797,0.152), 'L', 'LeftHandIndex4', 'END', parent=LeftHandIndex3)

    LeftHandMiddle1 = createJoints((5.048,8.986,-0.071), 'L', 'LeftHandMiddle1', 'BIND', parent=LeftHand)
    LeftHandMiddle2 = createJoints((5.279,8.928,-0.079), 'L', 'LeftHandMiddle2', 'BIND', parent=LeftHandMiddle1)
    LeftHandMiddle3 = createJoints((5.437,8.885,-0.071), 'L', 'LeftHandMiddle3', 'BIND', parent=LeftHandMiddle2)
    LeftHandMiddle4 = createJoints((5.663,8.816,-0.038), 'L', 'LeftHandMiddle4', 'END', parent=LeftHandMiddle3)

    LeftHandRing1 = createJoints((5.057,8.998,-0.223), 'L', 'LeftHandRing1', 'BIND', parent=LeftHand)
    LeftHandRing2 = createJoints((5.262,8.966,-0.231), 'L', 'LeftHandRing2', 'BIND', parent=LeftHandRing1)
    LeftHandRing3 = createJoints((5.38,8.92,-0.223), 'L', 'LeftHandRing3', 'BIND', parent=LeftHandRing2)
    LeftHandRing4 = createJoints((5.559,8.843,-0.238), 'L', 'LeftHandRing4', 'END', parent=LeftHandRing3)

    LeftHandPinky1 = createJoints((5.021,8.998,-0.373), 'L', 'LeftHandPinky1', 'BIND', parent=LeftHand)
    LeftHandPinky2 = createJoints((5.139,8.966,-0.381), 'L', 'LeftHandPinky2', 'BIND', parent=LeftHandPinky1)
    LeftHandPinky3 = createJoints((5.257,8.92,-0.373), 'L', 'LeftHandPinky3', 'BIND', parent=LeftHandPinky2)
    LeftHandPinky4 = createJoints((5.418,08.863,-0.388), 'L', 'LeftHandPinky4', 'END', parent=LeftHandPinky3)

    #right leg 
    RightUpLeg = createJoints((-0.591,5.377,0), 'L', 'RightUpLeg', 'BIND', parent=waist)
    RightLeg = createJoints((-0.806,3.405,0), 'L', 'RightLeg', 'BIND', parent=RightUpLeg)
    RightFoot = createJoints((-0.95,0.67,0), 'L', 'RightFoot', 'BIND', parent=RightLeg)
    RightFootEnd = createJoints((-1.13,-0.009,0.774), 'L', 'RightFootEnd', 'END', parent=RightFoot)
 
    #LefLeg
    LeftUpLeg = createJoints((0.591,5.377,0), 'L', 'LeftUpLeg', 'BIND', parent=waist)
    LeftLeg = createJoints((0.806,3.405,0), 'L', 'LeftLeg', 'BIND', parent=LeftUpLeg)
    LeftFoot = createJoints((0.95,0.67,0), 'L', 'LeftFoot', 'BIND', parent=LeftLeg)
    LeftFootEnd = createJoints((1.13,-0.009,0.774), 'L', 'LeftFootEnd', 'END', parent=LeftFoot)

def createJoints(pos, alignment, name, suffix, radius=0.1, parent=None):

    if parent:
        mc.select(parent)
    else:
        mc.select(clear=True)

    joint_name = f"{alignment}__{name}__JNT__{suffix}"
    joint = mc.joint(p=pos, n=joint_name, radius=radius)

    print(f"Created joint: {joint} (radius={radius})")
    return joint

 
createSkeleton()

# def myUI():
#     if mc.window("myWindow", exists=True):
#         mc.deleteUI("myWindow")

#     # Create window
#     window = mc.window("myWindow", title="Simple UI", widthHeight=(300, 150))

#     # Layout
#     mc.columnLayout(adjustableColumn=True, rowSpacing=10)

#     # Buttons
#     for i in range(1, 6):
#         mc.button(label=f"Button {i}", command=lambda x, i=i: print(f"Button {i} clicked"))

#     # Slider
#     mc.text(label="Adjust Value:")
#     mc.floatSlider(min=0.0, max=10.0, value=5.0, step=0.1, dragCommand=lambda val: print(f"Slider value: {val}"))

#     mc.showWindow(window)

# # Run the UI
# myUI()

class CPAT(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindow









