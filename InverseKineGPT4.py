# Import toolboxes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Global Variables
# Link Lengths
L1, L2, L3, L4 = 10, 10, 10, 10

# End Effector Position
x, y, z = 15, 15, 15

def inverse_kinematics_4r_3d(x, y, z, L1, L2, L3, L4):
    # Calculate the distance from the base to the projection of the end effector in the xy plane
    r1 = np.sqrt(x**2 + y**2)

    # Calculate the distance from the base to the end effector
    r2 = np.sqrt(x**2 + y**2 + z**2)

    # Calculate the angle between the base and the projection of the end effector in the xy plane
    phi = np.arctan2(y, x)

    # Calculate the angle between the second link and the projection of the end effector in the xy plane
    alpha = np.arccos((L2**2 - L4**2 + r2**2) / (2*L2*r2))

    # Calculate the angle between the third link and the end effector
    beta = np.arccos((L3**2 - r2**2 - L2**2) / (-2*L2*r2))

    # Calculate the angle between the second link and the third link
    gamma = np.arccos((r2**2 - L2**2 - L3**2) / (-2*L2*L3))

    # Calculate the joint angles
    t1 = np.arctan2(y, x)
    t2 = phi + alpha
    t3 = np.pi - gamma - beta
    t4 = np.arctan2(z, r1) - np.arctan2(L4*np.sin(t3), L2+L3*np.cos(t3))

    return t1, t2, t3, t4

# Compute the forward kinematics of the robot
posee, pos1, pos2, pos3, pos4 = forward_kinematics_4R(t1, t2, t3, t4, L1, L2, L3, L4)

# Establishes plot and plots EE position
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(posee[0], posee[1], posee[2], color='red', s=30)

# Plot the joint positions and origin
joint1_pos = np.array([pos1[0], pos1[1], pos1[2]])
joint2_pos = np.array([pos2[0], pos2[1], pos2[2]])
joint3_pos = np.array([pos3[0], pos3[1], pos3[2]])
joint4_pos = np.array([pos4[0], pos4[1], pos4[2]])
ax.scatter(0, 0, 0, color='blue', s=30)
ax.scatter(joint1_pos[0], joint1_pos[1], joint1_pos[2], color='blue', s=30)
ax.scatter(joint2_pos[0], joint2_pos[1], joint2_pos[2], color='blue', s=30)
ax.scatter(joint3_pos[0], joint3_pos[1], joint3_pos[2], color='blue', s=30)
ax.scatter(joint4_pos[0], joint4_pos[1], joint4_pos[2], color='blue', s=30)

# Plot the links as lines
ax.plot([0, joint1_pos[0]], [0, joint1_pos[1]], [0, joint1_pos[2]], color='black')
ax.plot([joint1_pos[0], joint2_pos[0]], [joint1_pos[1], joint2_pos[1]], [joint1_pos[2], joint2_pos[2]], color='black')
ax.plot([joint2_pos[0], joint3_pos[0]], [joint2_pos[1], joint3_pos[1]], [joint2_pos[2], joint3_pos[2]], color='black')
ax.plot([joint3_pos[0], joint4_pos[0]], [joint3_pos[1], joint4_pos[1]], [joint3_pos[2], joint4_pos[2]], color='black')
ax.plot([joint4_pos[0], posee[0]], [joint4_pos[1], posee[1]], [joint4_pos[2], posee[2]], color='black')

# Set the initial viewing position
ax.view_init(elev=25, azim=-45)

# Adjust the height and width of the viewing window
ax.set_box_aspect([1, 1, 0.7])  # Set the aspect ratio of the plot

# Adjust the height and width of the window in which the plot is displayed
fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)  # Adjust the margins of the plot
fig.set_size_inches(8, 8)  # Set the size of the window in inches

# Add labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3R Forward Kinematics')

# Set the boundaries of the graph
ax.set_xlim([-50, 200])
ax.set_ylim([-200, 200])
ax.set_zlim([-10, 300])


# Show the plot
plt.show()

