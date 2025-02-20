#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback(data):
    rospy.loginfo(f"Received: {data.data}")
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    twist = Twist()

    #Maju twist.linear.x = 2.0
    #Mundur twist.linear.x = -2.0
    #Kiri twist.angular.z = 2.0
    #Kanan twist.angular.z = -2.0

    if data.data.lower() == "maju":
        twist.linear.x = 2.0  
        twist.angular.z = 0.0
    elif data.data.lower() == "mundur":
        twist.linear.x = -2.0  
        twist.angular.z = 0.0
    elif data.data.lower() == "kiri":
        twist.linear.x = 0.0
        twist.angular.z = 2.0  
    elif data.data.lower() == "kanan":
        twist.linear.x = 0.0
        twist.angular.z = -2.0  
    else:
        rospy.logwarn(f"Unknown command: {data.data}")
        return

    pub.publish(twist)
    rospy.loginfo(f"Published Twist: linear.x={twist.linear.x}, angular.z={twist.angular.z}")

def listener():
    # Menggunakan topik  "/turtle_commands"

    rospy.init_node('turtle_controller', anonymous=True)
    rospy.Subscriber('/turtle_commands', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
