#!/usr/bin/env python
import rospy
from robotnik_msgs.srv import *

# resetOdometry(x_position(m), y_position(m), z_position(m), orientation(rads))
def resetOdometry(x, y, z, w):
    try:
        rospy.loginfo("Restarting odometry ...")
        service = rospy.ServiceProxy("/robot/reset_odometry", set_odometry)
        response = service(x, y, z, w)
        rospy.loginfo("Odometry restarted")
    except rospy.ServiceException as e:
        rospy.logerr("Something has gone wrong: %s", e)

if __name__ == "__main__":
    # resetOdometry(x_position(m), y_position(m), z_position(), orientation(rads))
    resetOdometry(0,0,0,0)