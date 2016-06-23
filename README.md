# Rigify_DeformBones

Rigify script, which remove deformation from DEF-xxx bones and add deformation to ORG-xxx bones. This allows the Rigify rig to be imported into Unity and be able to use it with Mecanim humanoid setup. 

---

###### **Rigify_script.py**

This script contains only the code to change DEF-xxx bones into ORG-xxx bones. You have to run it manualy. 

-

###### **Rigify4Mecanim.py**

This script is addon. It creates a buttons in generated rig from Rigify addon. You can find those buttons at the bottom of Armature tab. 

There is button for converting the Rigify rig into Unity Mecanim ready rig. And also a button to convert it back to Rigify rig. 

There is one more button for exporting the final rig and mesh into fbx file. You have to specify (or select) path and file name (with *.fbx extension) and it will take the rig and mesh (which is child of the rig... if it is not you have to shift+select the mesh manually) and creates an fbx file with only the deformation bones (so no unneeded bones are exported and the rig is clean in unity).

**_Installation:_** 
- You have to put it into %blender_directory%/scripts/addons
- Open File -> User Preferences -> Addons -> under Rigging category, there is Rigify to Unity addon (enable it) 
