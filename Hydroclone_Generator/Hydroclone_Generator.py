import numpy as np
import trimesh

# Define cylinder parameters
r = 10 # radius of cylinder
h = 20 # height of cylinder
num_points = 100 # number of points to sample along circumference

# Generate cylinder points using Pitt method
if num_points > 0:
    theta = np.linspace(0, 2*np.pi, num_points)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = np.linspace(0, h, num_points)
    points = np.column_stack((x, y, z))
else:
    print("Error: num_points must be greater than 0")
    exit()

# Create faces for cylinder mesh
if len(points) > 1:
    faces = []
    for i in range(num_points - 1):
        faces.append([i, i+1, num_points+i+1])
        faces.append([i, num_points+i+1, num_points+i])

    # Add last face to connect end points
    faces.append([num_points-1, 0, num_points])
    faces.append([num_points-1, num_points, 2*num_points-1])
else:
    print("Error: not enough points to create faces")
    exit()

# Create mesh object
cylinder_mesh = trimesh.Trimesh(points=points, faces=faces)

print("points:", points)
print("faces:", faces)

# Save mesh to STL file
cylinder_mesh.export(r"C:\Users\saldridge\Desktop\hydrocyclone.stl")
