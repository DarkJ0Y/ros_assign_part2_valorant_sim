#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Header
from valorant_simulation_sudipto.msg import WorkDone

class SageTheHealer:
    def __init__(self):
        rospy.init_node('sage_the_healer', anonymous=True)
        self.pub_work_done = rospy.Publisher('/work_done', WorkDone, queue_size=1)
        rospy.Subscriber('/riot_hq', String, self.command_callback)

    def command_callback(self, data):
        rospy.loginfo("Command received: {}".format(data.data))

        work_done_msg = WorkDone()
        work_done_msg.message = data.data
        work_done_msg.character_count = len(data.data.replace(" ", ""))

        self.pub_work_done.publish(work_done_msg)
        rospy.loginfo("The message is {} and the number of ch is {}".format(work_done_msg.message, work_done_msg.character_count))

if __name__ == '__main__':
    sage = SageTheHealer()
    rospy.spin()
