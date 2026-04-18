Week 4: ROS 2 Launch, Rosbag, and RQT Plot

Lab Overview

In this lab, I automated the startup of the Turtlesim environment using launch files, recorded manual control data using Rosbag, and analyzed the velocity profile using RQT Plot. This lab demonstrated how to manage multiple nodes and persist data for later analysis.

Tasks Completed

Launch System: I developed a Python-based launch file named my_launch.launch.py. This script starts the turtlesim_node and an xterm teleop window simultaneously. By using the prefix='xterm -e' argument, I ensured that the keyboard control interface opens in its own window, which keeps the main terminal clean and allows for easier multitasking.

Data Recording (Rosbag): I utilized the ros2 bag record command to capture traffic on the /turtle1/cmd_vel topic. I performed a 20-second manual navigation session using the arrow keys. This process created a localized database containing all the velocity commands sent during the session.

Playback and Verification: After recording, I stopped the node and used ros2 bag play to replay the saved data. I observed the turtlesim_node executing the exact same trajectory as my manual input. This confirms that Rosbag captures the message data accurately, regardless of the physical state of the robot at the time of playback.

Data Visualization (RQT): I utilized rqt_plot to monitor the /turtle1/cmd_vel/linear/x topic. By observing the live graph, I was able to see exactly when the "Up" arrow key was pressed, resulting in a spike in linear velocity, and when the key was released, causing the velocity to return to zero.

Observations

Workflow Optimization: Launch files are a significant upgrade from running individual nodes. They allow for complex configurations, such as starting multiple turtles or remapping topics, to be saved and reused reliably.

Data Reusability: Rosbag is an essential tool for debugging. By recording sensor or command data, a developer can test new control algorithms against the "recorded reality" of a previous run without having to manually drive the robot every time.

Granular Control Analysis: RQT Plot revealed that the turtle_teleop_key node sends discrete, fixed-velocity bursts. This is a "step input" in control theory, which explains why the turtle starts and stops abruptly rather than smoothly accelerating.

Conclusion

This lab successfully provided hands-on experience with the professional tools used to manage ROS 2 systems. The combination of Launch for deployment, Rosbag for data logging, and RQT for debugging forms the foundation of modern robotics development.
