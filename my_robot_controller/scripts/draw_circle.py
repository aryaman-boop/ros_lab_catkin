#!usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	rospy.init_node('draw_circle')
	rospy.loginfo("Draw Circle mode has neem started.")

	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

	rate = rospy.Rate(10)
	while not rospy.is_shutdown(): # do a infinite loop as long as a node is not shutdown
		msg = Twist()
		msg.linear.x = 2.0
		msg.angular.z = 1.
		pub.publish(msg)
		rate.sleep()
