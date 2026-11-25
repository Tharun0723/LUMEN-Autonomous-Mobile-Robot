
# LUMEN — Robot Mechanical Design

## 1. Design Overview

LUMEN will use a custom differential-drive mobile robot platform designed for indoor autonomous navigation.

The design will prioritize:
- Stable movement
- Realistic physical properties
- Modular construction
- Practical sensor placement
- Accurate collision geometry
- Compatibility with ROS 2 and Gazebo Harmonic

## 2. Mechanical Configuration

### Chassis
The main chassis will support the robot's electronics, sensors and mechanical assemblies.

### Drive System
The robot will use:
- Two independently driven wheels
- Left and right wheel assemblies
- Caster support for balance

The differential-drive configuration enables forward movement, reverse movement and rotation.

### Sensor Assembly

Planned sensor configuration:

| Sensor | Purpose |
|---|---|
| 2D LiDAR | Distance measurement and mapping |
| RGB Camera | Visual perception |
| IMU | Orientation and acceleration |
| Wheel Encoders | Wheel rotation measurement |

## 3. Robot Description

The robot model will be developed using modular URDF/Xacro files.

Planned model components:
- Chassis links
- Wheel links
- Caster links
- Sensor links
- Joint definitions
- Visual geometry
- Collision geometry
- Inertial properties
- Materials

## 4. Preliminary Design Decisions

| Parameter | Current Decision |
|---|---|
| Robot type | Indoor mobile robot |
| Drive configuration | Differential drive |
| Powered wheels | Two |
| Support wheels | Caster configuration |
| Description format | URDF / Xacro |
| Simulation | Gazebo Harmonic |
| Sensor arrangement | Modular |

Exact dimensions, wheel separation, wheel radius, mass and inertial properties are not finalized.

## 5. Physics and Simulation Requirements

The robot model must include:
- Appropriate mass distribution
- Realistic inertia tensors
- Collision geometry
- Wheel friction parameters
- Correct joint axes
- Stable contact with the ground

Visual geometry and collision geometry should be designed separately where necessary.

## 6. Design Validation

The mechanical design will be validated through:

1. URDF/Xacro parsing
2. Robot link and joint inspection
3. Inertial property verification
4. Gazebo model spawning
5. Wheel rotation testing
6. Ground contact testing
7. Stability and movement testing
8. Sensor placement verification

## 7. Future Improvements

Potential improvements include:
- Modular sensor mounts
- Detailed industrial-style exterior
- Protective sensor housings
- Custom visual materials
- Optimized chassis geometry

All decorative components must preserve realistic collision and physical behavior.
