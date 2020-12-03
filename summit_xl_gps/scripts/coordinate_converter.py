#!/usr/bin/env python
import rospy
from summit_xl_gps.srv import gps_to_others, gps_to_othersResponse
import geonav_transform.geonav_conversions as gc
reload(gc)
import alvinxy.alvinxy as axy
reload(axy)

def handle(request):
    xg, yg = gc.ll2xy(request.lat,request.lon,request.olat,request.olon)
    utmy, utmx, utmzone = gc.LLtoUTM(request.lat,request.lon)
    xa,ya = axy.ll2xy(request.lat,request.lon,request.olat,request.olon)

    return gps_to_othersResponse(xg, yg, xa, ya, utmx, utmy)

def server():
    rospy.init_node("coordinate_converter", anonymous = False)
    service = rospy.Service("coordinate_converter", gps_to_others, handle)
    rospy.loginfo("COORDINATE CONVERTER Server started...")
    rospy.spin()

if __name__ == "__main__":
    server()