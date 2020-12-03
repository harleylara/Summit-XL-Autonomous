#!/usr/bin/env python
import rospy
from std_srvs.srv import *

def calibrateIMU():
    try:
        rospy.loginfo("Calibrating IMU ...")
        service_acc = rospy.ServiceProxy("/robot/calibrate_imu_acc", Trigger)
        service_gyro = rospy.ServiceProxy("/robot/calibrate_imu_gyro", Trigger)
        service_mag = rospy.ServiceProxy("/robot/calibrate_imu_mag", Trigger)
        response_acc = service_acc()
        response_gyro = service_gyro()
        response_mag = service_mag()
        print(response_acc)
        print(response_gyro)
        print(response_mag)
    except rospy.ServiceException as e:
        rospy.logerr("Something has gone wrong: %s", e)

if __name__ == "__main__":
    calibrateIMU()