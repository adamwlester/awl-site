---
layout: project-detail-page
title: "Omniroute Maze System"
description: "A dynamically reconfigurable rodent maze system that integrates automated route configurations, sensory cue control, and targeted reward delivery."
summary: "A dynamically reconfigurable rodent maze system that integrates automated route configurations, sensory cue control, and targeted reward delivery."
hero: "images/hero.png"
model_src: "models/omniroute-maze-system.glb"
model_camera_orbit: "auto auto auto"
model_camera_target: "auto auto auto"
model_fov: "auto"
images:
  - src: "images/render_1.png"
    caption: "Three-quarter view (front, left, top) render of full Omniroute system with projected floor and wall cues"
  - src: "images/render_2_annotated.png"
    caption: "Annotated oblique view (front, top) render of full Omniroute system"
  - src: "images/render_3.png"
    caption: "Three-quarter view (front, left, top) render of feeder gantry and maze platform"
  - src: "images/render_4.png"
    caption: "Top view render of feeder gantry and maze platform"
  - src: "images/render_5.png"
    caption: "Top view render of maze platform with projected stimuli"
  - src: "images/render_6.png"
    caption: "Three-quarter view (front, right, top) render of maze platform with NC4gate modules"
  - src: "images/system_diagram.png"
    caption: "System architecture diagram"
  - src: "images/photo_1.png"
    caption: "Combined in-rig photos of ceiling and floor components of the Omniroute system"
  - src: "images/photo_2.png"
    caption: "Combined in-rig photos of example wall and floor projected stimuli"
published: true
---

<div class="content-groups">
<div class="content-group content-group-primary" markdown="1">

## Description

