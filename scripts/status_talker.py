#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def status_talker():
    pub = rospy.Publisher('status', String, queue_size=10)
    rospy.init_node('status_talker', anonymous=True)
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        for msg in range(5):
            if msg == 2:
                publish_msg = "status:warning"
            elif msg == 4:
                publish_msg = "status:error"
            else:
                publish_msg = "status:ok"
            rospy.loginfo(publish_msg)
            pub.publish(publish_msg)
            rate.sleep()


if __name__ == '__main__':
    try:
        status_talker()
    except rospy.ROSInterruptException:
        pass
