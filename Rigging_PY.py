import maya.cmds as mc 

def createSkeleton():
    createJoint((), 'c', '')


def createJoints(pos, alignment, name):
    mc.select(cl = True)
    mc.joint(p=pos, n= alignment + '__' = name + '__' + 'JNT')



createSkeleton()