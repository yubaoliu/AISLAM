import math
import numpy as np
import matplotlib.pyplot as plt
pi = math.pi

# load laserscan and plot in scanner frame
scan = np.loadtxt('laserscan.dat')
angle = np.linspace(-pi/2, pi/2, np.shape(scan)[0], endpoint='true')
x = scan * np.cos(angle)
y = scan * np.sign(angle)
plt.figure()
plt.plot(x, y, '.k', markersize=3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Laser scan')
plt.gca().set_aspect('equal')
plt.savefig('scan1.pdf')

# transform to global frame
# Define the transformation matrix
T_global_robot = np.array(
    [[np.cos(pi / 4), -np.sin(pi / 4), 1],
     [np.sin(pi / 4), np.cos(pi / 4), 0.5],
     [0, 0, 1]])
T_robot_laser = np.array(
    [[np.cos(pi), -np.sin(pi), 0.2],
     [np.sin(pi), np.cos(pi), 0.0],
     [0, 0, 1]])

# Compute the laser frame w.r.t. the global frame
T_global_laser = np.dot(T_global_robot, T_robot_laser)

# Apply the transformation to the scan points
w = np.ones((1, np.shape(x)[0]))[0]

scan_laser = np.array([x, y, w])
scan_global = np.dot(T_global_laser, scan_laser)

# plot the laser points
plt.figure()
plt.plot(scan_global[0, :], scan_global[1, :], '.k', markersize=3)

# plot the  robot pose in blue
plt.plot(T_global_robot[0, 2], T_global_robot[1, 2], '+b')

# plot the laser pose in red
plt.plot(T_global_laser[0, 2], T_global_laser[1, 2], '+r')

plt.gca().set_aspect('equal')
plt.savefig('scan2.pdf')
plt.show()

