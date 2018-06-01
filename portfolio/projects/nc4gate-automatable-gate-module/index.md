---
layout: project
title: "NC4gate Automatable Gate Module"
summary: "Modular motorized gate system for autonomous control of rodent behavior in maze experiments."
hero: "hero.png"
model: "models/nc4gate-automatable-gate-module.glb"
images:
  - src: "images/render_1.png"
    caption: "three-quarter view (front/rear, right, top) render of gate module"
  - src: "images/render_2.png"
    caption: "three-quarter view (front, right, top) render of gate module in raised and lowered state"
  - src: "images/render_3.png"
    caption: "three-quarter view (rear, right, top) render of gate module in raised and lowered state"
  - src: "images/render_4_annotated.png"
    caption: "annotated three-quarter view (front/rear, right, top) render of gate module"
  - src: "images/render_5.png"
    caption: "three-quarter view (front, right, top) render of 60 gate modules installed in Omniroute rig"
  - src: "images/cadview_1_annotated.png"
    caption: "annotated exploded CAD view of gate module"
  - src: "images/photo_1.png"
    caption: "bench photo of gate module, electronics side"
  - src: "images/photo_2.png"
    caption: "bench photo of gate module, wall panel side"
  - src: "images/photo_3.png"
    caption: "bench photo of 60 gate modules installed in Omniroute rig"
---

## Description

These gate modules, termed the NC4gate, were designed for use with another portfolio project: the [Omniroute Maze System](https://www.cadcrowd.com/3d-models/omniroute-maze-system). 

Each module is constructed from laser-cut POM-C acetal panels joined with snap-fits and minimal fasteners, with a waterjet-cut aluminum pin-in-slot linkage driven by a compact 12 V DC gearmotor. Limit switches at the top and bottom of travel register position and ensure safe, reliable operation. The design provides 180 mm of gate travel in a compact 117 × 86 × 290 mm footprint, allowing modules to be densely packed in multi-gate maze systems. Standard hardware and drilling jigs streamline fabrication and assembly.  

Electronics include a custom motor driver board (based on the TI DRV8870 chip) for PWM motor control and limit switch monitoring. For large-scale setups, modules connect via I²C to Cypress expansion boards, enabling a single Arduino Mega to control up to 512 gates.

## Role & Contributions

- Conceived, designed, and fabricated the mechanical system
- Developed all CAD models and assemblies
- Directed custom PCB development team
- Principal author of firmware and host software
- Produced assembly, wiring, and operating documentation
- Primary maintainer

## Highlights & Key Specs

**Envelope:**  
117 × 86 × 290 mm (gate lowered)

**Gate travel:**  
180 mm total

**Typical actuation time:**  
~578 ms up, ~531 ms down

**Endurance:**  
- Thousands of cycles  
- Individual modules tested up to 100,000 cycles  

**Control scale:**  
Up to 512 gates from a single PC and microcontroller

**Interfaces:**  
Qt-based GUI for manual operation; Python API for programmatic control

## Materials & Fabrication

**Structure:**  
Laser-cut POM-C acetal (3.175 mm) with snap-fit features and minimal fasteners

**Actuation:**  
12 V 50 RPM DC gear motor (37 mm can) driving pin-in-slot linkage

**Linkage:**  
Waterjet-cut aluminum arm for durability under repeated cycling

**Sensing:**  
Upper and lower limit switches for hard-stop detection

**Hardware:**  
Standard fasteners, spacers, rollers; cable ties and strain relief provisions

## Validation & Performance

**Actuation latency:**  
Tests on N=5 modules across 50 cycles each show consistent latencies: upward ~578 ms and downward ~531 ms, suitable for behavioral control

**Stress testing:**  
- Long operational life up to 100,000 cycles, with field-repairable failure modes (motor wear, linkage retention, wiring)  
- 60-module system running near-daily for over one year  

## Deployment & Status

**Development:**  
Completed, Dec 2021–Sep 2023

**Deployment:**  
NC4 Lab, University of British Columbia (3 studies)

**Status:**  
Active, Sep 2023–present, NC4 Lab	

## Included files

*Attached on this page.*

### Image Files

- **render_1.png:** three-quarter view (front/rear, right, top) render of gate module
- **render_2.png:** three-quarter view (front, right, top) render of gate module in raised and lowered state
- **render_3.png:** three-quarter view (rear, right, top) render of gate module in raised and lowered state
- **render_4_annotated.png:** annotated three-quarter view (front/rear, right, top) render of gate module
- **render_5.png:** three-quarter view (front, right, top) render of 60 gate modules installed in Omniroute rig
- **cadview_1_annotated.png:** annotated exploded CAD view of gate module
- **photo_1.png:** bench photo of gate module, electronics side
- **photo_2.png:** bench photo of gate module, wall panel side
- **photo_3.png:** bench photo of 60 gate modules installed in Omniroute rig

### 3D Model Files

- **nc4_gate_TOP_ASSY_lowered.step:** top-level assembly of automatable gate module in lowered position
- **nc4_gate_TOP_ASSY_raised.step:** top-level assembly of automatable gate module in raised position

## Release

- **CAD:** 
  - Design files including SolidWorks assemblies and parts, PCBs, jigs, cutting templates, and documentation: [https://osf.io/uy7ez](https://osf.io/uy7ez)
- **Software:**
  - Standalone NC4gate firmware and software repo: [https://github.com/NC4Lab/NC4gate](https://github.com/NC4Lab/NC4gate)
  - Omniroute system firmware and software repo:
    - ROS workspace (Ubuntu host): [https://github.com/NC4Lab/omniroute_ubuntu_ws](https://github.com/NC4Lab/omniroute_ubuntu_ws)
    - ROS workspace (Windows host): [https://github.com/NC4Lab/omniroute_windows_ws](https://github.com/NC4Lab/omniroute_windows_ws)
- **Related portfolio entry:** [Omniroute Maze System](https://www.cadcrowd.com/3d-models/omniroute-maze-system)

## Licensing

- **Hardware:** CERN-OHL-W v2.0
- **Software:** Apache-2.0
- **Documentation:** CC BY 4.0

## References

For additional details, including system performance tests and detailed schematics, see the preprint methods manuscripts for the NC4gate system and associated Omniroute maze:
- Lester, A. W., Kaur, G., Djafri, N., & Madhav, M. S. (2024). [A modular gate system for autonomous control of rodent behavior](https://www.biorxiv.org/content/10.1101/2024.11.22.624912v1). bioRxiv.
- Lester, A. W., Mombeini, A. G., & Madhav, M. S. (2025). [The Omniroute maze: a novel rodent navigation apparatus that integrates dynamically configurable routes, sensory cues, and automated reward delivery](https://www.biorxiv.org/content/10.1101/2025.09.01.672969v1). bioRxiv.
