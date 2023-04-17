import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# Define link lengths
L1 = 25
L2 = 100
L3 = 95
L4 = 80
L5 = 10

# Your given function
def forward_kinematics_4R(t1, t2, t3, t4, L1, L2, L3, L4, L5):

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
    posee = T05[:3,3]
    pos1 = T01[:3,3]
    pos2 = T02[:3,3]
    pos3 = T03[:3,3]
    pos4 = T04[:3,3]

    return posee, pos1, pos2, pos3, pos4

# Linear interpolation
def interpolate_angles(start_angles, end_angles, steps):
    return np.linspace(start_angles, end_angles, steps)

# Define joint angles for each pose
pose1_angles = np.array([0, 0, 0, 0])
pose2_angles = np.array([np.pi/4, np.pi/4, np.pi/4, np.pi/4])
pose3_angles = np.array([np.pi/2, np.pi/2, np.pi/2, np.pi/2])

# Define the number of steps for interpolation
steps = 100

# Interpolate between poses
path1 = interpolate_angles(pose1_angles, pose2_angles, steps)
path2 = interpolate_angles(pose2_angles, pose3_angles, steps)

# Combine paths
path = np.concatenate((path1, path2), axis=0)

# Animation setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-50, 200])
ax.set_ylim([-200, 200])
ax.set_zlim([-10, 300])

# Set the initial viewing position
ax.view_init(elev=25, azim=-45)

# Adjust the height and width of the viewing window
ax.set_box_aspect([1, 1, 0.7])  # Set the aspect ratio of the plot

# Adjust the height and width of the window in which the plot is displayed
fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)  # Adjust the margins of the plot
fig.set_size_inches(8, 8)  # Set the size of the window in inches

# Animate the motion
for angles in path:
    t1, t2, t3, t4 = angles
    posee, pos1, pos2, pos3, pos4 = forward_kinematics_4R(t1, t2, t3, t4, L1, L2, L3, L4, L5)

    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-200, 200])
    ax.set_ylim([-200, 200])
    ax.set_zlim([-10, 200])

    # Plot the arm's links
    ax.plot([0, pos1[0], pos2[0], pos3[0], pos4[0], posee[0]],
            [0, pos1[1], pos2[1], pos3[1], pos4[1], posee[1]],
            [0, pos1[2], pos2[2], pos3[2], pos4[2], posee[2]], 'o-')

    plt.draw()
    plt.pause(0.01)

plt.show()
