# CMake generated Testfile for 
# Source directory: /home/macosma1/catkin_ws/src/send/realsense2_description
# Build directory: /home/macosma1/catkin_ws/build/realsense2_description
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_realsense2_description_nosetests_tests "/home/macosma1/catkin_ws/build/realsense2_description/catkin_generated/env_cached.sh" "/home/macosma1/anaconda3/envs/robot/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/macosma1/catkin_ws/build/realsense2_description/test_results/realsense2_description/nosetests-tests.xml" "--return-code" "\"/usr/bin/cmake\" -E make_directory /home/macosma1/catkin_ws/build/realsense2_description/test_results/realsense2_description" "/usr/bin/nosetests-2.7 -P --process-timeout=60 --where=/home/macosma1/catkin_ws/src/send/realsense2_description/tests --with-xunit --xunit-file=/home/macosma1/catkin_ws/build/realsense2_description/test_results/realsense2_description/nosetests-tests.xml")
subdirs("gtest")
