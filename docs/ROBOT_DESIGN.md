
# LUMEN — Robot Mechanical Design

**Design Revision:** 0.2  
**Status:** Preliminary engineering specification  
**Drive Configuration:** Four-wheel skid-steer  
**Simulation:** Gazebo Harmonic

## 1. Design Overview

LUMEN is a futuristic industrial autonomous mobile robot designed for indoor navigation, mapping, localization and perception.

The robot uses four independently actuated rubber wheels arranged in a skid-steer configuration.

The mechanical design prioritizes:
- Stable indoor locomotion
- Realistic simulation physics
- Modular mechanical assemblies
- Accurate sensor positioning
- Maintainable URDF/Xacro architecture
- Compatibility with ROS 2 Jazzy and Gazebo Harmonic

## 2. Drive Configuration

- Four powered rubber wheels
- Two wheels on the left side
- Two wheels on the right side
- Independent revolute joint for each wheel
- Left and right wheels controlled as logical drive groups
- No caster wheels

The robot turns through differential wheel velocities and controlled wheel-ground slip.

## 3. Preliminary Chassis Specifications

| Parameter | Value |
|---|---:|
| Chassis length | 500 mm |
| Chassis width | 320 mm |
| Chassis height | 140 mm |
| Wheel diameter | 160 mm |
| Wheel radius | 80 mm |
| Wheel width | 45 mm |
| Wheelbase | 340 mm |
| Track width | 380 mm |
| Ground clearance | 45 mm |
| Overall wheel width | 425 mm |
| Target total mass | 25 kg |

These dimensions are preliminary and subject to simulation validation.

## 4. Coordinate Convention

The robot uses the standard ROS coordinate convention:

- X: Forward
- Y: Left
- Z: Upward

The chassis geometric centre is the reference origin for the mechanical layout.

The planned wheel positions are:

| Wheel | X | Y | Z |
|---|---:|---:|---:|
| Front left | +170 mm | +190 mm | 80 mm |
| Rear left | -170 mm | +190 mm | 80 mm |
| Front right | +170 mm | -190 mm | 80 mm |
| Rear right | -170 mm | -190 mm | 80 mm |

Wheel axle direction: Y-axis.

## 5. Wheel Clearance

Chassis half-width:

160 mm

Wheel centre lateral offset:

190 mm

Wheel half-width:

22.5 mm

Inner wheel edge:

190 - 22.5 = 167.5 mm

Nominal clearance:

167.5 - 160 = 7.5 mm

Protective panels and mounting brackets must preserve this clearance.

## 6. Vertical Geometry

Reference ground plane: Z = 0.

| Component | Height above ground |
|---|---:|
| Wheel centre | 80 mm |
| Chassis bottom | 45 mm |
| Chassis centre | 115 mm |
| Chassis top | 185 mm |
| LiDAR centre | 300 mm |
| RGB-D camera centre | 420 mm |

The `base_link` frame is initially positioned at the chassis geometric centre.

Sensor offsets relative to `base_link`:

- LiDAR: +185 mm in Z.
- RGB-D camera: +305 mm in Z.
- Wheel centres: -35 mm in Z.

The camera's final X position and mounting angle remain to be determined.

## 7. Sensor Configuration

### 2D LiDAR

Purpose:
- Distance measurement
- Obstacle detection
- SLAM mapping
- Navigation costmaps

Proposed mounting height: 300 mm.

Frame: `laser_link`.

### RGB-D Camera

Purpose:
- RGB image acquisition
- Depth perception
- Object detection
- Visual inspection

Proposed mounting height: 420 mm.

Frame: `camera_link`.

An optical frame will be provided for camera data.

### IMU

Purpose:
- Angular velocity measurement
- Linear acceleration measurement
- Orientation estimation

The IMU will be mounted close to the chassis centre of gravity.

Frame: `imu_link`.

### Wheel Encoders

Wheel rotation measurements will be obtained from the four wheel joints.

## 8. Skid-Steer Kinematics

Let:

- vL = average left-side wheel linear velocity.
- vR = average right-side wheel linear velocity.
- B = effective track width.
- v = robot linear velocity.
- omega = robot angular velocity.

Ideal kinematic equations:

v = (vR + vL) / 2

omega = (vR - vL) / B

Initial geometric track width:

B = 0.38 m

Real skid-steer motion includes lateral slip. The effective track width will be calibrated through simulation testing.

