#! /usr/bin/env python

import rospy
import message_filters
from sensor_msgs.msg import LaserScan

rospy.init_node("camera_test")

def callback(camera, back_camera):
    Front = front_sub
    Back = back_sub


front_sub = message_filters.Subscriber("/camera", LaserScan)
back_sub = message_filters.Subscriber("/back_camera", LaserScan)

# ats = message_filters.ApproximateTimeSynchronizer([front_sub, back_sub], queue_size=5, slop=0.01)
ats = message_filters.TimeSynchronizer([front_sub, back_sub], queue_size=5)

ats.registerCallback(callback)
rospy.spin()