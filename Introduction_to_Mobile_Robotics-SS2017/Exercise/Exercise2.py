import numpy as np
import matplotlib.pyplot as plt

# where x, y, and θ is the pose of the robot, vl and vr are the speed of the left and
# right wheel, t is the driving time, and l is the distance between the wheels of the robot
# OUTPUT: The output of the function is the new pose of the robot xn, yn, and θ
def my_diffdrive(x, y, theta, v_l, v_r, t, l):
    if not v_r == v_l:
        v = (v_l + v_r)/2.
        w = (v_r - v_l)/l
        delta_theta = w * t
        R = 1./2. * (v_l + v_r)/(v_r - v_l)

        ICC = np.array([x - R * np.sin(theta), y + R * np.cos(theta)])

        RT = np.array([[float(np.cos(delta_theta)), -float(np.sin(delta_theta)), 0.],
                  [float(np.sin(delta_theta)), float(np.cos(delta_theta)), 0.],
                  [0.,   0.,  1.]])
        res = np.dot(RT, np.array([x-ICC[0], y-ICC[1], theta]).T) + np.array([ICC[0], ICC[1], delta_theta]).T
        x_n = res[0]
        y_n = res[1]
        theta_n = res[2]
    else:
        x_n = x + v_l * t * np.cos(theta)
        y_n = y + v_l * t * np.sin(theta)
        theta_n = theta
    return x_n, y_n, theta_n


def diffdrive(x, y, theta, v_l, v_r, t, l):
    # straight line
    if v_l == v_r:
        theta_n = theta
        x_n = x + v_l * t * np.cos(theta)
        y_n = y + v_l * t * np.sin(theta)
    # circular motion
    else:
        # calculate the radius
        R = 1/2.0 * ((v_l + v_r)/(v_r - v_l))

        # computing center of curvature
        ICC_x = x - R * np.sin(theta)
        ICC_y = y + R * np.cos(theta)

        # compute the angular velocity
        omega = (v_r - v_l)/l

        # computing angle change
        dtheta = omega * t

        # forward kinematics for differential drive
        x_n = np.cos(dtheta) * (x-ICC_x) - np.sin(dtheta) * (y - ICC_y) + ICC_x
        y_n = np.sin(dtheta) * (x-ICC_x) + np.cos(dtheta) * (y-ICC_y) + ICC_y
        theta_n = theta + dtheta
    return x_n, y_n, theta_n


plt.gca().set_aspect('equal')
# set the distance between the wheels and the initial robot position
l = 0.5
x, y, theta =1.5, 2.0, (np.pi)/2.0

# plot the starting position
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print("starting pose: x: %f, y: %f, theta: %f" % (x, y, theta))

# first motion
v_l = 0.3
v_r = 0.3
t = 3
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print("after motion 1: x: %f, y: %f, theta: %f" % (x, y, theta))

# second motion
v_l = 0.1
v_r = -0.1
t = 1
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print("after motion 2: x: %f, y: %f, theta: %f" % (x, y, theta))

# third motion
v_l = 0.2
v_r = 0.0
t = 2
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print("after motion 3: x: %f, y: %f, theta: %f" % (x, y, theta))


plt.xlim([0.5, 2.5])
plt.ylim([1.5, 3.5])

plt.savefig("pose.png")
plt.show()