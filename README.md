# Rigify into Unity Mecanim

Blender python script for Rigify rig, which remove deformation from DEF-xxx bones and add deformation to ORG-xxx bones. This allows the Rigify rig to be imported into Unity and be able to use it with Mecanim humanoid setup. 

---

###### **Rigify_script.py**

This script contains only the code to change DEF-xxx bones into ORG-xxx bones. You have to run it manualy. 

-

###### **Rigify4Mecanim.py**

This script is addon. It creates a buttons in generated rig from Rigify addon. You can find those buttons at the bottom of Data/Armature tab. 

There is button for converting the Rigify rig into Unity Mecanim ready rig. And also a button to convert it back to Rigify rig. 

There is one more button for exporting the final rig and mesh into fbx file. You have to specify (or select) path and file name (with *.fbx extension) and it will take the rig and mesh (which is child of the rig... if it is not you have to shift+select the mesh manually) and creates an fbx file with only the deformation bones (so no unnecessary bones are exported and the rig/hierarchy is clean in unity).      
This export uses "apply_unit_scale=False" option, so the final scale in Unity should be 1.

There is a checkbox for the experimental feature !Apply Transform! (from fbx exporter) which you can deselect if it's causing problems.

**_Installation:_** 
- Open File -> User Preferences -> Addons -> Instal from File... -> choose the downloaded script and install it
- You can find the Addon under Rigging category, there should be "Rigify to Unity" addon
