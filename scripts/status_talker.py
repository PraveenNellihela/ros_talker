#!usr/bin/env python3
import rospy
from std_msgs.msg import String


def status_talker():
    pub = rospy.Publisher('/status_talker/status', String, queue_size=10)
    rospy.init_node('status_talker', anonymous=True)
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        for current_status in range(5):
            if current_status == 2:
                status = "status:warning"
                rospy.logwarn(status)
            elif current_status == 4:
                status = "status:error"
                rospy.logerr(status)
            else:
                status = "status:ok"
                rospy.loginfo(status)
            pub.publish(status)
            rate.sleep()


if __name__ == '__main__':
    try:
        status_talker()
    except rospy.ROSInterruptException:
        pass
