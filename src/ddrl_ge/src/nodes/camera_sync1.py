#! /usr/bin/env python

import rospy
import message_filters
import numpy as np
from sensor_msgs.msg import LaserScan

rospy.init_node("camera_sync1")

def callback(camera, laser):
    scan = camera
    laser = laser
    val_max = 0
    sum_data = 0
    promedio = 0
    scan_max = 1
    scan_data_pre = []
    scan_data = 48*[0]
    
    #print(scan.header)
    for i in range(len(scan.ranges)*2):
        if i < 12:
            if scan.ranges[i] == float("Inf"):
                scan_data_pre.append(3.5)
                val_max = 3.5
            elif np.isnan(scan.ranges[i]):
                scan_data_pre.append(0)
                val_max = 0
            else:
                scan_data_pre.append(scan.ranges[i])
                val_max = scan.ranges[i]
            
            sum_data = sum_data + val_max
            if scan.ranges[i] > scan_max:
                if scan.ranges[i] <= 2:
                    scan_max = scan.ranges[i]
                else:
                    pass
            else: 
                pass

        if i == 12:
            promedio = sum_data/12
            if scan_max == 1:           #son todos o mayores de 2 o menor de 1, pillamos el promedio entonces
                scan_max = promedio
        
        if i >= 12:
            scan_data_pre.append(scan_max)

    scan_data[0:6] = scan_data_pre[6:12]
    scan_data[6:18] = scan_data_pre[12:24]
    scan_data[18:24] = scan_data_pre[0:6]
    
    for i in range(len(laser.ranges)):
        if laser.ranges[i] == float("Inf"):
            scan_data_pre.append(3.5)
        elif np.isnan(laser.ranges[i]):
            scan_data_pre.append(0)
        else:
            scan_data_pre.append(laser.ranges[i])
    
    scan_data[24:48] = scan_data_pre[24:48]

    if np.any(np.isnan(np.array(scan_data))):
        scan_data = d 
        raise Exception("it's nan sensor")

    pub.publish(ranges = scan_data)
    #return scan_data


camera = message_filters.Subscriber("camera", LaserScan)
laser = message_filters.Subscriber("scan", LaserScan)
print("camera_sync1")
pub = rospy.Publisher('camera_sync1', LaserScan, queue_size=1)

ats = message_filters.ApproximateTimeSynchronizer([camera, laser], queue_size=2, slop=0.15)
#ats = message_filters.TimeSynchronizer([front_sub, laser], queue_size=1)
ats.registerCallback(callback)

rospy.spin()


