import rospy #(demonstrate autocompletion possibility)
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	rospy.init_node("test_node")

	rospy.loginfo("Test node has been started.")
	rate = rospy.Rate(10)

	while not rospy.is_shutdown(): # do a infinite loop as long as a node is not shutdown
	    rospy.loginfo("Hello")
	    rate.sleep()
