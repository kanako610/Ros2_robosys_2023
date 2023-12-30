#!/usr/bin/python3
# SPDX-FileCopyrightText: © 2023 Kanako Takahashi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import sys
print(sys.version)
def cb(msg):
    global node
    node.get_logger().info("Listen: %s" % msg.data)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb, 10)

rclpy.spin(node)
