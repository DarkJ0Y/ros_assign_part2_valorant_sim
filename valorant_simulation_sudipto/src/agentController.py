#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from valorant_simulation_sudipto.msg import WorkDone

class AgentController:
    def __init__(self, your_name):
        self.your_name = your_name
        rospy.init_node('agent_controller', anonymous=True)
        self.pub_riot_hq = rospy.Publisher('/riot_hq', String, queue_size=1)

    def send_hello_message(self):
        rate = rospy.Rate(0.2)  # Send every 5 seconds (0.2 Hz)
        while not rospy.is_shutdown():
            rospy.loginfo("Data is publishing....")
            self.pub_riot_hq.publish(f"Hello {self.your_name}")
            rate.sleep()

if __name__ == '__main__':
    your_name = "Sudipto"  # Replace with your actual name
    agent = AgentController(your_name)
    agent.send_hello_message()
