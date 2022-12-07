#!/usr/bin/env python3

""" 
A sample ROS node with a simple Publisher.
"""

import rospy

from sample_python_module.sample_class import SampleClass
from sample_python_module.sample_class import add_two_things
from sample_python_module.python_sub_module.sub_class import SubClass

from std_msgs.msg import Float32

if __name__ == "__main__":
    node_name = "sample_ros_node"
    rospy.init_node(node_name)
    rospy.loginfo("Initializing ros node %s", node_name)

    sample_pub = rospy.Publisher("sample_topic", Float32, queue_size=5)
    spm = SampleClass("John Doe")

    spm.welcome_print()

    sample_pub.publish(add_two_things(2, 10))

    sc = SubClass("December")
    sc.print_month()
