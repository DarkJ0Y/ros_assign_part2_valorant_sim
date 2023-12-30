#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from valorant_simulation_sudipto.msg import WorkDone

class YoruFlashbang:
    def __init__(self):
        rospy.init_node('yoru_flashbang', anonymous=True)
        self.pub_check = rospy.Publisher('/check', String, queue_size=1)
        rospy.Subscriber('/work_done', WorkDone, self.work_done_callback)

    def work_done_callback(self, data):
        rospy.loginfo("WorkDone received: {}".format(data.message))

        check_msg = f"{data.message} {data.character_count}"
        self.pub_check.publish(check_msg)
        rospy.loginfo(check_msg)

if __name__ == '__main__':
    yoru = YoruFlashbang()
    rospy.spin()
