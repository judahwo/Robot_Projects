import numpy as np

a1 = 1 #a1 length
a2 = 1 #a2 length
a3 = 1 #a3 length
a4 = 1 #a4 length


T1 = 10 #Theta 1 in units of degrees
T2 = 70 #Theta 2 in units of degrees

T1 = (T1/180.0)*np.pi #Theta1 in radians
T2 = (T2/180.0)*np.pi #Theta2 in radians

R0_1 = [[np.cos(T1),-np.sin(T1),0],[np.sin(T1),np.cos(T1),0],[0,0,1]]
R1_2 = [[np.cos(T2),-np.sin(T2),0],[np.sin(T2),np.cos(T2),0],[0,0,1]]

R0_2 = np.dot(R0_1,R1_2)
print(R0_2)

D0_1 = [[a2*np.cos(T1)],[a2*np.sin(T1)],[a1]]
D1_2 = [[a4*np.cos(T2)],[a4*np.sin(T2)],[a3]]
print(np.matrix(D0_1))
print(np.matrix(D1_2))