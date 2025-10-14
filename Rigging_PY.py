import maya.cmds as mc

def createSkeleton():
    #spine
    createJoints((0,6.108,0), 'c', 'waist', 'BIND')
    createJoints((0,6.792,0), 'c', 'Spine1', 'BIND')
    createJoints((0,7.743,0), 'c', 'Spine2', 'BIND')
    createJoints((0,8.701,0), 'c', 'Spine3', 'BIND')
    createJoints((0,9.252,0), 'c', 'Neck', 'BIND')
    createJoints((0,9.87,0), 'c', 'Head', 'BIND')
    createJoints((0,11.1,0), 'c', 'HeadTop_End', 'REF')

    #righarm
    createJoints((-0.559,9.028,0), 'L', 'RightShoulder', 'BIND')
    createJoints((-1.212,8.954,0), 'L', 'RightArm', 'BIND')
    createJoints((-2.591,8.939,0), 'L', 'RightForearm', 'BIND')
    createJoints((-4.408,8.969,0), 'L', 'RightHand', 'BIND')
    createJoints((-4.589,8.889,0.062), 'L', 'RightHandThumb1', 'BIND')
    createJoints((-4.712,8.788,0.168), 'L', 'RightHandThumb2', 'BIND')
    createJoints((-4.85,8.697,0.237), 'L', 'RightHandThumb3', 'BIND')
    createJoints((-5.007,8.616,0.305), 'L', 'RightHandThumb4', 'END')

    #leftarm
    createJoints((0.648,9.028,0), 'L', 'LeftShoulder', 'BIND')
    createJoints((1.3,8.954,0), 'L', 'LeftArm', 'BIND')
    createJoints((2.68,8.939,0), 'L', 'LeftForearm', 'BIND')
    createJoints((4.386,8.985,0), 'L', 'LeftHand', 'BIND')
    createJoints((0,0,0), 'L', '', 'BIND')
    createJoints((0,0,0), 'L', '', 'BIND')
    createJoints((0,0,0), 'L', '', 'BIND')
    createJoints((0,0,0), 'L', '', 'BIND')


    createJoints((0,0,0), 'L', '', 'BIND')
    createJoints((0,0,0), 'L', '', 'BIND')
    createJoints((0,0,0), 'L', '', 'BIND')
    createJoints((0,0,0), 'L', '', 'BIND')
    createJoints((0,0,0), 'L', '', 'BIND')
    createJoints((0,0,0), 'L', '', 'BIND')
    createJoints((0,0,0), 'L', '', 'BIND')
    createJoints((0,0,0), 'L', '', 'BIND')
    createJoints((0,0,0), 'L', '', 'BIND')


def createJoints(pos, alignment, name, suffix):
    mc.select(cl = True)
    mc.joint(p=pos, n= alignment + '__' + name + '__' + 'JNT' + '__' + suffix)

createSkeleton()



createJoints((0,0,0), 'L', '', 'BIND')