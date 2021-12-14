How to run the package

    • Install your package in the catkin_ws/src of your workspace
      
    • Make sure you have all the dependencies like python3, ros noetic and gazebo environment
      
    •  Run catkin_make clean && catkin_make in the catkin_ws folder followed by 
       source ~/catkin_ws/devel.setup.bash

    • To perform Teleop, run the following command in the catkin_ws

	roslaunch quad_robot template_launch.launch
      
 	This will launch the robot in gazebo environment

    • To visualize in rviz , after launching in gazebo on a new terminal type rviz and from drop down menu add the robot.

    • Now go to catkin_ws/src/quad_robot folder on the command prompt and run the following command
    • 
	chmod +x publisher.py

	This command gives our publisher required permissons to publish data
      
	rosrun quad_robot publisher.py 

    	This command publisher set velocity commands on joints of one leg of 	robot.
    • Package also contains other files like kinematics calculation, kinematics validation.
      
      
      
      	
