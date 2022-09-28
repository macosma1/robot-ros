import os
import sys
import time

#os.system('ping 10.236.52.82')
os.system('source devel/setup.bash  &  roslaunch ddrl_ge turtlebot3_box.launch &')
time.sleep(3)
os.system('roslaunch pc2l start.launch &')
time.sleep(3)
#os.system('python detect.py --weights Detection/exp4/weights/best.pt')
os.system('source devel/setup.bash & roslaunch ddrl_ge turtlebot3_ddrl_ge.launch')
#os.system('python detect1.py --weights Detection/exp4/weights/best.pt > data.txt')
#os.system('ping 10.236.52.82 | tee data.txt')

