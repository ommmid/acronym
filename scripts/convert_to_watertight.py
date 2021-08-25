# The meshes (models-OBJ.zip) downloaded from ShapeNetSem (https://shapenet.org/download/shapenetsem) are not ready to be laoded in trimesh
# We have to convert them to the watertight versions using Manifol software
# Also, for each object I will create a separate folder as that is how 'load_mesh' from acronym_tools works. To load the 
# mesh it need a folder like /meshes/Mug/shapenet_id.obj

# ----------- save the watertight in <meshes>/<object name>/
# 1) extract the object name nad shapent id from acronym/grasps
# 2) with that id go to shapenetsem-models and extract the right obj file
# 3) use the Manfold software to make the watertight version of the obj file
# 4) save the new obj file in acronym/meshes/<object name>


import mypy
import subprocess

acronym_grasp_path = '/home/oheidari/acronym/data/acronym/grasps/'
acronym_mesh_path = '/home/oheidari/acronym/data/acronym/meshes/'
shapenetsem_path = '/home/oheidari/acronym/data/shapenetsem-models/'

fnames = mypy.find_files(acronym_grasp_path + '*')

for object in fnames:
    object_name, shapenet_id, object_scale = mypy.parse_(object, with_extension=True)
    # print(f'object name: {object_name} | shapenet id: {shapenet_id} | scale: {object_scale}')

    manifold_input = shapenetsem_path + shapenet_id + '.obj'
    manifold_output = acronym_mesh_path + shapenet_id + '.obj'

    subprocess.run('/home/oheidari/Manifold/build/manifold ' +  manifold_input + ' ' + manifold_output, shell = True)
    subprocess.run('cp ' + shapenetsem_path + shapenet_id + '.mtl ' + acronym_mesh_path, shell = True)