## 9. Wheel Speed Calculations

Wheel radius:

r = 0.08 m

Wheel circumference:

C = 2*pi*r = 0.50265 m

At a linear velocity of 0.5 m/s:

Wheel angular velocity:

omega_w = v/r = 6.25 rad/s

Wheel rotational speed:

RPM = approximately 59.7

For the initial simulation configuration, the proposed maximum wheel angular speed limit is 9 rad/s.

This is a simulation parameter, not a physical motor selection.

## 10. Preliminary Mass Budget

| Assembly | Estimated mass |
|---|---:|
| Chassis and structure | 10 kg |
| Four wheel assemblies | 4 kg |
| Drive assemblies | 4 kg |
| Battery and electronics | 4 kg |
| Sensors | 1 kg |
| Upper panels and accessories | 2 kg |
| Total | 25 kg |

These values are design estimates.

### Centre of Gravity Estimate

Assumed component centre heights:

| Assembly | Mass | Centre height |
|---|---:|---:|
| Chassis | 10 kg | 115 mm |
| Wheels | 4 kg | 80 mm |
| Drive assemblies | 4 kg | 95 mm |
| Battery and electronics | 4 kg | 80 mm |
| Sensors | 1 kg | 350 mm |
| Upper panels | 2 kg | 185 mm |

Using:

Z_CG = sum(mass * height) / total mass

Estimated vertical centre of gravity:

Z_CG = 115.6 mm

Target centre of gravity: approximately 110–150 mm above ground.

The actual value must be recalculated after component geometry and mass properties are finalized.

## 11. Chassis Inertia Estimate

The chassis is initially approximated as a uniform rectangular box.

Mass: 10 kg

Length: 0.5 m

Width: 0.32 m

Height: 0.14 m

Calculated inertia:

| Component | Value |
|---|---:|
| Ixx | 0.10167 kg m^2 |
| Iyy | 0.22467 kg m^2 |
| Izz | 0.29367 kg m^2 |

These values apply only to the idealized chassis body.

The complete robot inertia must include the wheels, motors, battery, sensor mast and other assemblies.

## 12. Mechanical Assembly Breakdown

Planned assemblies:

1. Main chassis base
2. Upper protective chassis cover
3. Front left wheel module
4. Rear left wheel module
5. Front right wheel module
6. Rear right wheel module
7. Four motor mounting assemblies
8. LiDAR mounting mast
9. RGB-D camera bracket
10. IMU mounting structure
11. Decorative protective panels

## 13. Gazebo Physics Requirements

Each physical component must have:

- Visual geometry
- Collision geometry
- Mass
- Inertial properties
- Correct joint configuration

Additional simulation requirements:

- Wheel-ground contact
- Appropriate friction parameters
- Stable contact behaviour
- Realistic wheel rotation
- Collision clearance
- Skid-steer turning validation

## 14. Validation Plan

Before considering the mechanical design complete:

1. Validate chassis geometry.
2. Verify wheel positions.
3. Verify wheel rotation axes.
4. Check wheel-ground contact.
5. Test forward and reverse motion.
6. Test rotation in place.
7. Verify sensor mounting positions.
8. Inspect mass and inertia properties.
9. Validate robot stability in Gazebo.
10. Calibrate effective skid-steer track width.

## 15. Unresolved Design Decisions

- Exact wheel hub and motor geometry.
- Motor mounting dimensions.
- Final camera X position and pitch.
- LiDAR model and scan parameters.
- IMU model and noise parameters.
- Detailed upper cover geometry.
- Component-level inertial properties.
- Wheel friction calibration.

## 16. Current Design Status

Revision 0.2 is a preliminary mechanical engineering specification.

The robot has not yet been implemented as a URDF/Xacro model.

Mechanical geometry and physical parameters must be validated through Gazebo simulation before being considered finalized.

## 17. Detailed Chassis Engineering — Revision 0.3

### 17.1 Overall Chassis Envelope

| Parameter | Value |
|---|---:|
| Length | 500 mm |
| Width | 320 mm |
| Height | 140 mm |
| Ground clearance | 45 mm |
| Reference frame | base_link |

The chassis is centred at the base_link origin.

Its coordinate extents are:

- X: -250 mm to +250 mm
- Y: -160 mm to +160 mm
- Z: -70 mm to +70 mm

