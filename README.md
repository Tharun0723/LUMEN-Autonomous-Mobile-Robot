# LUMEN — Autonomous Mobile Robot

**Intelligent Navigation. Autonomous Movement. Real-World Robotics.**

LUMEN is an autonomous differential-drive mobile robot being developed using **ROS 2 Jazzy** and **Gazebo Harmonic**. The project focuses on building a custom mobile robot simulation with autonomous navigation, mapping, localization, sensor integration and intelligent obstacle avoidance.

The goal is to develop a complete robotics software system using industry-relevant tools and engineering practices.

## Project Objectives

- Design a custom differential-drive mobile robot using URDF and Xacro.
- Develop a realistic indoor simulation environment in Gazebo Harmonic.
- Implement robot motion control and odometry.
- Integrate LiDAR, RGB camera and IMU sensors.
- Visualize the robot and sensor data using RViz2.
- Build maps using SLAM Toolbox.
- Implement localization using AMCL.
- Configure autonomous navigation using Nav2.
- Develop obstacle avoidance and waypoint navigation.
- Validate the complete system through structured testing.

## Technology Stack

| Category | Technologies |
|---|---|
| Operating System | Ubuntu 24.04 |
| Robotics Middleware | ROS 2 Jazzy |
| Simulation | Gazebo Harmonic |
| Robot Description | URDF, Xacro |
| Visualization | RViz2 |
| Mapping | SLAM Toolbox |
| Localization | AMCL |
| Navigation | Nav2 |
| Programming | Python, C++ |
| Version Control | Git, GitHub |
| Development Environment | VS Code, WSL2 |

## Planned Robot Capabilities

- Differential-drive locomotion
- LiDAR-based environment perception
- Camera-based visual perception
- IMU-based motion sensing
- Odometry and TF2 transforms
- Autonomous mapping and localization
- Global and local path planning
- Dynamic obstacle avoidance
- Goal-based and waypoint navigation

*These are development objectives, not claims that all features are already implemented.*

## Repository Structure

```text
LUMEN-Autonomous-Mobile-Robot/
├── .github/
├── config/
├── docs/
├── maps/
├── media/
│   ├── images/
│   └── videos/
├── scripts/
├── src/
├── tests/
├── worlds/
├── .gitignore
└── README.md
```

## Development Roadmap

1. Development environment and repository setup
2. Robot mechanical design and URDF/Xacro
3. Gazebo simulation and indoor environment
4. Differential-drive control and odometry
5. Sensor integration
6. TF2 and RViz2 visualization
7. SLAM and map generation
8. AMCL localization
9. Nav2 autonomous navigation
10. Obstacle avoidance and waypoint missions
11. System integration and testing
12. Documentation and final demonstration

## Project Documentation

- [Project Overview](docs/PROJECT_OVERVIEW.md)
- [System Architecture](docs/SYSTEM_ARCHITECTURE.md)
- [Robot Design](docs/ROBOT_DESIGN.md)
- [Development Log](docs/DEVELOPMENT_LOG.md)
- [Testing](docs/TESTING.md)
- [Project State](docs/PROJECT_STATE.md)

## Project Status

**Current stage:** Repository and development environment setup.

Implementation progress will be documented as individual modules are developed and verified.

## License

License to be selected before public distribution.
