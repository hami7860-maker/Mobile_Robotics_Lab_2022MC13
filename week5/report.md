Lab 5 Execution Summary: TurtleBot3 Simulation and SLAM Navigation

1\. Lab Objective  
The primary objective of this laboratory exercise was to deploy a simulated TurtleBot3 environment using ROS 2 (Humble), Gazebo, and RViz. The session focused on executing a Simultaneous Localization and Mapping (SLAM) algorithm to generate a reliable floor plan, followed by the development of custom Python nodes for programmatic velocity control and odometry data extraction.

2\. Simulation Environment and SLAM Execution (Tasks 1-7)

	Initialization: The TURTLEBOT3\_MODEL environment variable was set to burger to load the appropriate URDF and sensor plugins. The simulation was initiated using turtlebot3\_gazebo, spawning the robot in an enclosed test arena.

	Mapping Setup: Cartographer was launched alongside RViz (use\_sim\_time:=true) to process real-time LiDAR scans and visualize TF frames, odometry, and the active map generation.

	Operational Challenges & Mapping: During manual teleoperation, system resource constraints (low Real Time Factor in Gazebo) introduced significant control latency. To prevent odometry drift and overlapping walls in the SLAM output, navigation was adapted to use isolated, single-axis movements (stop-and-go driving).

	Map Extraction: Once the hexagonal perimeter was fully closed and the inner obstacles were mapped, the environmental data was successfully serialized and saved to the local directory utilizing the map\_saver\_cli utility from the nav2\_map\_server package.

3\. Custom ROS 2 Architecture (Tasks 8 & 9\)  
To fulfill the programming requirements and avoid dependency conflicts, a new ament\_python package was compiled.

	Task 8: Open-Loop Velocity Controller  
	A publisher node (alternating\_pub.py) was engineered to bypass manual teleoperation. Utilizing a 2.0-second timer callback, the node alternates a boolean state to publish specific geometry\_msgs/msg/Twist commands to the /cmd\_vel topic. This successfully forced the robot into an automated loop of driving forward at 0.1 m/s and stopping.

	Task 9: Telemetry Subscriber  
	A subscriber node (odom\_sub.py) was developed to passively monitor the robot's state. It was configured to listen to the /odom topic. To filter out unnecessary covariance matrices and angular data, the callback function systematically extracted and logged only the active position.x and position.y coordinate floats from the incoming nav\_msgs/msg/Odometry messages.

**Deliverable 5: Observations on Discrepancies Between Expected and Simulated Motion**

During the execution of this lab, several significant discrepancies were observed between the expected kinematic behavior of the TurtleBot3 and its actual performance within the Gazebo simulation:

* **Command Latency and Input Queuing:** \* *Expected:* The robot should exhibit a 1:1 real-time response to keyboard teleoperation inputs.  
  * *Simulated:* Due to the heavy computational load of running a 3D physics engine and Cartographer simultaneously on a Virtual Machine, Gazebo's Real Time Factor (RTF) dropped to approximately 0.22. This caused severe command latency. Keystrokes were delayed and queued, causing the robot to unexpectedly accelerate to maximum velocity or over-rotate long after the input was given.  
* **Odometry Drift and Map Smearing:** \* *Expected:* The SLAM algorithm should instantly draw perfectly straight walls and sharp corners as the robot moves.  
  * *Simulated:* Because the simulation lag caused jerky, stuttering movements, the robot's internal odometry (wheel encoders) momentarily drifted from its true spatial position. This caused slight "smearing" or double-lines in the RViz map during manual teleoperation.  
* **Open-Loop vs. Closed-Loop Stability:** \* *Expected:* Manual control should be the easiest way to navigate a room.  
  * *Simulated:* Manual control proved highly unstable under high system load. Conversely, when the custom publisher (Task 8\) injected a constant, programmatic velocity directly into the `/cmd_vel` topic, the simulated motion became perfectly smooth, allowing Cartographer to easily close the loop and generate a sharp map.

4\. Final Conclusion  
This lab demonstrated the functional pipeline between hardware simulation and spatial mapping. The challenges faced during manual control highlighted the necessity of programmatic motor control when operating under network or computational latency. By successfully writing and executing the publisher and subscriber nodes, the fundamental ROS 2 concepts of message passing and automated kinodynamic control were validated.  