### 17.2 Chassis Construction

The chassis is divided into three conceptual assemblies:

1. Lower structural plate
2. Main enclosure
3. Removable upper cover

Proposed lower plate dimensions:

- Length: 460 mm
- Width: 280 mm
- Thickness: 8 mm

The lower plate is positioned inside the overall chassis envelope.

Its proposed centre height is 49 mm above ground, corresponding to Z = -66 mm relative to base_link.

The main enclosure has an overall envelope of 500 x 320 x 140 mm.

### 17.3 Internal Component Arrangement

Planned component locations:

- Battery: low and near the chassis centre.
- Main computer: centre-rear region.
- Motor electronics: near the respective motor assemblies.
- Power distribution: near the battery.
- IMU: close to the estimated centre of gravity.
- Sensor wiring: protected internal routing.

Exact component positions will be established after selecting simulated component models.

### 17.4 Motor and Wheel Interface

The four motor assemblies will be mounted inside the chassis.

Each motor output shaft will extend through the corresponding chassis side region and connect to an external wheel hub.

Wheel mounting reference coordinates:

- Front left: (+170, +190, -35) mm
- Rear left: (-170, +190, -35) mm
- Front right: (+170, -190, -35) mm
- Rear right: (-170, -190, -35) mm

These coordinates are relative to base_link.

The wheel axle direction is along the Y-axis.

The final motor housing and shaft dimensions remain to be determined.

### 17.5 Collision and Visual Geometry

The initial Gazebo model will use one simplified chassis collision box:

- Length: 0.500 m
- Width: 0.320 m
- Height: 0.140 m

The collision box is centred on base_link.

The lower plate, upper cover and decorative panels will initially be visual components attached to the chassis.

Detailed collision geometry will be introduced only when necessary.

### 17.6 Preliminary Chassis Mass Allocation

| Component | Estimated mass |
|---|---:|
| Lower structure | 4.0 kg |
| Main enclosure | 3.0 kg |
| Internal support structures | 1.5 kg |
| Upper cover | 1.5 kg |
| Total | 10.0 kg |

These values are provisional simulation allocations.

### 17.7 Validation Requirements

Before finalizing the chassis:

1. Verify overall dimensions.
2. Verify wheel and motor clearances.
3. Inspect the battery and electronics layout.
4. Check the collision box against the wheel geometry.
5. Validate chassis mass and inertia.
6. Spawn the model in Gazebo.
7. Check for unwanted collisions and ground contact.

The chassis remains a preliminary design until these tests are completed.

## 18. Four-Wheel Drivetrain Engineering — Revision 0.5

### 18.1 Drivetrain Configuration

LUMEN uses four independently rotating rubber wheels in a skid-steer configuration.

The four motor-wheel assemblies use exposed industrial motor housings visible through side-window openings in the chassis.

The selected packaging configuration is Option A: motors housed within the chassis envelope.

### 18.2 Wheel Specification

| Parameter | Value |
|---|---:|
| Wheel diameter | 160 mm |
| Wheel radius | 80 mm |
| Wheel width | 45 mm |
| Wheel mass estimate | 1 kg |
| Number of wheels | 4 |
| Wheel type | Rubber cylindrical |

### 18.3 Wheel Hub

| Parameter | Proposed value |
|---|---:|
| Hub diameter | 60 mm |
| Hub axial length | 35 mm |
| Shaft interface diameter | 20 mm |
| Shaft engagement | Approximately 25 mm |

The hub is fixed to the corresponding rotating wheel link.

### 18.4 Output Shaft

- Proposed shaft diameter: 20 mm.
- Shaft axis: Y.
- Approximate engagement into hub: 25 mm.
- Four shaft assemblies.
- Shaft and hub connection represented as a fixed connection in the initial simulation.

### 18.5 Motor Housing

| Parameter | Proposed value |
|---|---:|
| Length along X | 100 mm |
| Width along Y | 70 mm |
| Height along Z | 70 mm |
| Number | 4 |
| Mounting | Fixed to chassis |
| Arrangement | Side-window packaging |

Motor centre positions relative to base_link:

- Front left: (+170, +115, -35) mm
- Rear left: (-170, +115, -35) mm
- Front right: (+170, -115, -35) mm
- Rear right: (-170, -115, -35) mm

### 18.6 Motor Mounting

Each motor is attached to the chassis using a fixed mounting interface.

