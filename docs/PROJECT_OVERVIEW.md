# LUMEN — Project Overview

## 1. Introduction

LUMEN is an autonomous differential-drive mobile robot developed using ROS 2 Jazzy and Gazebo Harmonic.

The project aims to develop a complete autonomous mobile robotics system capable of understanding its environment, creating maps, estimating its position and navigating through indoor environments.

Development will focus on modular robot design, simulation, perception, localization, planning and autonomous navigation.

## 2. Problem Statement

Indoor mobile robots must navigate environments containing walls, corridors, obstacles and restricted areas.

To accomplish this reliably, a robot requires:
- Accurate motion control
- Environment perception
- Localization
- Mapping
- Path planning
- Obstacle avoidance

LUMEN will integrate these capabilities into one ROS 2-based autonomous robotics platform.

## 3. Project Objectives

1. Design a custom differential-drive robot.
2. Develop its mechanical description using URDF and Xacro.
3. Build an indoor simulation environment.
4. Integrate LiDAR, RGB camera and IMU sensors.
5. Implement robot control and odometry.
6. Develop mapping using SLAM Toolbox.
7. Implement localization using AMCL.
8. Configure autonomous navigation using Nav2.
9. Test obstacle avoidance and waypoint navigation.
10. Document and validate the complete system.

## 4. Development Environment

| Component | Selected Technology |
|---|---|
| OS | Ubuntu 24.04 |
| Middleware | ROS 2 Jazzy |
| Simulator | Gazebo Harmonic |
| Visualization | RViz2 |
| Robot description | URDF / Xacro |
| Mapping | SLAM Toolbox |
| Localization | AMCL |
| Navigation | Nav2 |
| Programming | Python / C++ |
| Version control | Git / GitHub |
| Editor | VS Code |

## 5. Expected Capabilities

- Differential-drive movement
- Sensor data acquisition
- Robot state visualization
- Odometry and coordinate transforms
- Indoor mapping
- Map saving and loading
- Autonomous localization
- Global and local path planning
- Obstacle avoidance
- Goal-based navigation
- Waypoint missions

These capabilities are planned and will be marked complete only after testing.

## 6. Development Philosophy

LUMEN will be developed incrementally.

Every major subsystem will be:
- Designed before implementation
- Developed as a modular component
- Tested independently
- Integrated with other subsystems
- Documented with verified results

## 7. Current Development Stage

Repository foundation and development environment setup.