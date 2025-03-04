```shell
ros2 run fishbot_application nav_to_pose
colcon build --packages-up-to fishbot_application
ros2 launch fishbot_description gazebo.launch.py
ros2 launch fishbot_cartographer cartographer.launch.py
ros2 launch fishbot_navigation2 navigation2.launch.py
```