Proposed mounting plate:

- Length: 100 mm
- Height: 90 mm
- Thickness: 6 mm

Detailed bolt positions and shaft geometry remain to be finalized.

### 18.7 Drivetrain Kinematics

Four independent wheel joints will be implemented.

Logical control groups:

Left:
- front_left_wheel_joint
- rear_left_wheel_joint

Right:
- front_right_wheel_joint
- rear_right_wheel_joint

The wheel axle direction is along the Y-axis.

### 18.8 Collision and Visual Modelling

Motor housings will initially be visual-only components fixed to the chassis.

The chassis collision geometry must provide suitable clearance around the motor mounting regions.

Wheel collision geometry will remain independent.

The final collision model must avoid overlapping solid collision bodies.

### 18.9 Drivetrain Validation

1. Verify all four wheel positions.
2. Check shaft and hub alignment.
3. Verify motor housing clearance.
4. Validate wheel joint axes.
5. Test forward movement.
6. Test reverse movement.
7. Test rotation in place.
8. Inspect wheel-ground contact.
9. Calibrate skid-steer turning behaviour.

This is a preliminary simulation design, not a validated physical drivetrain.

## 19. Sensor Mounting Engineering — Revision 0.6

### 19.1 Sensor Architecture

LUMEN will use three primary sensor assemblies:

1. 2D LiDAR
2. RGB-D camera
3. IMU

All sensors will be rigidly mounted to the robot structure.

### 19.2 Central LiDAR Assembly

| Parameter | Proposed value |
|---|---|
| Mounting type | Central vertical cylindrical mast |
| X position | 0 mm |
| Y position | 0 mm |
| Sensor centre height | 300 mm above ground |
| Z relative to base_link | +185 mm |
| Sensor frame | laser_link |
| Orientation | Horizontal scan plane |
| Mounting | Fixed |

The mast must not obstruct the LiDAR's horizontal scanning plane.

Mast diameter, length and mounting plate dimensions remain to be finalized after selecting the sensor housing.

### 19.3 Front RGB-D Camera Assembly

| Parameter | Proposed value |
|---|---|
| Mounting | Recessed front housing |
| Housing arrangement | Raised front sensor pod |
| X position | +230 mm |
| Y position | 0 mm |
| Sensor centre height | 420 mm above ground |
| Z relative to base_link | +305 mm |
| Direction | Forward (+X) |
| Proposed downward pitch | 10 degrees |
| Sensor frame | camera_link |
| Optical frame | camera_optical_frame |
| Mounting | Fixed |

The camera pod will be integrated into the front structure.

The camera aperture must provide an unobstructed viewing path.

The final pod dimensions, camera recess depth, X position and mounting angle require geometric validation.

### 19.4 Internal IMU Assembly

| Parameter | Proposed value |
|---|---|
| Mounting | Internal |
| X position | 0 mm |
| Y position | 0 mm |
| Z position | Approximately +0.6 mm |
| Sensor frame | imu_link |
| Orientation | Aligned with base_link |
| Mounting | Fixed |

The proposed position is based on the preliminary estimated centre of gravity of 115.6 mm above ground.

The IMU will be mounted close to the chassis centre.

### 19.5 Sensor Coordinate Conventions

Robot body frame:

- X: Forward
- Y: Left
- Z: Up

Camera optical frame:

- X: Right
- Y: Down
- Z: Forward

The camera optical frame will be connected to camera_link through a fixed transform.

The LiDAR scan plane will be horizontal relative to the robot.

### 19.6 Sensor Frame Hierarchy

base_link
├── laser_link
├── camera_link
│   └── camera_optical_frame
└── imu_link

All sensor frames will be connected through fixed joints.

### 19.7 Sensor Validation Requirements

1. Verify sensor mounting coordinates.
2. Check LiDAR 360-degree scanning clearance.
3. Verify camera viewing direction.
4. Check camera housing obstruction.
5. Verify camera optical frame orientation.
6. Verify IMU orientation.
7. Inspect sensor transforms in RViz2.
8. Validate sensor output in Gazebo.

This sensor architecture is preliminary and must be validated after implementation.

## 20. Wheel Module Packaging Study — Revision 0.8

### 20.1 Reference Geometry

The original motor and wheel positions are retained.

