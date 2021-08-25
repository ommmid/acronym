import trimesh
from acronym_tools import load_mesh, load_grasps, create_gripper_marker, create_coordinate_frame_marker
from trimesh.permutate import transform
import trimesh.transformations as transform

file_string = "/home/oheidari/acronym/data/examples/grasps/Mug_10f6e09036350e92b3f21f1137c3c347_0.0002682457830986903.h5"

T, success = load_grasps(file_string)
t = T[3]
# t = transform.identity_matrix()
# t[0,3] = 0 
# t[1,3] = 0 
# t[2,3] = 0
gripper = create_gripper_marker(color=[0, 250, 0], tube_radius=0.0005).apply_transform(t)


w = transform.identity_matrix()
world_frame = create_coordinate_frame_marker(color=[0, 250, 0], tube_radius=0.0005).apply_transform(w)

s = transform.identity_matrix()
s[0,3] = 1 
s[1,3] = 1 
s[2,3] = 0
box = trimesh.creation.box(extents=[0.5, 0.5, 0.5], transform=s)

m = transform.identity_matrix()
m[0,3] = 0 
m[1,3] = 0 
m[2,3] = 0
mug = load_mesh(file_string, "../data/examples/").apply_transform(m)

scene = trimesh.Scene(gripper + mug + world_frame + box )

print('gripper with respect to world:\n', t)
 
# visualize the scene
scene.show()
