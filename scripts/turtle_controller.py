#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# Deklarasi publisher global
pub = None

def callback(data):
    """
    Callback untuk menangani perintah yang diterima dari topik /turtle_commands.
    """
    global pub  # Pastikan menggunakan publisher global
    rospy.loginfo(f"Received: {data.data}")

    twist = Twist()

    #Maju twist.linear.x = 2.0
    #Mundur twist.linear.x = -2.0
    #Kiri twist.angular.z = 2.0
    #Kanan twist.angular.z = -2.0
    # Menerjemahkan perintah menjadi gerakan
    if data.data == "maju":
        twist.linear.x = 2.0  
        twist.angular.z = 0.0
    elif data.data == "mundur":
        twist.linear.x = -2.0  
        twist.angular.z = 0.0
    elif data.data == "kiri":
        twist.linear.x = 0.0
        twist.angular.z = 2.0  
    elif data.data == "kanan":
        twist.linear.x = 0.0
        twist.angular.z = -2.0  
    else:
        rospy.logwarn(f"Unknown command: {data.data}")
        return

    # Publish gerakan ke /turtle1/cmd_vel
    if pub is not None:  # publisher sudah diinisialisasi
        pub.publish(twist)
        rospy.loginfo(f"Published Twist: linear.x={twist.linear.x}, angular.z={twist.angular.z}")
    else:
        rospy.logerr("Publisher 'pub' belum diinisialisasi!")

def listener():

    global pub  # Menggunakan variabel global untuk publisher

    rospy.init_node('turtle_controller', anonymous=True)
    #-
    # Inisialisasi publisher untuk /turtle1/cmd_vel
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Subscriber untuk topik /turtle_commands
    rospy.Subscriber('/turtle_commands', String, callback)
    rospy.loginfo("Turtle Controller is now listening for commands...")

    # Menjaga node tetap berjalan
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
