#!/usr/bin/env python
import rospy
import sys
import time
import actionlib
from math import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from summit_xl_gps.srv import *

PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

def coordinate_converter(lat, lon, olat, olon):
    rospy.wait_for_service("coordinate_converter")
    try:
        service = rospy.ServiceProxy("coordinate_converter", gps_to_others)
        response = service(lat, lon, olat, olon)
        return response.xg, response.yg, response.xa, response.ya, response.utmx, response.utmy
    except rospy.ServiceException as e:
        print("La llamada al servicio fallo: %s", e)

def feedback_callback(feedback):
    rospy.loginfo(str(feedback))

def MoveBaseClient(x=0.0, y=0.0, theta=0.0, frame_id="map"):

    qx, qy, qz, qw = EulerToQuaternion(0,0,theta)

    rospy.init_node('move_base_gps_node')

    action_server_name = '/move_base/'
    client = actionlib.SimpleActionClient(action_server_name, MoveBaseAction)

    # waits until the action server is up and running
    rospy.loginfo('Waiting for action Server ' + action_server_name)
    client.wait_for_server()
    rospy.loginfo('Action Server Found...' + action_server_name)

    # creates a goal to send to the action server
    goal = MoveBaseGoal()

    goal.target_pose.header.frame_id = frame_id
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.x = qx
    goal.target_pose.pose.orientation.y = qy
    goal.target_pose.pose.orientation.z = qz
    goal.target_pose.pose.orientation.w = qw

    client.send_goal(goal, feedback_cb = feedback_callback)

    state_result = client.get_state()
    rate = rospy.Rate(1)

    rospy.loginfo("state_result: "+str(state_result))

    rospy.loginfo("Doing Stuff while waiting for the Server to give a result....")
    while not rospy.is_shutdown():
        state_result = client.get_state()
        rospy.loginfo("[Result] State: " + str(state_result))
        if (state_result == 3):
            rospy.loginfo("Punto alcanzado")
            break
        rate.sleep()


def EulerToQuaternion(roll, pitch, yaw):

    roll = radians(roll)
    pitch = radians(pitch)
    yaw = radians(yaw)

    qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
    qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
    qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
    qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)

    return qx, qy, qz, qw

if __name__ == "__main__":

    # Origin Point
    olat = 51.4978308
    olon = 6.5491412

    p1_lat = 51.4977194
    p1_lon = 6.5491159

    p2_lat = 51.4976913
    p2_lon = 6.5492859

    p3_lat = 51.49774
    p3_lon = 6.549315

    p4_lat = 51.4977617
    p4_lon = 6.5492369

    p5_lat = 51.4978292
    p5_lon = 6.5492459

 
    # Call coordinate_converter Server
    # xg,yg,xa,ya,utmx,utmy = coordinate_converter(target_latitude, target_longitude, origin_latitude, origin_longitude) 
    # MoveBaseClient(target_x, target_y, target_orientation_deg, robot_frame)
    for i in range(1):
        xg,yg,xa,ya,utmx,utmy = coordinate_converter(p1_lat, p1_lon, olat, olon)
        #print(xa,ya)
        MoveBaseClient(xg, yg, 0, "map")

        #xg,yg,xa,ya,utmx,utmy = coordinate_converter(p2_lat, p2_lon, olat, olon)
        #MoveBaseClient(xa, ya, 180, "map")

        #xg,yg,xa,ya,utmx,utmy = coordinate_converter(p3_lat, p3_lon, olat, olon)
        #MoveBaseClient(xa, ya, 270, "map")

        #xg,yg,xa,ya,utmx,utmy = coordinate_converter(p4_lat, p4_lon, olat, olon)
        #MoveBaseClient(xa, ya, 0, "map")

        #xg,yg,xa,ya,utmx,utmy #= coordinate_converter(p5_lat, p5_lon, olat, olon)
        #MoveBaseClient(xa, ya, 270, "map")

        #xg,yg,xa,ya,utmx,utmy = coordinate_converter(p5_lat, p5_lon, olat, olon)
        #MoveBaseClient(0, 0, 0, "map")