| Parameter | Value |
|---|---:|
| Motor centre Y | +115 mm |
| Motor outer face | +150 mm |
| Chassis outer boundary | +160 mm |
| Wheel inner face | +167.5 mm |
| Hub inner face | +172.5 mm |
| Wheel centre | +190 mm |

### 20.2 Packaging Constraint

The nominal distance between the motor outer face and wheel inner face is 17.5 mm.

This region must accommodate the necessary shaft, bearing support and mechanical interfaces where applicable.

### 20.3 Bearing Support Architecture

The selected concept is an independently bearing-supported wheel hub.

The bearing carrier will be structurally attached to the reinforced chassis side structure.

The motor will transmit torque through a suitable coupling.

### 20.4 Unresolved Engineering Parameters

- Bearing type and dimensions.
- Bearing spacing.
- Bearing carrier dimensions.
- Axle and shaft geometry.
- Coupling type and dimensions.
- Axial retention mechanism.
- Motor output interface.
- Structural attachment details.

### 20.5 Validation Requirements

1. Produce a dimensioned wheel-module cross-section.
2. Verify bearing and coupling packaging.
3. Check motor and chassis interference.
4. Verify wheel and hub alignment.
5. Calculate wheel support loads.
6. Validate shaft strength and deflection.
7. Confirm axial retention.
8. Check serviceability and bearing replacement.

No bearing or shaft dimensions are considered finalized at this stage.

## 21. Wheel Loading and Axle Design Basis — Revision 0.9

### 21.1 Robot Weight

Preliminary total robot mass: 25 kg.

Gravitational acceleration: 9.81 m/s².

Total weight:

W = 25 × 9.81 = 245.25 N

### 21.2 Static Wheel Loading

Assuming equal static load distribution across four wheels:

F_wheel = 245.25 / 4

Static load per wheel = 61.31 N.

This is an ideal estimate. Actual wheel loading will vary with centre of gravity, acceleration, turning and ground conditions.

### 21.3 Preliminary Radial Design Load

A provisional load factor of 3 is adopted for initial mechanical sizing.

F_design = 3 × 61.31

F_design = 183.9 N per wheel.

This is a preliminary engineering assumption and requires validation.

### 21.4 Bearing Architecture

- Two bearings per wheel are proposed.
- Total proposed bearing count: 8.
- Bearing carrier fixed to reinforced chassis structure.
- Rotating axle supported by the bearing pair.
- Motor torque transmitted through a suitable coupling.

### 21.5 Axle Design Requirements

The axle must be checked for:

1. Radial bending load.
2. Transmitted torque.
3. Combined bending and torsional stress.
4. Shaft deflection.
5. Fatigue strength.
6. Bearing-seat dimensions.
7. Axial retention.

### 21.6 Unresolved Parameters

- Bearing spacing.
- Wheel-load overhang.
- Bearing type and load rating.
- Axle material.
- Axle diameter.
- Coupling dimensions.
- Actual dynamic wheel loading.

No axle diameter or bearing selection is finalized by this calculation.

## 22. Wheel Bearing Reactions and Axle Load Analysis — Revision 1.0

### 22.1 Purpose

This section establishes the preliminary load-analysis method for LUMEN's four-wheel skid-steer drivetrain.

The objective is to determine the loads transmitted from each wheel through its hub, axle and bearing support into the chassis.

The bearing and axle dimensions remain subject to detailed geometric and mechanical validation.

### 22.2 Preliminary Wheel Loading

| Parameter | Value |
|---|---:|
| Preliminary robot mass | 25 kg |
| Number of wheels | 4 |
| Gravitational acceleration | 9.81 m/s² |
| Static load per wheel (equal distribution) | 61.31 N |
| Preliminary load factor | 3 |
| Preliminary radial design load per wheel | 183.94 N |

Static wheel load:

F_static = (m × g) / 4

F_static = (25 × 9.81) / 4

F_static = 61.31 N

Preliminary radial design load:

F_design = 3 × F_static

F_design = 183.94 N

The load factor of 3 is a preliminary design assumption, not a verified dynamic load factor.

Actual wheel loads may differ due to centre-of-gravity position, acceleration, braking, uneven ground and skid-steer manoeuvres.

### 22.3 Bearing Arrangement

The current design concept considers two bearings per wheel, giving eight bearings across the robot.

The intended load path is:

