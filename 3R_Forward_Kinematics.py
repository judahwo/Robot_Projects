# Import toolboxes

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# This program employs forward kinematics for a 3R Robot in 3D
# The function, forward_kinematics_4R, is passed link lengths and joint angles, and returns joint and end effectors
# positions. The program plots the links, joint and end effector positions.

# Define link lengths
L1 = 25
L2 = 100
L3 = 95
L4 = 80
L5 = 10

# Define the joint angles
t1 = 0
t2 = 1.9204
t3 = -0.8430
t4 = -1.508

#   Main function, receives link lengths and joint angles, returns joint and end effector positions
def forward_kinematics_3R(t1, t2, t3, t4, L1, L2, L3, L4):

    # Convert angles from degrees to radians
    # t1 = np.radians(t1)
    # t2 = np.radians(t2)
    # t3 = np.radians(t3)

    # Frame to frame transformation matrices
    T01 = np.array([[np.cos(t1), 0, np.sin(t1), 0],
                   [np.sin(t1), 0, -np.cos(t1), 0],
                   [0, 1, 0, L1],
                   [0, 0, 0, 1]])

    T12 = np.array([[np.cos(t2), -np.sin(t2), 0, L2*np.cos(t2)],
                    [np.sin(t2), np.cos(t2), 0, L2*np.sin(t2)],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

    T23 = np.array([[np.cos(t3), -np.sin(t3), 0, L3*np.cos(t3)],
                    [np.sin(t3), np.cos(t3), 0, L3*np.sin(t3)],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

    T34 = np.array([[np.cos(t4), -np.sin(t4), 0, L3 * np.cos(t4)],
                    [np.sin(t4), np.cos(t4), 0, L3 * np.sin(t4)],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

    T45 = np.array([[1, 0, 0, L5],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

    # Joint and EE homogenous transformation matrices
    T02 = np.dot(T01, T12)
    T03 = np.dot(T02, T23)
    T04 = np.dot(T03, T34)
    T05 = np.dot(T04, T45)

    # Extract joint and EE positions from transformation matrices
    posee = T05[:3, 3]
    pos1 = T01[:3,3]
    pos2 = T02[:3,3]
    pos3 = T03[:3,3]
    pos4 = T04[:3,3]

    return posee, pos1, pos2, pos3, pos4

# Compute the forward kinematics of the robot
posee, pos1, pos2, pos3, pos4 = forward_kinematics_3R(t1, t2, t3, t4, L1, L2, L3, L4)

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

