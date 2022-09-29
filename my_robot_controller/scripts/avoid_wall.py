#!usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def pose_callback(msg):
    if msg.x>2 or msg.x <9 or msg.y>2 or msg.y<9:
        msg.linear.x = 2.0
    else:
        msg.linear.x = 2.0
        msg.angular.z = 1.
        
def leniar_vel():
    msg = Twist()
	msg.linear.x = 2.0
	msg.angular.z = 0.
	pub.publish(msg)

def pose_sub():
    rospy.init_node('turtle_pose_subscriber')
    rospy.loginfo("Subscription started.")
    sub = rospy.Subscriber('/turtle1/pose', Pose, callback = pose_callback)
    rospy.spin()
    rate = rospy.Rate(2)


if __name__ == '__main__':
	rospy.init_node('draw_circle')
	rospy.loginfo("Draw Circle mode has neem started.")

	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

	rate = rospy.Rate(10)
	while not rospy.is_shutdown(): # do a infinite loop as long as a node is not shutdown
        leniar_vel()
		rate.sleep()
        pose_sub()
        

def wall_rebound():