Wheel and tyre
→ Wheel hub
→ Rotating axle
→ Bearing inner races
→ Bearing rolling elements
→ Bearing outer races
→ Stationary bearing carrier
→ Chassis structure

The motor transmits driving torque through a coupling. The independent bearing support is intended to prevent the motor gearbox output from carrying the wheel's primary external radial and bending loads.

The physical bearing arrangement has not yet been finalized.

### 22.4 Bearing Reaction Model

For a simplified overhung wheel-load arrangement, define:

- F = radial design load at the wheel load plane.
- S = axial distance between the two bearing centres.
- e = distance from the outboard bearing centre to the wheel load plane.
- R_outboard = reaction magnitude at the outboard bearing.
- R_inboard = reaction magnitude at the inboard bearing.

For the idealized static model:

R_outboard = F × (1 + e/S)

R_inboard = F × (e/S)

The two bearing reactions act in opposite directions.

These equations are valid for the simplified two-support overhung-load model. Final analysis must account for the actual bearing arrangement, shaft geometry and applied loads.

### 22.5 Axle Bending and Torsion

For a solid circular axle:

Bending stress:

σ_b = 32M / (πd³)

Torsional shear stress:

τ = 16T / (πd³)

Where:

- M = maximum axle bending moment.
- T = transmitted axle torque.
- d = axle diameter.

For the simplified overhung arrangement:

M = F × e

A combined-stress check, fatigue assessment, deflection check and suitable safety factors will be required before selecting the axle diameter and material.

### 22.6 Geometry Required Before Numerical Validation

The following dimensions must be established:

1. Distance between bearing centres (S).
2. Wheel-load-plane overhang from the outboard bearing (e).
3. Axle diameter and material.
4. Bearing type and dimensions.
5. Bearing carrier geometry and mounting arrangement.
6. Motor output-shaft and coupling dimensions.
7. Axial retention method for the axle and hub.

The available 17.5 mm motor-to-wheel-inner-face gap must be considered during packaging. It must not be assumed that two conventional bearings can fit in this space.

### 22.7 Simulation Simplification

For the initial Gazebo model, each wheel will use a revolute joint connected to the chassis structure.

Physical bearing internals will not be modelled in the initial simulation.

The independent bearing-supported hub remains a physical design objective, subject to later packaging and mechanical validation.

### 22.8 Current Engineering Status

| Item | Status |
|---|---|
| Preliminary static wheel load | Calculated |
| Preliminary radial design load | Calculated |
| Two-bearing-per-wheel concept | Proposed |
| Bearing spacing | Not established |
| Wheel overhang | Not established |
| Bearing selection | Pending |
| Axle diameter and material | Pending |
| Axle stress validation | Pending |
| Bearing carrier design | Pending |

No final bearing or axle specification is approved in this revision.

## 23. Wheel Module Interface Definition — Revision 1.1

### 23.1 Coordinate Convention

The wheel axle is aligned with the Y-axis.

The left-side wheel module is located on the positive Y side of the robot. The right-side module is mirrored across the robot centre plane.

The wheel and motor centre positions are aligned in X and Z.

### 23.2 Known Left-Side Axial Geometry

| Interface | Y Position |
|---|---:|
| Motor outer face | +150 mm |
| Tyre inner face | +167.5 mm |
| Hub inner face | +172.5 mm |
| Wheel centre plane | +190 mm |
| Hub outer face | +207.5 mm |
| Tyre outer face | +212.5 mm |

### 23.3 Available Axial Space

Motor outer face to tyre inner face:

167.5 - 150 = 17.5 mm

Motor outer face to hub inner face:

172.5 - 150 = 22.5 mm

The 22.5 mm dimension is the nominal space between the motor output face and the hub inner face.

This dimension is not an approved bearing installation envelope. Bearing-carrier radial dimensions, mounting features, shaft shoulders, assembly clearances and actual motor output geometry must also be considered.

### 23.4 Wheel Module Functional Interfaces

The intended functional arrangement is:

Motor and gearbox
→ Torque coupling
→ Rotating axle
→ Wheel hub
→ Wheel and tyre

The bearing support is stationary relative to the chassis and supports the rotating axle.

The final bearing arrangement must transfer wheel radial loads and bending moments into the chassis without relying on the motor gearbox output as the primary wheel-load support.

### 23.5 Unresolved Motor Interface Dimensions

The following information is required before finalizing the wheel module:

