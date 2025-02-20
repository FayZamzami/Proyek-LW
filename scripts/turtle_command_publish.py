#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def publisher():
    """
    Node publisher untuk mengirimkan perintah pengguna ke topik /turtle_commands.
    """
    rospy.init_node('turtle_command_publisher', anonymous=True)
    pub = rospy.Publisher('/turtle_commands', String, queue_size=10)

    rospy.loginfo("Turtle Command Publisher is ready.")
    print("Masukkan salah satu perintah berikut: maju, mundur, kiri, kanan.")
    print("Tekan Ctrl+C untuk keluar.")

    while not rospy.is_shutdown():
        try:
            # Meminta input dari pengguna
            command = input("Masukkan perintah (maju, mundur, kiri, kanan): ").strip().lower()

            # Validasi input
            if command not in ["maju", "mundur", "kiri", "kanan"]:
                print("Perintah tidak valid. Masukkan salah satu: maju, mundur, kiri, kanan.")
                continue

            # Membuat dan memublikasikan pesan
            msg = String()
            msg.data = command
            pub.publish(msg)
            rospy.loginfo(f"Published command: {msg.data}")

        except KeyboardInterrupt:
            print("\nPublisher dihentikan.")
            break

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
