---
layout: project-detail-page
title: "Two-Axis Feeder Gantry"
description: "CNC-based gantry system for automated spatially targeted reward delivery in rodent open-field experiments."
summary: "CNC-based gantry system for automated spatially targeted reward delivery in rodent open-field experiments."
hero: "images/render_1.png"
model_src: "models/two-axis-feeder-gantry.glb"
model_camera_orbit: "auto auto auto"
model_camera_target: "auto auto auto"
model_fov: "auto"
images:
  - src: "images/diagram_1.png"
    caption: "Annotated top view diagram of gantry layout and travel"
  - src: "images/diagram_2.png"
    caption: "Annotated top and side view diagram of feeder arm assembly"
  - src: "images/render_1.png"
    caption: "Three-quarter view (front, left, top) render of full feeder gantry"
  - src: "images/render_2.png"
    caption: "Top view render of full feeder gantry"
  - src: "images/render_3.png"
    caption: "Top view render of cover carriage with feeder arm"
  - src: "images/render_4.png"
    caption: "Three-quarter view (front, right, top) render of cover carriage with feeder arm"
  - src: "images/render_5.png"
    caption: "Three-quarter view (front, right, top) render of feeder arm assembly, close-up"
  - src: "images/photo_1.png"
    caption: "On-rig photo of the feeder gantry installed on the Omniroute system; legacy servo-driven feeder arm"
  - src: "images/photo_2.png"
    caption: "On-rig top view of the cover carriage over the Omniroute system; legacy servo-driven feeder arm"
published: true
---

<div class="content-groups">
<div class="content-group content-group-primary" markdown="1">

## Description