The Omniroute maze measures 90 × 90 cm and is organized as a 3 × 3 grid of chambers separated by 60 movable gates, which are featured as a separate portfolio entry ([NC4gate Automatable Gate Module](https://www.cadcrowd.com/3d-models/modular-gate-mechanism)). Each gate module, detailed in a separate project, can be raised or lowered programmatically to define unique routes in real time. The system also incorporates a CNC feeder gantry for spatially targeted liquid reward delivery, also featured as a separate portfolio entry ([Two-Axis Maze Feeder Gantry](https://www.cadcrowd.com/3d-models/modular-gate-mechanism)). Four short-throw projectors arrayed around the maze deliver dynamic visual cues onto the gate walls or maze floor as well as directional auditory cues. All components are designed and tested for compatibility with high-density electrophysiological recordings and closed-loop experimental paradigms.

Maze construction combines 80/20 aluminum extrusion for the structural frame, laser-cut POM-C acetal for the gate modules, and CNC-milled PVC foam board for the platform. The modular design allows rapid assembly, easy replacement of components, and scaling to different experimental configurations.

The system is controlled via the Robot Operating System (ROS) with custom nodes and Python/C++ libraries for gate actuation, GRBL-controlled gantry motion, and OpenGL-based cue projection and geometric transforms. Nodes communicate via ROS topics, services, and actions; device I/O uses serial, I²C, and PWM. Gates are driven by 12 V DC gearmotors via custom DRV8870 motor-driver PCBs, networked over I²C to Cypress I/O expander boards, enabling control of up to 512 gates from a single Arduino Mega. A high-speed 3D tracking pipeline streams pose to ROS at >100 Hz, enabling real-time closed-loop control of visual cues and reward delivery.

## Validation & Performance

**System latency:**  
- Sub-second gate actuation, projection updates, and audio playback  

**Gantry accuracy:**  
- Reliable centimeter-scale arrival to commanded targets in gantry tests  

**Electrophysiology compatibility:**  
- No movement-locked electrical artifacts during gate or gantry actuation  

**Behavioral performance:**  
- Above-chance task accuracy with projected cues and wall configurations  

## Materials & Fabrication

**Frame:**  
- 80/20 aluminum T-slot extrusion  

**Platform:**  
- CNC-milled foam PVC with integrated module slots and inserts  

**Gates:**  
- Laser-cut POM-C acetal modules with 12 V DC gearmotors, pin-in-slot linkage, and top/bottom limit switches  

**Electronics:**  
- Custom DRV8870 motor driver PCBs  
- Cypress I/O expanders on I²C  
- Arduino Mega control  

**Projector mounts:**  
- Waterjet-cut aluminum brackets with yaw and height adjustment  

**Gantry:**  
- OpenBuilds-style V-slot rails, NEMA 17 steppers, GT2 belts  
- Laser-cut acrylic roller plates, motor plates, and overhead panel  
- SLA-printed resin brackets and reward feeder assembly  

## Release

- **CAD:**
  - Gate modules:
    - Design files (CAD, PCB, documentation): [https://osf.io/uy7ez](https://osf.io/uy7ez)
    - See portfolio entry: ["NC4gate Automatable Gate Module"](https://www.cadcrowd.com/3d-models/modular-gate-mechanism)
  - Feeder gantry: see portfolio entry ["Two-Axis Maze Feeder Gantry"](https://www.cadcrowd.com/3d-models/feeder-gantry)
  - Projector mounts: see portfolio entry ["Adjustable Aluminum Projector Mount"](https://www.cadcrowd.com/3d-models/projector-mount)
- **Software:**
  - ROS workspace (Ubuntu host): [https://github.com/NC4Lab/omniroute_ubuntu_ws](https://github.com/NC4Lab/omniroute_ubuntu_ws)
  - ROS workspace (Windows host): [https://github.com/NC4Lab/omniroute_windows_ws](https://github.com/NC4Lab/omniroute_windows_ws)

## References

For additional details, including system performance tests, rodent behavior, and detailed schematics, see the preprint methods manuscripts for the Omniroute and the associated NC4gate system:
- Lester, A. W., Mombeini, A. G., & Madhav, M. S. (2025). [The Omniroute maze: a novel rodent navigation apparatus that integrates dynamically configurable routes, sensory cues, and automated reward delivery](https://www.biorxiv.org/content/10.1101/2025.09.01.672969v1). bioRxiv.
- Lester, A. W., Kaur, G., Djafri, N., & Madhav, M. S. (2024). [A modular gate system for autonomous control of rodent behavior](https://www.biorxiv.org/content/10.1101/2024.11.22.624912v1). bioRxiv.


</div>
<div class="content-group content-group-secondary" markdown="1">

## Role & Contributions

- Conceived and architected the system end-to-end
- Developed all CAD models and assemblies
- Fabricated and assembled key hardware
- Led teams for mechanical build, PCB development, and validation
- Principal author of GUI, control, and firmware
- Designed and executed validation
- Principal author of build documentation and SOPs
- Primary maintainer

## Highlights & Key Specs

**Platform:**  
- 90 × 90 cm with 3 × 3 chamber grid  
- 60 independently motorized gates  

**Cues:**  
- Four short-throw projectors with integrated speakers for dynamic visual and auditory stimuli  

**Reward:**  
- XY gantry for spatially targeted liquid reward anywhere on the platform  

**Tracking:**  
- Real-time 3D pose of animal and gantry  
- Closed-loop task control  

**System timing:**  
- Sub-second round-trip latencies for gates, projection, and audio as characterized in the preprint  

**Gantry performance:**  
- Centimeter-scale targeting accuracy with smooth velocity profiles  

## Deployment & Status

**Development:**  
- v1 developed, Dec 2021–Sep 2023  
- Feeder-gantry subsystem enhancements, Jun 2025–present  

**Deployment:**  
- NC4 Lab, University of British Columbia (3 studies)  

**Status:**  
Active, Sep 2023–present, NC4 Lab  

## Licensing

- **Hardware:** CERN-OHL-W-2.0
- **Software:** MIT
- **Documentation:** CC-BY-4.0


</div>
</div>
