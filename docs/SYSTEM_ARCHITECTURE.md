
# LUMEN — System Architecture

## 1. Overview

LUMEN follows a modular ROS 2 architecture. Each subsystem is responsible for a specific robotics function and communicates with other subsystems through ROS 2 topics, services, actions and TF2 transforms.

The architecture will be implemented incrementally and validated at every stage.

## 2. High-Level Architecture

```text
                 LUMEN AUTONOMOUS ROBOT
                          |
          +---------------+---------------+
          |                               |
    GAZEBO HARMONIC                  ROBOT MODEL
          |                               |
    Simulated Sensors               URDF / XACRO
          |                               |
          +---------------+---------------+
                          |
                    ROS 2 JAZZY
                          |
          +---------------+---------------+
          |               |               |
      CONTROL         PERCEPTION       ROBOT STATE
          |               |               |
      Odometry        LiDAR / Camera     TF2
      Velocity        IMU Processing     Joint States
          |               |               |
          +---------------+---------------+
                          |
                MAPPING & LOCALIZATION
                          |
                 SLAM TOOLBOX / AMCL
                          |
                   NAV2 NAVIGATION
                          |
             Planning & Obstacle Avoidance
                          |
                 AUTONOMOUS ROBOT
```

## 3. Main Subsystems

### 3.1 Robot Description

Responsible for the robot's physical and visual model.

Planned components:
- Main chassis
- Differential-drive wheels
- Caster wheels
- LiDAR assembly
- RGB camera
- IMU
- Sensor mounting structures

Technologies:
- URDF
- Xacro
- robot_state_publisher

### 3.2 Simulation

Responsible for simulating the robot and its environment.

Technology:
- Gazebo Harmonic
- ros_gz
- ros_gz_bridge

### 3.3 Motion Control

Responsible for controlling the robot's linear and angular velocity.

Planned functionality:
- Differential-drive kinematics
- Wheel velocity control
- Odometry generation
- Command velocity handling

### 3.4 Sensor Processing

Responsible for acquiring and processing sensor data.

Planned sensors:
- 2D LiDAR
- RGB camera
- IMU
- Wheel encoders

### 3.5 Coordinate Frames

TF2 will manage coordinate transformations.

Planned frame structure:

```text
map
 └── odom
      └── base_link
           ├── base_footprint
           ├── laser_link
           ├── camera_link
           ├── imu_link
           ├── left_wheel_link
           └── right_wheel_link
```

The final frame tree will be adjusted according to the implemented robot model and navigation requirements.

### 3.6 Mapping and Localization

Mapping:
- SLAM Toolbox
- Occupancy grid generation
- Map saving and loading

Localization:
- AMCL
- Robot pose estimation
- Map-to-odometry transformation

### 3.7 Autonomous Navigation

Nav2 will provide:
- Global path planning
- Local trajectory control
- Obstacle avoidance
- Goal navigation
- Recovery behaviors
- Waypoint navigation

## 4. Development Sequence

1. Robot description
2. Gazebo integration
3. Motion control
4. Sensor integration
5. TF2 validation
6. RViz2 visualization
7. SLAM mapping
8. AMCL localization
9. Nav2 navigation
10. System integration and testing

## 5. Engineering Principle

Each subsystem must be tested independently before integration.

Topics, services, actions, frame names and configuration parameters will be documented as they are implemented and verified.