1. Motor output-shaft diameter.
2. Motor output-shaft protrusion length.
3. Gearbox output-bearing arrangement and load capacity.
4. Motor mounting bolt pattern.
5. Coupling bore and length.
6. Axle shoulder and axial-retention arrangement.
7. Available bearing-carrier radial envelope.

These dimensions must be obtained from the selected motor/gearbox documentation or component CAD.

### 23.6 Engineering Constraints

- Retain the selected motor housing envelope and centre positions.
- Retain the selected wheel dimensions and centre positions.
- Do not assume two conventional bearings fit in the available axial space.
- Do not finalize axle diameter or bearing dimensions without load and packaging validation.
- Keep the Gazebo wheel-joint model independent of the unresolved physical bearing details.

### 23.7 Current Status

| Item | Status |
|---|---|
| Wheel axle direction | Defined |
| Wheel and motor centre alignment | Defined |
| Motor-to-wheel axial geometry | Calculated |
| Available motor-to-hub axial space | 22.5 mm |
| Motor output interface | Pending |
| Coupling dimensions | Pending |
| Bearing-carrier envelope | Pending |
| Final bearing arrangement | Pending |

## 24. Motor-to-Wheel Torque Transmission — Revision 1.2

### 24.1 Purpose

This section defines the preliminary torque-transmission architecture between each motor and its corresponding wheel.

The design uses four independently driven wheel assemblies. Each motor drives one wheel through a coaxial torque-transmission arrangement.

### 24.2 Torque Transmission Path

The proposed arrangement is:

DC motor
→ Gearbox
→ Flexible shaft coupling
→ Rotating axle
→ Wheel hub
→ Wheel and tyre

The coupling transfers rotational torque between the gearbox output and the wheel axle.

The independent wheel bearing support is responsible for supporting the wheel's external radial loads and bending moments.

The coupling must not be treated as the primary wheel bearing or structural wheel-load support.

### 24.3 Coupling Concepts

Three coupling types were considered:

| Coupling | Characteristics |
|---|---|
| Flexible jaw coupling | Elastomer element, vibration damping and limited misalignment tolerance |
| Bellows coupling | High torsional stiffness and precision |
| Rigid coupling | Direct torque transmission but requires accurate alignment |

A flexible jaw coupling is the preliminary candidate for LUMEN.

No coupling model or dimensions have been selected.

Final selection requires the motor output-shaft dimensions, axle dimensions, required peak torque, operating speed and available installation space.

### 24.4 Preliminary Wheel Torque Calculation

Assumptions:

- Robot mass = 25 kg
- Linear acceleration = 0.5 m/s²
- Number of driven wheels = 4
- Wheel radius = 0.08 m

Total ideal translational force:

F = m × a

F = 25 × 0.5

F = 12.5 N

Ideal force per wheel:

F_wheel = 12.5 / 4

F_wheel = 3.125 N

Ideal torque per wheel:

T_wheel = F_wheel × r

T_wheel = 3.125 × 0.08

T_wheel = 0.25 Nm

The calculated 0.25 Nm is an ideal translational acceleration estimate only.

It excludes rolling resistance, drivetrain losses, slopes, skid-steer tyre scrub, shock loads and rotational acceleration.

It must not be used as the final motor or coupling rating.

### 24.5 Coupling Selection Requirements

The final coupling must be checked against:

1. Gearbox output torque and peak torque.
2. Required operating rotational speed.
3. Motor output-shaft diameter.
4. Wheel axle diameter.
5. Coupling bore dimensions.
6. Available axial and radial installation space.
7. Permissible angular, parallel and axial misalignment.
8. Shock-load and fatigue requirements.
9. Coupling retention and assembly method.

The coupling torque rating must be suitable for the maximum expected transmitted torque, including an appropriate design margin.

### 24.6 Motor and Gearbox Considerations

The gearbox output is the relevant interface for the wheel coupling.

Motor shaft torque and gearbox output torque must not be confused.

Gear reduction changes output speed and torque. Actual output torque also depends on gearbox efficiency and its operating limits.

The selected motor and gearbox must satisfy the required wheel speed and torque simultaneously.

### 24.7 Current Engineering Status

