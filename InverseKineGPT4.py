import numpy as np


def inverse_kinematics_3r_3d(x, y, z, L1, L2, L3):
    # Calculate the distance from the target position to the base
    r = np.sqrt(x ** 2 + y ** 2)

    # Calculate the height of the target position from the first joint
    h = z - L1

    # Calculate the distance from the first joint to the target position in the plane formed by the second and third links
    D = np.sqrt(r ** 2 + h ** 2)

    # Calculate joint angles using the geometric approach
    theta1 = np.arctan2(y, x)
    theta2 = np.arccos((L2 ** 2 + D ** 2 - L3 ** 2) / (2 * L2 * D)) + np.arctan2(h, r)
    theta3 = np.arccos((L2 ** 2 + L3 ** 2 - D ** 2) / (2 * L2 * L3))

    # Convert joint angles from radians to degrees
    theta1_deg = np.rad2deg(theta1)
    theta2_deg = np.rad2deg(theta2)
    theta3_deg = np.rad2deg(theta3)

    return theta1_deg, theta2_deg, theta3_deg


# Example usage
L1, L2, L3 = 10, 10, 10
x, y, z = 15, 0, 15
theta1_deg, theta2_deg, theta3_deg = inverse_kinematics_3r_3d(x, y, z, L1, L2, L3)

print("Theta1 (deg):", theta1_deg)
print("Theta2 (deg):", theta2_deg)
print("Theta3 (deg):", theta3_deg)
