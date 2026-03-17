Mobile Robotics Lab - Week 2 Report

1. Lab Objectives

Utilized ROS 2 CLI tools (topics, services).

Operated and controlled the Turtlesim simulator.

Implemented multi-robot coordination using the rqt GUI.

2. Steps Followed

Environment Setup: Sourced /opt/ros/humble/setup.bash.

Simulation: Launched turtlesim_node and controlled it via turtle_teleop_key.

Service Calls: Used the /reset service to return the turtle to home position and the /spawn service to create turtle2.

Topic Interaction: Published velocity commands to /turtle2/cmd_vel to initiate circular motion independent of turtle1.

RQT Integration: Used RQT Service Caller and Message Publisher for graphical control.

3. Observations

Topics allow for continuous data streaming (velocity commands).

Services are better for one-time actions (spawning, resetting).

Each turtle exists in its own namespace, allowing for independent control via specific topics (e.g., /turtle1/cmd_vel vs /turtle2/cmd_vel).

Week 2 - Post-Lab Answers

1. What is the difference between a Topic and a Service?

Topic: Uses a publisher/subscriber model for continuous data streams. It is asynchronous (the sender doesn't wait for a response).

Service: Uses a request/response model for discrete actions. It is synchronous (the client waits for the server to finish the task).

2. What is the purpose of the /spawn service?

The /spawn service creates a new turtle instance within the existing turtlesim_node at a specific (x, y, theta) coordinate with a unique name.

3. How does rqt_graph help in debugging?

rqt_graph provides a visual representation of the ROS 2 ecosystem, showing exactly which nodes are talking to which topics. This helps identify if a node is publishing to the wrong topic or if a connection is missing.

4. What message type is used for turtle movement?

The geometry_msgs/msg/Twist message type is used, which contains linear and angular velocity vecto
