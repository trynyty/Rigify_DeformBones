import re
import bpy
porg = re.compile('ORG-*')
for object in bpy.context.object.data.bones:
    object.use_deform = False
for object in bpy.context.object.data.bones:
    if porg.match(object.name):
        object.use_deform = True
bpy.context.object.data.bones['ORG-heel.L'].use_deform = False
bpy.context.object.data.bones['ORG-heel.02.L'].use_deform = False
bpy.context.object.data.bones['ORG-heel.R'].use_deform = False
bpy.context.object.data.bones['ORG-heel.02.R'].use_deform = False

