#! /usr/bin/env python
from ik import ik
import rospy
from std_msgs.msg import Float64
import numpy as np


# coordinates = input("Enter the coordinates: ")
theta = np.array([[0,0.8,0,5,0.8,0,0]])

rospy.init_node('publisher')

pub_1 = rospy.Publisher('/quad_robot/rr_h_controller/command',Float64, queue_size=10)
pub_2 = rospy.Publisher('/quad_robot/rr_l_1_controller/command',Float64, queue_size=10)
pub_3 = rospy.Publisher('/quad_robot/rr_lg_controller/command',Float64, queue_size=10)
pub_4 = rospy.Publisher('/quad_robot/rr_l_2_controller/command',Float64, queue_size=10)
pub_5 = rospy.Publisher('/quad_robot/rr_a_controller/command',Float64, queue_size=10)
pub_6 = rospy.Publisher('/quad_robot/rr_f_controller/command',Float64, queue_size=10)

rate = rospy.Rate(5)

while not rospy.is_shutdown():
    
    pub_1.publish(theta[0])
    pub_2.publish(theta[1])
    pub_3.publish(theta[2])
    pub_4.publish(theta[3])
    pub_5.publish(theta[4])
    pub_6.publish(theta[5])
    rospy.loginfo('Giving angle command to rear right leg') 
    rate.sleep()  
     
    
    
    
