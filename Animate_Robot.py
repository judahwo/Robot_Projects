import numpy as np
import matplotlib.pyplot as plt

# This program employs forward kinematics for a 4R Robot in 3D
# The function, forward_kinematics_4R, is passed link lengths and joint angles, and returns joints and end effector
# positions. The program plots and animates the motion of the robot arm.

# Define link lengths
L1 = 25
L2 = 100
L3 = 95
L4 = 80
L5 = 25

# Forward kinematics main function
def forward_kinematics_4R(t1, t2, t3, t4, L1, L2, L3, L4, L5):

    # Define the homogenous transformation matrices
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

    # Calculate the transformation matrices
    T02 = np.dot(T01, T12)
    T03 = np.dot(T02, T23)
    T04 = np.dot(T03, T34)
    T05 = np.dot(T04, T45)

    # Calculate the end effector and joint positions
    posee = T05[:3,3]
    pos1 = T01[:3,3]
    pos2 = T02[:3,3]
    pos3 = T03[:3,3]
    pos4 = T04[:3,3]

    return posee, pos1, pos2, pos3, pos4

# Define a function to interpolate between joint angles
def interpolate_angles(start_angles, end_angles, steps):
    return np.linspace(start_angles, end_angles, steps)

# Define the joint angles for each pose
pose1_angles = np.array([0, 2.1204, -0.8430, -1.508])
pose2_angles = np.array([1.5, 2.1204, -0.8430, -1.508])
pose3_angles = np.array([1.5, 1.1204, -1.2430, -1.508])
pose4_angles = np.array([1.5, 1.5204, -0.8430, -1.508])
pose5_angles = np.array([-1.5, 1.5204, -0.8430, -1.508])
pose6_angles = np.array([-1.5, 1.1204, -1.2430, -1.508])
pose7_angles = np.array([0, 2.1204, -0.8430, -1.508])

# Define the number of steps to interpolate between poses
steps = 30

# Interpolate between poses (function call)
path1 = interpolate_angles(pose1_angles, pose2_angles, steps)
path2 = interpolate_angles(pose2_angles, pose3_angles, steps)
path3 = interpolate_angles(pose3_angles, pose4_angles, steps)
path4 = interpolate_angles(pose4_angles, pose5_angles, steps)
path5 = interpolate_angles(pose5_angles, pose6_angles, steps)
path6 = interpolate_angles(pose6_angles, pose7_angles, steps)

# Concatenate the paths
path = np.concatenate((path1, path2, path3, path4, path5, path6), axis=0)

# Create a figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the viewing angle
ax.view_init(elev=25, azim=-45)

# Set the aspect ratio of the plot, adjust the margins, and size of the window
ax.set_box_aspect([1, 1, 0.7])  # Set the aspect ratio of the plot
fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)  # Adjust the margins of the plot
fig.set_size_inches(8, 8)  # Set the size of the window in inches

# Animate the arm
for angles in path:
    t1, t2, t3, t4 = angles
    posee, pos1, pos2, pos3, pos4 = forward_kinematics_4R(t1, t2, t3, t4, L1, L2, L3, L4, L5) # Function call

    # Axes labels, title, and limits
    ax.clear()
    ax.set_xlabel('X-Axi (mm)')
    ax.set_ylabel('Y-Axis (mm))')
    ax.set_zlabel('Z-Axis (mm)')
    ax.set_title('4R Forward Kinematics')
    ax.set_xlim([-200, 200])
    ax.set_ylim([-200, 200])
    ax.set_zlim([-10, 300])

<<<<<<< HEAD
    # Plot/Animate the arm's links
=======
    # Plot the arm
>>>>>>> 2aea854df712e15e05b2c5ed0f6089d1c6966e09
    ax.plot([0, pos1[0], pos2[0], pos3[0], pos4[0], posee[0]],
            [0, pos1[1], pos2[1], pos3[1], pos4[1], posee[1]],
            [0, pos1[2], pos2[2], pos3[2], pos4[2], posee[2]], 
             linestyle='-', marker='o', markersize=10,
             markerfacecolor='red', markeredgecolor='black',
             linewidth=6, markeredgewidth=1, color='black')

    # Plot the end effector
    plt.draw()  
    plt.pause(0.01)

plt.show()