| Item | Status |
|---|---|
| Four independent motor-to-wheel drives | Defined concept |
| Coaxial torque transmission | Proposed |
| Flexible jaw coupling | Preliminary candidate |
| Ideal wheel torque estimate | 0.25 Nm |
| Motor model | Pending |
| Gearbox ratio | Pending |
| Gearbox output torque | Pending |
| Coupling model and dimensions | Pending |
| Axle interface | Pending |
| Final torque validation | Pending |

No motor, gearbox or coupling specification is approved in this revision.

## 25. Motor and Gearbox Sizing Basis — Revision 1.3

### 25.1 Design Inputs

| Parameter | Value |
|---|---:|
| Preliminary robot mass | 25 kg |
| Number of driven wheels | 4 |
| Wheel radius | 0.08 m |
| Maximum linear speed | 0.5 m/s |
| Maximum angular speed | 1.0 rad/s |
| Geometric track width | 0.38 m |
| Preliminary wheel acceleration target | 0.5 m/s² |

### 25.2 Straight-Line Wheel Speed

Wheel angular velocity:

ω = v / r

ω = 0.5 / 0.08

ω = 6.25 rad/s

Wheel rotational speed:

RPM = (ω × 60) / (2 × π)

RPM = 59.68

The straight-line maximum speed requires approximately 60 RPM at the wheel.

### 25.3 Combined Linear and Angular Motion

Using the ideal skid-steer approximation:

v_right = v + (ω × B / 2)

v_left = v - (ω × B / 2)

Where:

- v = 0.5 m/s
- ω = 1.0 rad/s
- B = 0.38 m

Right-side velocity:

v_right = 0.5 + (1.0 × 0.38 / 2)

v_right = 0.69 m/s

Left-side velocity:

v_left = 0.5 - (1.0 × 0.38 / 2)

v_left = 0.31 m/s

Maximum wheel angular velocity:

ω_max = 0.69 / 0.08

ω_max = 8.625 rad/s

Maximum wheel rotational speed:

RPM_max = (8.625 × 60) / (2 × π)

RPM_max = 82.36

The calculated combined-motion requirement is approximately 82.4 RPM at the fastest wheel.

A preliminary wheel output-speed target of approximately 90 RPM is adopted for further motor and gearbox evaluation.

This is a sizing target, not a final selected specification.

The ideal kinematic model does not account for skid-steer tyre slip. Actual performance will require simulation and calibration.

### 25.4 Gear Reduction

The approximate gear reduction ratio is:

G = Motor RPM / Wheel RPM

For an illustrative motor speed of 3000 RPM and wheel output speed of 90 RPM:

G = 3000 / 90

G = 33.33

This example demonstrates the calculation only. The motor speed and gearbox ratio have not been selected.

### 25.5 Gearbox Output Torque

The ideal gearbox output torque relationship is:

T_output = T_motor × G × η

Where:

- T_motor = motor shaft torque.
- G = gearbox reduction ratio.
- η = gearbox efficiency.

The final gearbox must satisfy the required continuous and peak wheel torque while operating within its speed and thermal limits.

### 25.6 Torque Validation Requirements

The earlier ideal translational acceleration estimate of 0.25 Nm per wheel is not a final motor-sizing value.

Further analysis must include:

1. Rolling resistance.
2. Ground friction and skid-steer tyre scrub.
3. Incline and grade requirements.
4. Wheel and drivetrain rotational inertia.
5. Gearbox efficiency.
6. Continuous and peak torque.
7. Starting and stall conditions.
8. Thermal performance during continuous operation.

### 25.7 Motor Selection Criteria

The selected motor and gearbox must be evaluated using:

- Required wheel output speed.
- Required continuous wheel torque.
- Required peak wheel torque.
- Gearbox reduction ratio.
- Gearbox continuous and peak torque ratings.
- Gearbox efficiency.
- Motor voltage and current.
- Motor thermal limits.
- Encoder availability and resolution.
- Physical dimensions and mounting interface.
- Output shaft dimensions and coupling compatibility.

### 25.8 Current Engineering Status

| Item | Status |
|---|---|
| Straight-line wheel speed | Calculated |
| Combined-motion wheel speed | Calculated |
| Preliminary wheel speed target | Approximately 90 RPM |
| Example reduction ratio | 33.33:1 |
| Required continuous torque | Pending |
| Required peak torque | Pending |
| Motor model | Pending |
| Gearbox model | Pending |
| Encoder specification | Pending |
| Final motor validation | Pending |

No motor or gearbox model is approved in this revision.
