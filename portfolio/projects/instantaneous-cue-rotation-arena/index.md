---
layout: project-detail-page
title: "Instantaneous Cue Rotation Arena"
summary: "An augmented reality behavioral arena for studying cue-based navigation in freely moving rats."
hero: "images/render_1.png"
model: "models/instantaneous-cue-rotation-arena.glb"
images:
  - src: "images/render_1.png"
    caption: "three-quarter view (front, right, top) render of full arena exterior with ceiling recess and strut channels"
  - src: "images/render_2_annotated.png"
    caption: "annotated front view render of arena layout"
  - src: "images/render_3.png"
    caption: "three-quarter view (rear, right, top) render of arena interior with robot and rat"
  - src: "images/render_4.png"
    caption: "top view render of arena interior with robot and rat"
  - src: "images/render_5.png"
    caption: "oblique view (right, top) render of robot and rat inside ICR arena"
  - src: "images/photo_1.png"
    caption: "in-rig photo of full arena in lab"
  - src: "images/photo_2.png"
    caption: "in-rig photo of rat on track with wall cues"
---

## Description

The Instantaneous Cue Rotation Arena is an augmented-reality rodent behavioral arena enabling instantaneous rotation of all orienting visual cues during ongoing navigation with extracellular electrophysiology recordings. The 1.4 m diameter circular track is enclosed by 68 cm tall rear-projection panels that form a seamless 360° panorama of visual cues. Four short-throw projectors render these cues and can rotate them remotely and instantaneously without removing the animal from the track to assess their effect on navigation accuracy. A mobile feeder robot tracks the rat to deliver food-based reinforcement, which is featured as a separate portfolio entry ([Wireless Mobile Feeder Robot](https://www.cadcrowd.com/3d-models/feeder-robot)). All static elements within the behavioral space are repeated every 10° to eliminate symmetry-breaking spatial cues. The structure uses 80/20 aluminum extrusion with ESD-coated acrylic and PVC foam board for durability and electrophysiology compatibility. The assembly is suspended from ceiling strut channels to keep the interior clear and allow access from below. An overhead speaker, recessed into the ceiling, delivers auditory cues and continuous white noise to mask potential orienting sounds that could conflict with the cue manipulation. Below this, a centrally mounted commutator with a drop-down boom arm keeps the tether aligned directly above the circular track for wired electrophysiology. Two overhead color cameras are offset to either side of the commutator to maintain coverage when either camera’s line of sight is occluded by the boom arm and provide continuous tracking data for the rat and feeder robot. The floor of the arena can be lowered via gas springs and pulleys to allow easy access to the base for cleaning and maintenance.

The system integrates with a NeuraLynx Digital Lynx SX acquisition system that records real-time position and stores synchronous timestamps for cue rotations and reward events. Two Arduino Due microcontrollers, one housed in the feeder robot, handle reward delivery, manage positional tracking and wireless serial communications, and actuate DC relays for projection and sound events, while sending accompanying TTL pulses to the acquisition system. Phototransistor sensors detect image changes on each projector and output TTL pulses that, together with TTLs for sound events, enable precise alignment of neural, behavioral, and stimulus data.

The mobile feeder robot tracks the rat to deliver precisely timed, spatially targeted liquid food reward without providing a static spatial cue that would interfere with the cue manipulation. The robot is wirelessly controlled via XBee-PRO Series 1 radios and powered by a LiPo battery, eliminating the need for a dedicated commutator. A retractable dish delivers liquid rewards. Onboard sensors track rat position using fused data from an overhead camera and a Pixy vision module. A cleaning module continuously clears debris and applies ethanol to minimize odor contamination.

A custom codebase coordinates all hardware components: C and C++ firmware on the microcontrollers for wireless communication, motor control, and timing; a C# application for wireless data streaming and interface tasks; and MATLAB scripts that provide the experimenter frontend, process tracking data, control visual cues, and synchronize peripheral systems.

This design cleanly dissociates external cues from self-motion feedback, while also restricting any olfactory or auditory orienting cues, in order to assess real-time visual cue use during uninterrupted navigation with full neural and behavioral synchronization.

## Role & Contributions

- Conceived and architected the system end-to-end
- Developed all CAD models and assemblies
- Fabricated and assembled key hardware
- Coordinated machining/fabrication of select parts
- Led teams for mechanical build and validation
- Authored control software, GUI, and analysis pipeline
- Designed and executed behavioral validation

## Highlights & Key Specs

**Arena:**  
- 1.4 m diameter circular track  
- 68 cm projection walls  
- Track can be accessed from underneath for training or lowered via gas springs and pulleys to allow easy access to the base for cleaning  

**Visual stimulus system:**  
Four short-throw projectors (BenQ MW621ST) with instantaneous remote cue rotations  

**Synchronization and I/O:**  
- Arduino Due controllers  
- NeuraLynx Digital Lynx SX integration  
- Phototransistor-triggered TTL, millisecond-precision timestamps for cue-change alignment  

**Reward and tracking:**  
- Mobile feeder robot with XBee-PRO wireless and LiPo power  
- Retractable liquid-reward dish  
- Fused overhead camera and Pixy-based position tracking  

**Software stack:**  
- MCU firmware in C/C++  
- C# wireless data interface  
- MATLAB control and analysis frontend and GUI  

**Acoustic control:**  
Continuous white noise to mask orienting auditory cues and optional sound cues  

## Materials & Fabrication

**Structure:**  
- 80/20 aluminum extrusion frame  
- Acrylic and PVC foam board  
- FlexGlass projection surface for rear projection  

**Electronics:**  
- Arduino Due microcontrollers  
- NeuraLynx Digital Lynx SX  
- Phototransistors  
- XBee-PRO Series 1 radios  
- LiPo battery system  
- Pixy vision module  

## Validation & Performance

**Behavioral performance:**  
Peer-reviewed methods paper documents apparatus and behavioral outcomes (see References)  

**Stable use:**  
In-rig and in vivo use across 2 experiments  

## Deployment & Status

**Development:**  
Completed, Aug 2013–May 2017  

**Deployment:**  
Barnes Lab, University of Arizona (2 studies)  

**Status:**  
Active, May 2017–present, Barnes Lab  

## Release

- **CAD:**
  - ICR: full assembly STEP available in portfolio (see 3D Model Files)
  - Mobile feeder robot: see portfolio entry “[Wireless Mobile Feeder Robot](https://www.cadcrowd.com/3d-models/feeder-robot)”
- **Software:**
  - Firmware and software repo: [https://github.com/adamwlester/icr-system](https://github.com/adamwlester/icr-system)

## Licensing

- **Hardware:** CERN-OHL-W-2.0
- **Software:** MIT
- **Documentation:** CC-BY-4.0

## References

For additional details, see the published methods manuscript, which features this system, and the subsequent study:
- Lester, A. W., Kapellusch, A. J., & Barnes, C. A. (2020). [A novel apparatus for assessing visual cue-based navigation in rodents](https://doi.org/10.1016/j.jneumeth.2020.108667). Journal of Neuroscience Methods, 338, 108667.
- Lester, A. W., Jordan, G. A., Blum, C. J., Philpot, Z. P., & Barnes, C. A. (2022). [Differential effects in young and aged rats’ navigational accuracy following instantaneous rotation of environmental cues](https://pubmed.ncbi.nlm.nih.gov/36395015/). Behavioral Neuroscience, 136, 561–574.

## Included files

*Attached on this page.*

### Image Files

- **render_1.png:** three-quarter view (front, right, top) render of full arena exterior with ceiling recess and strut channels
- **render_2_annotated.png:** annotated front view render of arena layout
- **render_3.png:** three-quarter view (rear, right, top) render of arena interior with robot and rat
- **render_4.png:** top view render of arena interior with robot and rat
- **render_5.png:** oblique view (right, top) render of robot and rat inside ICR arena
- **photo_1.png:** in-rig photo of full arena in lab
- **photo_2.png:** in-rig photo of rat on track with wall cues

### 3D Model Files

- **icr_arena_TOP_ASSY.step:** top-level Instantaneous Cue Rotation arena assembly
- **feeder_robot_SUB.step:** feeder robot subassembly