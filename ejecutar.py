import os
import sys
import time


os.system('source devel/setup.bash  &  roslaunch ddrl_ge turtlebot3_box.launch &')
time.sleep(3)
os.system('source devel/setup.bash & roslaunch ddrl_ge turtlebot3_ddrl_ge.launch')