This reward delivery system was designed for use with another portfolio project: the [Omniroute Maze System](https://www.cadcrowd.com/3d-models/omniroute-maze-system).

The gantry provides spatially targeted liquid reward by tracking animal movement within the Omniroute maze while simultaneously carrying a ceiling panel that prevents rats from climbing maze walls and houses a retractable feeder arm that can be rotated down to the maze floor for reward delivery. Motion control is handled by an OpenBuilds BlackBox X32 running GRBL and integrated with the Omniroute ROS stack for command, coordination, and tracking.

**Frame and motion platform:** The translation stage follows the OpenBuilds ACRO architecture with V-slot extrusion (20 × 40 mm profile), Delrin V-wheels, GT2 belts, and NEMA 17 steppers. The assembled stage has a footprint of 2.2 × 1.4 m (X, Y) and provides 1.6 × 0.8 m of usable travel. Enclosed cable carriers on the X and Y axes route wiring. Custom laser-cut motor and guide plates in 1/4 in high-impact acrylic provide stiff mounting for motors, idlers, and cable-chain anchors, and create direct interfaces to the cover carriage frame. The design leverages the ACRO stage format and select OpenBuilds components for the linear motion subsystem, while the mechanical interfaces, controller integration, platework, and fixtures are all customized to meet Omniroute’s geometry and the additional cover carriage and feeder arm functionality.

**Gantry cover carriage:** An approximately 60 × 60 cm carriage built from 10 × 10 mm lightweight aluminum extrusions carries a clear acrylic panel that acts as a moving ceiling to block climbing. The carriage includes printed brackets for the cover panel and support plates for guide wheels, plus integrated mounts for the liquid food reward vial, peristaltic pump, and feeder arm assembly (including the Z-axis motor, pulley posts, and limit-switch hardware). The frame geometry and component placement are tuned to maintain maze-wall clearance, keep high-visibility hardware away from the center of the animal’s sightlines, and avoid occlusion of the projected wall and floor stimuli used in the Omniroute maze.

**Feeder arm:** A retractable feeder arm assembly is mounted on the carriage and operates as a Z-axis accessory that rotates down to deliver liquid reward at a commanded XY location, then retracts to a parked position above the cover panel. Z motion is driven by a fourth NEMA 17 stepper on the motion controller Z channel through a timing-belt train with custom SLA-printed pulleys that couple the motor to the feeder arm. A small pulley-mounted cam actuates a lever-style limit switch at the fully retracted position, enabling reliable homing and interlocks. The dispensing arm uses a 1/4 in stainless-steel tube with a custom SLA angle connector joined to a flexible extension spring forming the short leg of the L-arm. A continuous silicone line runs from the pump through the tube and connector to the arm terminus. This linkage uses a doubled effective gear ratio to provide sufficient force margin to retract even if a rat hangs on it. The flexible arm end is designed to protect animals and maze walls if the arm contacts a rat during lowering or the gantry resumes movement before retracting.

**Design revision:** Upgraded to a stepper-driven actuator with integrated limit switch detection, replacing the original servo. The design is complete and being integrated into the assembly. The revised arm has stiffer components and a flexible end.

## Validation & Performance

**Traverse speed:**  
- Peak 0.47 m/s  
- Mean 0.21 m/s  

**Arrival latency:**  
1.5 s to within 2 cm over a 0.43 m move  

**Positional accuracy:**  
0.7 cm final error at stop  

**Acoustic profile:**  
+20 dB SPL during motion vs idle  

## Materials & Fabrication

**Frame and motion platform:**  
- V-slot 20 × 40 mm extrusion  
- Laser-cut 1/4 in high-impact acrylic motor and guide plates  
- GT2 belts and idlers  
- NEMA 17 steppers  
- OpenBuilds BlackBox X32 motion controller and Xtension Limit Switches  

**Gantry cover assembly:**  
- Laser-cut 1/16 in clear acrylic panel  
- Laser-cut 1/4 in high-impact acrylic motor, guide, and mounting plates  
- 10 × 10 mm aluminum T-slot extrusion frame  

**Feeder arm:**  
- NEMA 17 stepper  
- SLA-printed timing pulleys  
- GT2 belt  
- E-Switch limit switch (MS0850503F025C1C)  
- 1/4 in stainless-steel tube  
- 1/4 in extension spring  

**Pump and lines:**  
- Gravity Digital Peristaltic Pump (DFRobot DFR0523)  
- Food-grade silicone tubing  
- Glass vial reservoir  

## Release

- **CAD:** select STEP files available in portfolio (see 3D Model Files)
- **Software:**
- ROS workspace (Ubuntu): [https://github.com/NC4Lab/omniroute_ubuntu_ws](https://github.com/NC4Lab/omniroute_ubuntu_ws)
- ROS workspace (Windows): [https://github.com/NC4Lab/omniroute_windows_ws](https://github.com/NC4Lab/omniroute_windows_ws)
- **On request:** additional design files
- **Related portfolio entry:** [Omniroute Maze System](https://www.cadcrowd.com/3d-models/omniroute-maze-system)

## References

For additional details, including system performance tests, see the preprint methods manuscript for the Omniroute maze, which features this subsystem:
- Lester, A. W., Mombeini, A. G., & Madhav, M. S. (2025). [The Omniroute maze: a novel rodent navigation apparatus that integrates dynamically configurable routes, sensory cues, and automated reward delivery](https://www.biorxiv.org/content/10.1101/2025.09.01.672969v1). bioRxiv.


</div>
<div class="content-group content-group-secondary" markdown="1">

## Role & Contributions

- Conceived, designed, built, and maintained end to end
- Developed all CAD models and assemblies
- Led mechanical and electrical build team
- Authored firmware and PC software
- Designed and executed validation
- Primary maintainer

## Highlights & Key Specs

**Footprint:**  
2.2 × 1.4 m (X, Y) frame envelope  

**Travel:**  
1.6 × 0.8 m (X, Y) commanded range  

**Carriage capacity:**  
60 × 60 cm cover area  

**Motion performance:**  
peak traverse speed: 0.47 m/s  

## Deployment & Status

**Development:**  
- V1 developed, Jan 2023–Sep 2023  
- Feeder arm v2 integration, Jun 2025–present  

**Deployment:**  
NC4 Lab, University of British Columbia (3 studies)  

**Status:**  
active, Sep 2023–present, NC4 Lab  

## Licensing

- **Hardware:** CERN-OHL-W-2.0
- **Software:** MIT
- **Documentation:** CC-BY-4.0


</div>
</div>
