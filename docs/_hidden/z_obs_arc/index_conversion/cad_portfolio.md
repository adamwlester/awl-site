# Roller-Bearing Cable Guide

## Summary
Compact, low-torsion cable guide with a bearing-mounted collet and dual-rail carriage for quiet, low-resistance travel in tethered rodent recordings.

## Description
Designed for linear-track experiments, this guide prevents torsion on the headstage cable while allowing smooth travel along the track. A collet mounted in a roller bearing isolates twist from the signal cable as the animal runs, and the carriage rides on dual stainless-steel rails using adjustable plastic roller bearings for quiet motion.

## Role & Contributions
- Designed and fabricated all components
- Integrated into linear-track recording rigs

## Highlights & Key Specs
- **Cable interface:** collet accommodates 3/16 in cable; twist isolation via roller bearing
- **Guide travel:** along two 4 ft, 1/2 in diameter stainless-steel rails
- **Bearings:** plastic roller bearings on rails; internal roller bearing at collet
- **Commutator-ready:** intended for use downstream of a commutator to minimize cable torsion
- **Serviceability:** field-adjustable preload on roller bearings; standard hand tools

## Materials & Fabrication
- **Housing and collet**: SLA-printed resin two-part housing and two-part collet
- **Rails**: 1/2 in diameter stainless-steel rails, 4 ft length
- **Bearings**: plastic races with 316 stainless balls; 3/4 in ID × 1.625 in OD and 1/8 in ID × 0.375 in OD
- **Hardware**: #4-40 stainless bolts with nylon-insert lock nuts and #4 washers for roller assemblies

## Validation & Performance
- **Stable use:** In-rig and in vivo use with stable recordings for 2 experiments and 3 rigs.

## Deployment & Status
- **Development:** completed, Jan 2018–Feb 2018
- **Deployment:** Barnes Lab, University of Arizona (2 studies; 3 rigs)
- **Status:** active, Feb 2018–present, Barnes Lab

## Release
- **CAD:** STEP files available in portfolio (see 3D Model Files)
- **On request:** additional design files

## Licensing
- **Hardware:** CERN-OHL-W v2.0
- **Documentation:** CC BY 4.0

## Included files
*Attached on this page.*

### Image Files
- **render_1.png:** three-quarter view (front, right, top) render of the cable guide assembly
- **render_2_annotated.png:** annotated three-quarter view (front, right, top) render of the cable guide assembly
- **render_3.png:** top view render of the cable guide assembly

### 3D Model Files
- **cable_guide_TOP_ASSY.step:** top-level assembly of the cable guide
- **cable_guide_PART_housing_a.step:** first housing half
- **cable_guide_PART_housing_b.step:** second housing half
- **cable_guide_PART_split_collet.step:** two-part split collet for 3/16 in cable

# Dual-Bundle Electrode Drive

## Summary
Split-bundle implant for dual-region tetrode recordings in freely moving rats.

## Description
The drive is built around the NeuraLynx Halo-18 Microdrive design and utilizes the NeuraLynx FreeLynx wireless headstage and EIB-72-QC-Large electrode interface board (EIB). It separates 18 tetrodes into two independently adjustable bundles that can target different brain regions. Each bundle contains nine shuttles that can be raised or lowered individually, providing precise depth control. Bundle collars secure the front and rear bundles, while adjustment screws provide fine control along both anterior–posterior and dorsal–ventral axes to accommodate different recording targets and variable brain anatomy. At the distal end, the exit tip guides tetrodes into position with stable alignment.

During recording, a headstage cover secures the NeuraLynx FreeLynx wireless headstage and routes power to LEDs that use a diffuser lens to improve video tracking. The drive also supports a cap with a weight attachment that can be loaded with washers to gradually acclimate animals to the weight of the FreeLynx headstage and battery while they are in the home cage. Both options use magnets to align the part to the drive via corresponding magnets on the EIB and a single thumb screw to secure it.

## Role & Contributions
Core drive elements (body, core, shuttle) derived from NeuraLynx Halo-18 with substantial redesigns:
- Reconceived drive core with higher-strength components to reinforce 3D-printed parts
- Reconceived drive core and shuttle to add support and guide cannulae for split-bundle use, improving tetrode-travel stability and reliability
- Newly developed all other components, including cap and cover assemblies, tracking-LED electronics, and the split-bundle guide system
- Developed all CAD models and assemblies
- Authored build documentation and SOPs
- Primary maintainer

## Highlights & Key Specs
- **Mass:** ~24 g for drive body, core, bundle guide, shuttles, and guide cannulae
- **Shuttles:** M1 × 0.20 screws; ~9 mm total dorsal–ventral travel
- **Bundles:** two independently adjustable 9-tetrode bundles
- **Cover:** magnetically aligned cover for NeuraLynx FreeLynx with integrated LED tracking diffuser and thumb screw
- **Cap:** magnetically aligned cap with thumb screw retention and adjustable weights for acclimation

## Materials & Fabrication
- **Structure:** SLA-printed resin body, bundle guide, cap, and cover components
- **Shuttles:** machined M1 screws and UHMW polyethylene shuttle plates
- **Electronics:** surface-mount LEDs integrated in headstage cover
- **Hardware:** standard hardware including #0-80 and M1 fasteners, washers, springs, neodymium magnets, center post

## Validation & Performance
- **Stable use:** In-rig and in vivo use with stable recordings for 2 studies and 9 implants total.

## Deployment & Status
- **Development:** completed, Aug 2019–Jun 2020
- **Deployment:** Barnes Lab, University of Arizona (2 studies)
- **Status:** active, Jun 2020–present, Barnes Lab

## Release
- **CAD:** 
  - STEP files available in portfolio (see 3D Model Files)
  - Select additional files (i.e., drive body) withheld due to third-party IP
- **On request:** assembly notes

## Licensing
- **Hardware:** CERN-OHL-W v2.0
- **Documentation:** CC BY 4.0

### Attribution
- Inspired by the NeuraLynx Halo-18; Halo-18-compatible geometry; independent, non-affiliated design. NeuraLynx and FreeLynx are trademarks of their owner; names used for identification only.
- Special thanks and acknowledgement to Anders Lundberg, designer of the Halo-18, for informal guidance during scoping; all engineering decisions and CAD were produced independently.

## Included files
*Attached on this page.*

### Image Files
- **render_1.png:** three-quarter view (rear, left, top) render of the complete dual-bundle drive with FreeLynx cover and Halo-18 components
- **render_2_annotated.png:** annotated exploded three-quarter view (rear, left, top) render of major assemblies, excluding cap and cover
- **render_3_annotated.png:** annotated cross-section view render of the drive body and core with bundle guide
- **render_4_annotated.png:** annotated three-quarter view (rear, left, bottom) render of the bundle guide subassembly
- **render_5_annotated.png:** annotated three-quarter view (rear, left, top) render of the complete dual-bundle drive with FreeLynx cover and Halo-18 components
- **render_6_annotated.png:** annotated exploded three-quarter view (rear, left, top) render of the FreeLynx cover with LED and diffuser stack
- **render_7.png:** three-quarter view (rear, left, top) render of the drive cap and adjustable weight
- **render_8.png:** exploded three-quarter view (rear, left, top) render of the drive cap and adjustable weight
- **photo_1.png:** bench photo of the fully assembled drive with cap installed
- **photo_2.png:** close-up bench photo showing the drive body and core with bundle guide

### 3D Model Files
- **electrode_drive_SUB_core.step:** drive core assembly, including drive core, shuttles, and cannulae 
- **electrode_drive_SUB_bundle_guide.step:** bundle guide component for split-bundle routing
- **electrode_drive_SUB_cover.step:** headstage cover with LED diffuser interfaces
- **electrode_drive_SUB_cap.step:** cap with weight attachment

# Silicon Probe Microdrive Housing

## Summary
Implantable housing for high-density chronic silicon probe recordings in freely moving rats.

## Description
The housing is compatible with the 128-channel SpikeGadgets Horizontal Headstage and Cambridge Neurotech ASSY-236 F probes, and incorporates the Cambridge Neurotech NanoDrive for probe positioning. A custom probe interface PCB provides electrical interconnect and mechanical support between the probe and headstage. The three-part SLA-printed resin housing uses standard #0-80 fasteners for straightforward fabrication, assembly, and maintenance. Fine adjustment is achieved by accessing the NanoDrive through a top access hole that isolates the lead screw from probe components, providing approximately 6 mm of travel. The headstage clips into place on the back of the housing, angled at 10° to allow free head movement. The detachable base of the housing provides an adhesion point for surgical cement and enables easy extraction of the intact probe and main housing body for reuse.

## Role & Contributions
- Conceived, designed, fabricated, and maintained mechanical components end to end
- Directed custom probe-interface PCB development team
- Primary maintainer

## Highlights & Key Specs
- **Drive:** adjustment resolution ~250 µm per turn; rated travel up to 7.5 mm (implemented ~6 mm)
- **Mass:** ~5 g with housing, hardware, NanoDrive, and probe
- **Assembly:** straightforward three-part assembly with standard #0-80 fasteners and nuts
- **Compatibility:** Cambridge Neurotech 64-channel probes (ASSY-236 F) and SpikeGadgets 128-channel Horizontal Headstage; custom probe interface PCB for electrical interconnect and alignment

## Materials & Fabrication
- **Structure:** SLA-printed resin body  
- **Hardware:** #0-80 fasteners and nuts; stainless-steel tube segment for lead screw access

## Validation & Performance
- **Stable use:** In-rig and in vivo use with stable recordings across 5 implants.

## Deployment & Status
- **Development:** completed, Feb 2023–Oct 2023
- **Deployment:** NC4 Lab, University of British Columbia
- **Status:** active, Oct 2023–present, NC4 Lab

## Release
- **CAD:** STEP files available in portfolio (see 3D Model Files)
- **On request:** assembly notes

## Licensing
- **Hardware:** CERN-OHL-W v2.0
- **Documentation:** CC BY 4.0

## Included files
*Attached on this page.*

### Image Files
- **render_1.png:** three-quarter view (front, left, top) render of housing and headstage
- **render_2.png:** three-quarter view (rear, right, top) render of connector side of housing
- **render_3.png:** three-quarter view (front, left, top) render with right-side housing removed to show interior
- **render_4_annotated.png:** annotated right view render with right-side housing removed to show interior
- **render_5.png:** exploded three-quarter view (front, left, top) render of all components
- **render_6.png:** right view render of the assembly mounted on a rat model at scale
- **photo_1.png:** bench photo of assembled housing, side view
- **photo_2.png:** bench photo of assembled housing, connector-side rear view 
- **photo_3.png:** bench photo of assembled housing, top view

### 3D Model Files
- **probe_housing_TOP_ASSY.step:** top-level assembly of the silicon probe microdrive housing
- **probe_housing_PART_housing_body_a.step:** part model of housing body A
- **probe_housing_PART_housing_body_b.step:** part model of housing body B
- **probe_housing_PART_housing_base.step:** part model of housing base

# Fischer 344 Rat Model

## Summary
To-scale 3D model of a Fischer 344 laboratory rat for design planning, visualization, and demonstration of behavioral systems; proportions match strain-specific morphology for accurate spatial layouts.

## Role & Contributions
- Designed in SolidWorks

## Release
- **CAD:** STEP file available in portfolio (see 3D Model Files)

## Licensing
- **Design files:** CC BY 4.0

## Included files
*Attached on this page.*

### Image Files
- **render_1.png:** three-quarter view (front, left, top) render of the rat model
- **render_2.png:** three-quarter view (rear, left, top) render of the rat model
- **render_3.png:** three-quarter view (rear, right, top) render of the rat model

### 3D Model Files
- **3d_rat_PART.step:** single-part rat model

# Wireless Mobile Feeder Robot

## Summary
A mobile feeder robot for delivering liquid rewards to rats during circular track experiments

## Description
This mobile feeder robot was designed for use with another portfolio project: the [Instantaneous Cue Rotation (ICR) Arena](https://www.cadcrowd.com/3d-models/instantaneous-cue-rotation-arena).

As part of the ICR Arena, the feeder robot tracks rats on a circular track and delivers precisely timed, spatially targeted liquid food rewards. Drive is provided by dual stepper motors, with an inner set of rollers riding in a groove along the inner track wall for guided motion.

The robot receives two streams of position information: an overhead camera that tracks both the rat and an onboard tracking LED on the robot to provide absolute poses in arena coordinates, and an onboard Pixy module that provides a local measurement of the rat’s position relative to the robot. Robot motion commands supply incremental odometry. All measurements are mapped into a track-aligned 1D coordinate (angular position along the circumference), with the robot’s pose from the LED-based overhead tracking used to correct the Pixy measurements.

An extended Kalman filter fuses overhead tracking data from the rat and robot (identified by red and green LEDs), Pixy, and odometry to estimate the rat’s angular position and velocity as well as the robot–rat offset. The controller maintains a fixed offset by regulating robot speed with a PID loop that tracks a commanded relative angle, closing the loop from sensing to state estimate to actuation.

IR proximity sensors mounted on the robot’s front provide safety guardrails and slow or stop motion if an unexpected obstacle is detected. Wireless commands and overhead tracking data are relayed through XBee-PRO Series 1 modules, and all control logic runs on an Arduino Due powered by an 11.1 V LiPo battery, eliminating the need for a commutator.

Liquid reward is dispensed from a feeder dish mounted on a retractable arm that extends 60 cm ahead of the robot along the inner track wall. In its default state the dish remains out of reach. During reward delivery, the dish pivots into position via a NEMA 14–driven pulley system using 1/16 in jacketed steel cable, illuminates a reward light, and dispenses liquid reward via a hydraulic solenoid valve. The fluid line and light lead run through steel conduit, and a second steel conduit carries a polymer-lined guide for the pivot cable. These conduits prevent rats from accessing and chewing through exposed lines.

To minimize odor and visual cues, a rear-mounted cleaning module continuously clears the track. A dual-shaft stepper motor drives the wheel from its front shaft and, via a 3D-printed elliptical-pulley belt drive on the rear shaft, actuates a neoprene flap that scoops debris into a trap. The elliptical pulleys impart a burst of speed at contact with the track surface so the flap knocks debris loose rather than smearing it. A polyurethane foam wiper is periodically wetted with ethanol from an onboard reservoir through a second hydraulic solenoid valve to keep the track clean. The entire rear cleaning assembly can be removed via a thumbscrew for cleaning.

## Role & Contributions
- Conceived, designed, and maintained end to end
- Fabricated and assembled key hardware
- Coordinated machining/fabrication of select parts
- Authored control software
- Designed and executed behavioral validation

## Highlights & Key Specs
- **Drive and motion:** stepper-motor-driven robot with wireless control and onboard microcontroller and 11.1 V power; commutator-free operation; embedded Arduino Due microcontroller and motor driver
- **Tracking:** dual-source tracking fused with an extended Kalman filter using overhead-camera and Pixy (CMUcam5) inputs for smooth position/velocity tracking
- **Reward delivery:** retractable feeder arm extends ~60 cm and pivots for access during reward; hydraulic solenoid valve dispenses liquid reward; synchronized event timestamps
- **Track cleaning:** Integrated track-cleaning module with neoprene flap and ethanol wiper to minimize odor and visual cues

## Materials & Fabrication
- **Body and mechanical structures:** hand-machined acrylic panels; CNC-milled UHMW polyethylene arm; hand-machined aluminum mounts and brackets
- **Drive and motion:** front NEMA 14 and rear dual-shaft NEMA 17 stepper motors with pulley drive; hand-lathed UHMW polyethylene inner guide rollers with 1/2 in bearings running in the wall groove
- **Actuation and fluidics:** Two Parker Series 3 miniature 2-way valves for reward delivery and ethanol dosing; food-grade silicone tubing; 3/16 and 3/8 in steel conduit; NEMA 11 stepper with hand-lathed UHMW polyethylene cable pulley for feeder-arm pivot attached to 1/16 in jacketed steel cable; hand-machined UHMW polyethylene feeder dish; FDM-printed polycarbonate elliptical timing pulley on the dual-shaft NEMA 17 rear shaft for flapper drive with GT2 belt
- **Sensing and control electronics:** Arduino Due main controller; STMicroelectronics L6470 AutoDriver stepper driver; XBee-PRO Series 1 wireless modules; Pixy (CMUcam5) vision module; Sharp GP2Y0D810Z0F IR proximity sensors
- **Power and switching:** 11.1 V LiPo battery (3S, ~6400 mAh class); Omron G3SD-Z01P-PD-US solid-state relay for solenoid activation
- **Fasteners and hardware:** standard metric fasteners, washers, springs, magnets, and aluminum posts; thread-lock on vibration-prone joints

## Validation & Performance
- **Behavioral performance:** Peer-reviewed methods paper documents apparatus and behavioral outcomes (see References)
- **Stable use:** Deployed in-rig and in vivo across 2 experiments

## Deployment & Status
- **Development:** completed, Aug 2015–May 2017
- **Deployment:** Barnes Lab, University of Arizona (2 studies)
- **Status:** retired, May 2017–Aug 2021, Barnes Lab

## Release
- **CAD:** full assembly STEP available in portfolio (see 3D Model Files)
- **Software:** 
  - Firmware repo: [https://github.com/adamwlester/icr-system](https://github.com/adamwlester/icr-system)
- **Related portfolio entry:** [Instantaneous Cue Rotation (ICR) Arena](https://www.cadcrowd.com/3d-models/instantaneous-cue-rotation-arena)

## Licensing
- **Hardware:** CERN-OHL-W v2.0
- **Software:** Apache-2.0
- **Documentation:** CC BY 4.0

## References
For additional details, see the published methods manuscript featuring this system and performance comparisons with an earlier fixed-feeder variant:
- Lester, A. W., Kapellusch, A. J., & Barnes, C. A. (2020). [A novel apparatus for assessing visual cue-based navigation in rodents](https://doi.org/10.1016/j.jneumeth.2020.108667). Journal of Neuroscience Methods, 338, 108667.

## Included files
*Attached on this page.*

### Image Files
- **render_1.png:** three-quarter view (front, right, top) render of feeder robot
- **render_2.png:** oblique view (right, top) render of robot and rat inside ICR arena
- **render_3.png:** top view render of robot and rat on track
- **render_4_annotated.png:** annotated top view render of feeder and rat
- **render_5_annotated.png:** annotated right view render of robot body
- **render_6_annotated.png:** annotated left view render of robot body
- **photo_1.png:** in-rig photo of assembled robot body on track
- **photo_2.png:** close-up photo of feeder dish and cue LED
- **photo_3.png:** close-up photo of dish-pivot stepper and pulley

### 3D Model Files
- **feeder_robot_TOP_ASSY.step:** top-level feeder robot assembly

# Adjustable Aluminum Projector Mount

## Summary
Adjustable aluminum projector mount for precise alignment of short-throw projectors in behavioral arenas.

## Description
This mount was designed for use with another portfolio project: the [Omniroute Maze System](https://www.cadcrowd.com/3d-models/omniroute-maze-system).

The mount provides independent height and yaw adjustment to align a short-throw projector for visual cue delivery on the Omniroute maze. A horizontal 80/20 1020 boom, attached to ceiling strut channels, connects to a vertical 80/20 1020 upright via a pair of 80/20 angle plates. Height is set by loosening the angle-plate fasteners, sliding the upright along the boom, then retightening.

At the projector end, a waterjet-cut three-plate yaw assembly provides ±30° rotation. The frame-mount plate carries a pivot plate with an arc slot and degree markings. The projector-interface plate clamps to the pivot assembly with three 1/4-20 wing-head thumb screws for toolless, secure, repeatable yaw adjustment. The projector-interface plate is drilled for the Mi 4K Laser Projector.

## Role & Contributions
- Conceived and developed all CAD models and assemblies
- Integrated with Omniroute system and maintained in routine use

## Highlights & Key Specs
- **Adjustments:** independent yaw via 1/4-20 wing-head thumb screws over ±30°; vertical adjustment along an 80/20 1020 T-slot rail
- **Mounting interface:** projector-interface plate drilled for Mi 4K Laser Projector; can be re-patterned for other models
- **Installation:** standard hand tools; toolless yaw; secure, repeatable adjustment

## Materials & Fabrication
- **Plates:** waterjet-cut 1/4 in 6061 aluminum with tapped holes
- **Rails:** 80/20 1020 T-slot extrusion (upright and boom)
- **Hardware:** 1/4-20 stainless fasteners with roll-in T-nuts; two 80/20 angle plates (4151); three 1/4-20 wing-head thumb screws

## Deployment & Status
- **Development:** completed, May 2022–Oct 2023
- **Deployment:** NC4 Lab, University of British Columbia (3 studies)
- **Status:** active, Oct 2023–present, NC4 Lab

## Release
- **CAD:** select STEP files available in portfolio (see 3D Model Files)
- **On request:** additional design files
- **Related portfolio entry:** [Omniroute Maze System](https://www.cadcrowd.com/3d-models/omniroute-maze-system)

## Licensing
- **Hardware:** CERN-OHL-W v2.0
- **Documentation:** CC BY 4.0

## References
For additional details, see the preprint methods article for the Omniroute system, which featured this component:
- Lester, A. W., Mombeini, A. G., & Madhav, M. S. (2025). [The Omniroute maze: a novel rodent navigation apparatus that integrates dynamically configurable routes, sensory cues, and automated reward delivery](https://www.biorxiv.org/content/10.1101/2025.09.01.672969v1). bioRxiv.

## Included files
*Attached on this page.*

### Image Files
- **render_1.png:** three-quarter view (rear, right, top) render of projector mount with projector
- **render_2.png:** right view render of projector mount with projector
- **render_3.png:** exploded three-quarter view (rear, right, top) render of projector mount with projector
- **photo_1.png:** in-rig close-up photo of one installed projector mount
- **photo_2.png:** in-rig photo of four installed projector mounts in NC4 Lab Omniroute system

### 3D Model Files
- **projector_mount_TOP_ASSY.step:** top-level assembly of adjustable aluminum projector mount for 1020 rail
- **projector_mount_SUB_pivot.step:** pivot subassembly with yaw plate and slotted clamp hardware

# Two-Axis Feeder Gantry

## Summary
CNC-based gantry system for automated spatially targeted reward delivery in rodent open-field experiments.

## Description
This reward delivery system was designed for use with another portfolio project: the [Omniroute Maze System](https://www.cadcrowd.com/3d-models/omniroute-maze-system).

The gantry provides spatially targeted liquid reward by tracking animal movement within the Omniroute maze while simultaneously carrying a ceiling panel that prevents rats from climbing maze walls and houses a retractable feeder arm that can be rotated down to the maze floor for reward delivery. Motion control is handled by an OpenBuilds BlackBox X32 running GRBL and integrated with the Omniroute ROS stack for command, coordination, and tracking.

**Frame and motion platform:** The translation stage follows the OpenBuilds ACRO architecture with V-slot extrusion (20 × 40 mm profile), Delrin V-wheels, GT2 belts, and NEMA 17 steppers. The assembled stage has a footprint of 2.2 × 1.4 m (X, Y) and provides 1.6 × 0.8 m of usable travel. Enclosed cable carriers on the X and Y axes route wiring. Custom laser-cut motor and guide plates in 1/4 in high-impact acrylic provide stiff mounting for motors, idlers, and cable-chain anchors, and create direct interfaces to the cover carriage frame. The design leverages the ACRO stage format and select OpenBuilds components for the linear motion subsystem, while the mechanical interfaces, controller integration, platework, and fixtures are all customized to meet Omniroute’s geometry and the additional cover carriage and feeder arm functionality.

**Gantry cover carriage:** An approximately 60 × 60 cm carriage built from 10 × 10 mm lightweight aluminum extrusions carries a clear acrylic panel that acts as a moving ceiling to block climbing. The carriage includes printed brackets for the cover panel and support plates for guide wheels, plus integrated mounts for the liquid food reward vial, peristaltic pump, and feeder arm assembly (including the Z-axis motor, pulley posts, and limit-switch hardware). The frame geometry and component placement are tuned to maintain maze-wall clearance, keep high-visibility hardware away from the center of the animal’s sightlines, and avoid occlusion of the projected wall and floor stimuli used in the Omniroute maze.

**Feeder arm:** A retractable feeder arm assembly is mounted on the carriage and operates as a Z-axis accessory that rotates down to deliver liquid reward at a commanded XY location, then retracts to a parked position above the cover panel. Z motion is driven by a fourth NEMA 17 stepper on the motion controller Z channel through a timing-belt train with custom SLA-printed pulleys that couple the motor to the feeder arm. A small pulley-mounted cam actuates a lever-style limit switch at the fully retracted position, enabling reliable homing and interlocks. The dispensing arm uses a 1/4 in stainless-steel tube with a custom SLA angle connector joined to a flexible extension spring forming the short leg of the L-arm. A continuous silicone line runs from the pump through the tube and connector to the arm terminus. This linkage uses a doubled effective gear ratio to provide sufficient force margin to retract even if a rat hangs on it. The flexible arm end is designed to protect animals and maze walls if the arm contacts a rat during lowering or the gantry resumes movement before retracting.

**Design revision:** Upgraded to a stepper-driven actuator with integrated limit switch detection, replacing the original servo. The design is complete and being integrated into the assembly. The revised arm has stiffer components and a flexible end.

## Role & Contributions
- Conceived, designed, built, and maintained end to end
- Developed all CAD models and assemblies
- Led mechanical and electrical build team
- Authored firmware and PC software
- Designed and executed validation
- Primary maintainer

## Highlights & Key Specs
- **Footprint:** 2.2 × 1.4 m (X, Y) frame envelope
- **Travel:** 1.6 × 0.8 m (X, Y) commanded range
- **Carriage capacity:** 60 × 60 cm cover area
- **Motion performance:** peak traverse speed: 0.47 m/s

## Materials & Fabrication
- **Frame and motion platform:** V-slot 20 × 40 mm extrusion; laser-cut 1/4 in high-impact acrylic motor and guide plates; GT2 belts and idlers; NEMA 17 steppers; OpenBuilds BlackBox X32 motion controller and Xtension Limit Switches
- **Gantry cover assembly:** laser-cut 1/16 in clear acrylic panel; laser-cut 1/4 in high-impact acrylic motor, guide, and mounting plates; 10 × 10 mm aluminum T-slot extrusion frame
- **Feeder arm:** NEMA 17 stepper; SLA-printed timing pulleys; GT2 belt; E-Switch limit switch (MS0850503F025C1C); 1/4 in stainless-steel tube; 1/4 in extension spring
- **Pump and lines:** Gravity Digital Peristaltic Pump (DFRobot DFR0523); food-grade silicone tubing; glass vial reservoir

## Validation & Performance
- **Traverse speed:** peak 0.47 m/s; mean 0.21 m/s  
- **Arrival latency:** 1.5 s to within 2 cm over a 0.43 m move  
- **Positional accuracy:** 0.7 cm final error at stop  
- **Acoustic profile:** +20 dB SPL during motion vs idle

## Deployment & Status
- **Development:** v1 developed, Jan 2023–Sep 2023; feeder arm v2 integration, Jun 2025–present
- **Deployment:** NC4 Lab, University of British Columbia (3 studies)
- **Status:** active, Sep 2023–present, NC4 Lab

## Release
- **CAD:** select STEP files available in portfolio (see 3D Model Files)
- **Software:**
- ROS workspace (Ubuntu): [https://github.com/NC4Lab/omniroute_ubuntu_ws](https://github.com/NC4Lab/omniroute_ubuntu_ws)
- ROS workspace (Windows): [https://github.com/NC4Lab/omniroute_windows_ws](https://github.com/NC4Lab/omniroute_windows_ws)
- **On request:** additional design files
- **Related portfolio entry:** [Omniroute Maze System](https://www.cadcrowd.com/3d-models/omniroute-maze-system)

## Licensing
- **Hardware:** CERN-OHL-W v2.0
- **Software:** Apache-2.0
- **Documentation:** CC BY 4.0

## References
For additional details, including system performance tests, see the preprint methods manuscript for the Omniroute maze, which features this subsystem:
- Lester, A. W., Mombeini, A. G., & Madhav, M. S. (2025). [The Omniroute maze: a novel rodent navigation apparatus that integrates dynamically configurable routes, sensory cues, and automated reward delivery](https://www.biorxiv.org/content/10.1101/2025.09.01.672969v1). bioRxiv.

## Included files
*Attached on this page.*

### Image Files
- **diagram_1.png:** annotated top view diagram of gantry layout and travel
- **diagram_2.png:** annotated top and side view diagram of feeder arm assembly
- **render_1.png:** three-quarter view (front, left, top) render of full feeder gantry
- **render_2.png:** top view render of full feeder gantry
- **render_3.png:** top view render of cover carriage with feeder arm
- **render_4.png:** three-quarter view (front, right, top) render of cover carriage with feeder arm
- **render_5.png:** three-quarter view (front, right, top) render of feeder arm assembly, close-up
- **photo_1.png:** On-rig photo of the feeder gantry installed on the Omniroute system; legacy servo-driven feeder arm
- **photo_2.png:** On-rig top view of the cover carriage over the Omniroute system; legacy servo-driven feeder arm

### 3D Model Files
- **feeder_gantry_TOP_ASSY.step:** top-level assembly of full feeder gantry
- **feeder_gantry_SUB_cover_carriage.step:** cover carriage subassembly with feeder arm

# NC4gate Automatable Gate Module

## Summary
Modular motorized gate system for autonomous control of rodent behavior in maze experiments.

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
- **Envelope:** 117 × 86 × 290 mm (gate lowered)
- **Gate travel:** 180 mm total
- **Typical actuation time:** ~578 ms up, ~531 ms down
- **Endurance:** thousands of cycles; individual modules tested up to 100,000 cycles
- **Control scale:** up to 512 gates from a single PC and microcontroller
- **Interfaces:** Qt-based GUI for manual operation; Python API for programmatic control

## Materials & Fabrication
- **Structure:** laser-cut POM-C acetal (3.175 mm) with snap-fit features and minimal fasteners
- **Actuation:** 12 V 50 RPM DC gear motor (37 mm can) driving pin-in-slot linkage
- **Linkage:** waterjet-cut aluminum arm for durability under repeated cycling
- **Sensing:** upper and lower limit switches for hard-stop detection
- **Hardware:** standard fasteners, spacers, rollers; cable ties and strain relief provisions

## Validation & Performance
- **Actuation latency:** tests on N=5 modules across 50 cycles each show consistent latencies: upward ~578 ms and downward ~531 ms, suitable for behavioral control
- **Stress testing:** long operational life up to 100,000 cycles, with field-repairable failure modes (motor wear, linkage retention, wiring); 60-module system running near-daily for over one year

## Deployment & Status
- **Development:** completed, Dec 2021–Sep 2023
- **Deployment:** NC4 Lab, University of British Columbia (3 studies)
- **Status:** active, Sep 2023–present, NC4 Lab	

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

# Track-Mounted Feeder Cart

## Summary
Mobile feeder cart for controlled on-track liquid reinforcement with gated feeder access for rodent circular track experiments

## Description
This mobile feeder cart maintains a fixed offset to a rat running on a circular track and dispenses liquid rewards through a servo-gated feeder port, enabling continuous reinforcement while constraining the animal’s movement options.

The cart uses waterjet-cut 1/16 in clear polycarbonate panels and 1/8 in 6061 aluminum plate, with SLA-printed brackets and standard fasteners throughout for easy replication and repair.

A 3D-printed feeder port is supplied by a peristaltic pump via 1/16 in ID food-grade silicone tubing. Access to the port is controlled by a compact micro-servo-actuated vertical gate that can fully block or expose the port. An infrared (IR) break-beam across the port detects nose-in for precise dosing and event logging. Alternate feeder ports at either end of the cart can be used to drop rewards onto the track ahead of or behind the rat via a quick-disconnect tube fitting.

The cart integrates an overhead tether guide for wired electrophysiology that rides on a curved rail above the track. A low-friction trolley with five adjustable 1/4 in roller bearings keeps the cable centered over the animal and travels with the cart.

A microcontroller controls the pump, gate, and sensors, while a central drive motor rotates the cart assembly to track the rat’s position.

Drive is provided from a central pillar assembly at the platform center; the motor’s torque is transmitted via two 0.25 in coupling rods linking the central pillar to the cart’s drive interface. The central pillar incorporates alignment and load-bearing components (timing-belt pulleys, quick-disconnect bushing, sealed ball and thrust bearings) to ensure smooth rotation and a serviceable setup.

This feeder cart was designed for use with the Dome system, a rodent augmented-reality apparatus in which visual stimuli are projected onto the inside of a circular dome surrounding a circular track. The updated cart design retains compatibility with the Dome system while adding modular features like the feeder port, improved access control, and streamlined fabrication.

## Role & Contributions
- Conceived, designed, and fabricated the system
- Developed all CAD models and assemblies
- Primary maintainer

## Highlights & Key Specs
- **Drive and motion:** Central pillar drive with two 0.25 in coupling rods for smooth rotation and fixed-offset tracking
- **Access control:** Micro-servo-actuated vertical gate with repeatable full block/expose states
- **Reward delivery:** Peristaltic pump with food-grade silicone lines; quick-disconnect forward/rear drop ports
- **Detection and timing:** IR break-beam at port for nose-in timestamping and precise dosing
- **Ephys support:** Overhead tether guide with low-friction trolley and commutator integration

## Materials & Fabrication
- **Frame and panels:** Waterjet-cut 1/16 in clear polycarbonate side walls and end plates, and 1/8 in 6061 aluminum frame members
- **Drive and motion:** Central pillar assembly, two 0.25 in coupling rods, sealed ball bearings, threaded track roller
- **Feeder and gate:** SLA-printed feeder port and gate arm, bottle holder and mount; Takasago RP-CIII series peristaltic pump, 9 g micro servo, Adafruit IR break-beam sensor 2167, 1/16 in ID food-grade silicone tubing
- **Tether guide:** SLA-printed tether-roller housing; waterjet-cut 1/8 in 6061 aluminum curved guide components; five 1/4 in roller bearings

## Validation & Performance
- **Stable use:** In-rig and in vivo use with stable operation for 2 experiments

## Deployment & Status
- **Development:** completed, Feb 2024–Mar 2024
- **Deployment:** NC4 Lab, University of British Columbia (2 studies)
- **Status:** active, Mar 2024–present, NC4 Lab

## Release
- **CAD:** STEP files available in portfolio (see 3D Model Files)
- **On request:** assembly notes; additional design files

## Licensing
- **Hardware:** CERN-OHL-W v2.0
- **Documentation:** CC BY 4.0

## References
The original Dome system and cart design that this version was adapted from are described in detail in the following methods article:
- Madhav, M. S., Jayakumar, R. P., Lashkari, S. G., Savelli, F., Blair, H. T., Knierim, J. J., & Cowan, N. J. (2022). The Dome: a virtual reality apparatus for freely locomoting rodents. Journal of Neuroscience Methods, 368, 109336.

## Included files
*Attached on this page.*

### Image Files
- **render_1.png:** three-quarter view (front, right, top) render of track-mounted feeder cart installed on Dome system platform
- **render_2_annotated.png:** annotated three-quarter view (front, right, top) render of feeder cart system components
- **render_3_annotated.png:** annotated three-quarter view (front, right, top) render of gated feeder port, close-up
- **render_4.png:** right cross-section view render of gated feeder port, gate open
- **render_5.png:** right cross-section view render of gated feeder port, gate closed
- **render_6.png:** three-quarter view (front, left, top) render of tether guide clamp, close-up
- **photo_1.png:** bench photo of prototype track-mounted feeder cart assembly
- **photo_2.png:** combined bench close-up photos of gated feeder port, open and closed

### 3D Model Files
- **feeder_cart_TOP_ASSY.step:** top-level assembly of track-mounted feeder cart
- **feeder_cart_SUB_gated_port.step:** gated feeder port subassembly with servo, gate, and IR sensors
- **feeder_cart_SUB_tether_guide.step:** tether guide clamp subassembly for overhead rail

# Instantaneous Cue Rotation (ICR) Arena

## Summary
An augmented reality behavioral arena for studying cue-based navigation in freely moving rats.

## Description
The Instantaneous Cue Rotation (ICR) Arena is an augmented-reality rodent behavioral arena enabling instantaneous rotation of all orienting visual cues during ongoing navigation with extracellular electrophysiology recordings. The 1.4 m diameter circular track is enclosed by 68 cm tall rear-projection panels that form a seamless 360° panorama of visual cues. Four short-throw projectors render these cues and can rotate them remotely and instantaneously without removing the animal from the track to assess their effect on navigation accuracy. A mobile feeder robot tracks the rat to deliver food-based reinforcement, which is featured as a separate portfolio entry ([Wireless Mobile Feeder Robot](https://www.cadcrowd.com/3d-models/feeder-robot)). All static elements within the behavioral space are repeated every 10° to eliminate symmetry-breaking spatial cues. The structure uses 80/20 aluminum extrusion with ESD-coated acrylic and PVC foam board for durability and electrophysiology compatibility. The assembly is suspended from ceiling strut channels to keep the interior clear and allow access from below. An overhead speaker, recessed into the ceiling, delivers auditory cues and continuous white noise to mask potential orienting sounds that could conflict with the cue manipulation. Below this, a centrally mounted commutator with a drop-down boom arm keeps the tether aligned directly above the circular track for wired electrophysiology. Two overhead color cameras are offset to either side of the commutator to maintain coverage when either camera’s line of sight is occluded by the boom arm and provide continuous tracking data for the rat and feeder robot. The floor of the arena can be lowered via gas springs and pulleys to allow easy access to the base for cleaning and maintenance.

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
- **Arena:** 1.4 m diameter circular track; 68 cm projection walls; track can be accessed from underneath for training or lowered via gas springs and pulleys to allow easy access to the base for cleaning
- **Visual stimulus system:** four short-throw projectors (BenQ MW621ST) with instantaneous remote cue rotations
- **Synchronization and I/O:** Arduino Due controllers; NeuraLynx Digital Lynx SX integration; phototransistor-triggered TTL, millisecond-precision timestamps for cue-change alignment 
- **Reward and tracking:** Mobile feeder robot with XBee-PRO wireless and LiPo power; retractable liquid-reward dish; fused overhead camera and Pixy-based position tracking
- **Software stack:** MCU firmware in C/C++; C# wireless data interface; MATLAB control and analysis frontend and GUI
- **Acoustic control:** Continuous white noise to mask orienting auditory cues and optional sound cues

## Materials & Fabrication
- **Structure:** 80/20 aluminum extrusion frame; acrylic and PVC foam board; FlexGlass projection surface for rear projection
- **Electronics:** Arduino Due microcontrollers; NeuraLynx Digital Lynx SX; phototransistors; XBee-PRO Series 1 radios; LiPo battery system; Pixy vision module

## Validation & Performance
- **Behavioral performance:** Peer-reviewed methods paper documents apparatus and behavioral outcomes (see References)
- **Stable use:** In-rig and in vivo use across 2 experiments

## Deployment & Status
- **Development:** completed, Aug 2013–May 2017
- **Deployment:** Barnes Lab, University of Arizona (2 studies)
- **Status:** active, May 2017–present, Barnes Lab

## Release
- **CAD:**
  - ICR: full assembly STEP available in portfolio (see 3D Model Files)
  - Mobile feeder robot: see portfolio entry “[Wireless Mobile Feeder Robot](https://www.cadcrowd.com/3d-models/feeder-robot)”
- **Software:**
  - Firmware and software repo: [https://github.com/adamwlester/icr-system](https://github.com/adamwlester/icr-system)

## Licensing
- **Hardware:** CERN-OHL-W v2.0
- **Software:** Apache-2.0
- **Documentation:** CC BY 4.0

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

# Omniroute Maze System

## Summary
A dynamically reconfigurable rodent maze system that integrates automated route configurations, sensory cue control, and targeted reward delivery.

## Description
The Omniroute maze measures 90 × 90 cm and is organized as a 3 × 3 grid of chambers separated by 60 movable gates, which are featured as a separate portfolio entry ([NC4gate Automatable Gate Module](https://www.cadcrowd.com/3d-models/modular-gate-mechanism)). Each gate module, detailed in a separate project, can be raised or lowered programmatically to define unique routes in real time. The system also incorporates a CNC feeder gantry for spatially targeted liquid reward delivery, also featured as a separate portfolio entry ([Two-Axis Maze Feeder Gantry](https://www.cadcrowd.com/3d-models/modular-gate-mechanism)). Four short-throw projectors arrayed around the maze deliver dynamic visual cues onto the gate walls or maze floor as well as directional auditory cues. All components are designed and tested for compatibility with high-density electrophysiological recordings and closed-loop experimental paradigms.

Maze construction combines 80/20 aluminum extrusion for the structural frame, laser-cut POM-C acetal for the gate modules, and CNC-milled PVC foam board for the platform. The modular design allows rapid assembly, easy replacement of components, and scaling to different experimental configurations.

The system is controlled via the Robot Operating System (ROS) with custom nodes and Python/C++ libraries for gate actuation, GRBL-controlled gantry motion, and OpenGL-based cue projection and geometric transforms. Nodes communicate via ROS topics, services, and actions; device I/O uses serial, I²C, and PWM. Gates are driven by 12 V DC gearmotors via custom DRV8870 motor-driver PCBs, networked over I²C to Cypress I/O expander boards, enabling control of up to 512 gates from a single Arduino Mega. A high-speed 3D tracking pipeline streams pose to ROS at >100 Hz, enabling real-time closed-loop control of visual cues and reward delivery.

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
- **Platform:** 90 × 90 cm with 3 × 3 chamber grid; 60 independently motorized gates
- **Cues:** four short-throw projectors with integrated speakers for dynamic visual and auditory stimuli
- **Reward:** XY gantry for spatially targeted liquid reward anywhere on the platform
- **Tracking:** real-time 3D pose of animal and gantry; closed-loop task control
- **System timing:** sub-second round-trip latencies for gates, projection, and audio as characterized in the preprint
- **Gantry performance:** centimeter-scale targeting accuracy with smooth velocity profiles

## Materials & Fabrication
- **Frame:** 80/20 aluminum T-slot extrusion
- **Platform:** CNC-milled foam PVC with integrated module slots and inserts
- **Gates:** laser-cut POM-C acetal modules with 12 V DC gearmotors, pin-in-slot linkage, and top/bottom limit switches
- **Electronics:** custom DRV8870 motor driver PCBs; Cypress I/O expanders on I²C; Arduino Mega control
- **Projector mounts:** waterjet-cut aluminum brackets with yaw and height adjustment
- **Gantry:** OpenBuilds-style V-slot rails, NEMA 17 steppers, GT2 belts; laser-cut acrylic roller plates, motor plates, and overhead panel; SLA-printed resin brackets and reward feeder assembly

## Validation & Performance
- **System latency:** sub-second gate actuation, projection updates, and audio playback  	
- **Gantry accuracy:** reliable centimeter-scale arrival to commanded targets in gantry tests  
- **Electrophysiology compatibility:** no movement-locked electrical artifacts during gate or gantry actuation  
- **Behavioral performance:** above-chance task accuracy with projected cues and wall configurations

## Deployment & Status
- **Development:** v1 developed, Dec 2021–Sep 2023; feeder-gantry subsystem enhancements, Jun 2025–present
- **Deployment:** NC4 Lab, University of British Columbia (3 studies)
- **Status:** active, Sep 2023–present, NC4 Lab

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

## Licensing
- **Hardware:** CERN-OHL-W v2.0
- **Software:** Apache-2.0
- **Documentation:** CC BY 4.0

## References
For additional details, including system performance tests, rodent behavior, and detailed schematics, see the preprint methods manuscripts for the Omniroute and the associated NC4gate system:
- Lester, A. W., Mombeini, A. G., & Madhav, M. S. (2025). [The Omniroute maze: a novel rodent navigation apparatus that integrates dynamically configurable routes, sensory cues, and automated reward delivery](https://www.biorxiv.org/content/10.1101/2025.09.01.672969v1). bioRxiv.
- Lester, A. W., Kaur, G., Djafri, N., & Madhav, M. S. (2024). [A modular gate system for autonomous control of rodent behavior](https://www.biorxiv.org/content/10.1101/2024.11.22.624912v1). bioRxiv.

## Included files
*Attached on this page.*

### Image Files
- **render_1.png:** three-quarter view (front, left, top) render of full Omniroute system with projected floor and wall cues
- **render_2_annotated.png:** annotated oblique view (front, top) render of full Omniroute system
- **render_3.png:** three-quarter view (front, left, top) render of feeder gantry and maze platform
- **render_4.png:** top view render of feeder gantry and maze platform
- **render_5.png:** top view render of maze platform with projected stimuli
- **render_6.png:** three-quarter view (front, right, top) render of maze platform with NC4gate modules
- **system_diagram.png:** system architecture diagram
- **photo_1.png:** combined in-rig photos of ceiling and floor components of the Omniroute system
- **photo_2.png:** combined in-rig photos of example wall and floor projected stimuli

### 3D Model Files
- **omniroute_SUB_gates_and_platform.step:** subassembly of maze platform with NC4gate modules
- **omniroute_SUB_feeder_gantry.step:** subassembly of feeder gantry
- **omniroute_SUB_projector_mount.step:** subassembly of adjustable projector mount

# NC4touch Behavioral Apparatus

## Summary
Touchscreen-based behavioral apparatus for flexible, high-throughput cognitive testing with mice and rats.

## Description
NC4touch is a three-screen, Raspberry Pi-controlled chamber with calibrated liquid-reward delivery, overhead video tracking, sensory cue delivery, and modular device I/O for flexible, high-throughput cognitive testing in mice and rats.

The enclosure consists of a trapezoidal workspace with three touchscreens at the front and a food-reward dispensing system in the rear. The frame uses 10 × 10 mm aluminum T-slot extrusion with SLA-printed brackets and mounts, and laser-cut acetal panels for the enclosure and electronics bays, keeping the electronics fully separated from the behavioral space.

A USB camera mounted above the system captures the full field of view, and removable, laser-cut, 3/16 in clear acrylic lid and floor panels provide visibility and can be easily removed to aid wipe-down cleaning.

The front panel includes three capacitive touchscreens, each with a cue RGB LED and a buzzer for trial timing and feedback. Each screen is driven by a dedicated FireBeetle 2 M0 microcontroller over a single GDI ribbon cable, with USB used for command and data. Using a dedicated controller per display lets the screens load and render images in parallel, so updates do not block each other and refresh times stay fast under load. Because rodents can behave like a floating ground, a thin copper-foil-laminated floor panel beneath the screens nests into the removable acrylic floor but stays attached to the frame to keep the ground path intact.

The rear panel integrates a 3D-printed feeder port assembly with IR sensors, a stainless-steel lick spout, and a panel-mount cue RGB LED. A peristaltic pump with a dual-motor controller provides calibrated liquid rewards via food-grade silicone tubing. The IR break-beam detects nose-in and feeder occupancy for precise dosing and event logging. All tubing, port components, and the spout are quick to remove for cleaning, with standard fittings and clear service access.

A Raspberry Pi manages task state, device I/O, and logging. The Pi sends image commands to each display module via their microcontroller, controls both cue LEDs and the buzzer, and commands pump dosing. It receives touch events from all three screens and feeder IR signals, and timestamps these alongside the video stream from the overhead camera. Data are written to disk as compact CSV logs plus an optional frame-synchronized MP4 file to support reproducible analysis.

Single- or multi-chamber operation is supported. A single Raspberry Pi can run one or multiple daisy-chained chambers. Multi-chamber setups can be networked over Ethernet with a lightweight browser UI for monitoring and control. Optional PoE provides single-cable power and data to reduce clutter and simplify installation.

Mechanical and electrical design emphasize maintainability and replication. Panels are flat-pattern, laser-cut parts with captive fasteners where appropriate. 3D-printed brackets localize loads and register panel geometry. All external connectors are panel-mount for strain relief and quick replacement. Front and rear electronics bays are isolated from the behavioral space to protect components and simplify wipe-down.

## Role & Contributions
- Co-conceived and architected the system 
- Developed all CAD models and assemblies
- Led teams for mechanical build, embedded integration, and validation
- Contributed to control firmware
- Primary hardware maintainer

## Highlights & Key Specs
- **Workspace:** trapezoidal chamber with isolated electronics bays; removable clear acrylic lid and floor for wipe-down cleaning
- **Displays:** three 3.5 in 320 × 480 capacitive touchscreens, each driven by a microcontroller over a GDI ribbon cable, with USB for command and data
- **Control:** Raspberry Pi 4 with PoE; single- or multi-chamber orchestration via browser UI; unified I/O and logging
- **Cue delivery:** RGB indicators on the front and rear interior faces plus a buzzer for behavioral feedback
- **Tracking:** 8 MP USB overhead camera covering the full field of view
- **Reward:** IR break-beam for reward timing and logging, and a quick-service fluid path
- **Data:** CSV logs and optional synchronized MP4 with millisecond event timestamps

## Materials & Fabrication
- **Frame:** miniature T-slotted aluminum extrusion (McMaster 5969N16) with associated T-nuts and fasteners; custom SLA-printed frame-to-panel joining brackets
- **Enclosure and electronics bays:** laser-cut POM-C (acetal) sidewalls and electronics panels; laser-cut clear acrylic top, floor, and grounding panel; SLA-printed brackets for panel registration and service access; SLA-printed clips and cable mounts
- **Displays and controllers:** three capacitive touchscreens (DFRobot Fermion DFR0669) with associated FireBeetle 2 M0 (DFR0652) development board controllers
- **Cue delivery:** four Dialight 8 mm RGB panel indicators (6201121317F) and a Gravity digital buzzer (DFR0032)
- **Camera:** DFRobot 8 MP USB camera (FIT0729) with dedicated SLA-printed camera mount assembly
- **Feeder system:** SLA-printed feeder port assembly; Adafruit IR break-beam sensor (2167); TFS RP-CIII ring pump; stainless-steel tubing, food-grade silicone tubing, and glass vials

## Validation & Performance
- **Bench validation:** end-to-end verification of touch detection, cue LEDs and buzzer, pump dosing, and synchronized video plus CSV logging on single- and multi-chamber setups using the browser UI and PoE  
- **Timing and data integrity:** frame-aligned MP4 confirmed millisecond event–video alignment; chambers wrote synchronized session logs to shared storage  
- **Networked operation:** multi-chamber control over Ethernet with shared code, firmware, and image directories; no desynchronization observed during concurrent runs
- **Behavioral performance:** all three rats completed an eight-stage visual discrimination task with stage-wise performance gains, meeting the ≥77 percent correct advancement criterion at each stage

## Deployment & Status
- **Development:** completed, Sep 2023–Nov 2024
- **Deployment:** 
  - NC4 Lab, University of British Columbia (2 studies, 4 rigs)
  - Snyder Lab, University of British Columbia (1 study, 2 rigs)
- **Status:** active, Nov 2024–present, NC4 Lab

## Release
- **CAD:** 
  - Design files including SolidWorks assemblies and parts, cutting templates, and documentation: [https://osf.io/8q9tk](https://osf.io/8q9tk)
- **Software:** 
  - Firmware and software repo: [https://github.com/NC4Lab/TouchscreenApparatus](https://github.com/NC4Lab/TouchscreenApparatus)
- **On request:** additional design files; assembly notes

## Licensing
- **Hardware:** CERN-OHL-W v2.0
- **Software:** Apache-2.0
- **Documentation:** CC BY 4.0

## References
For additional details, see:
- Modara, G., Lester, A. W., Schwein, I., & Madhav, M. S. (2025). NC4touch: An open-source modular touchscreen apparatus for rodent behavioral testing. bioRxiv. [link pending]

## Included files
*Attached on this page.*

### Image Files
- **render_1.png:** oblique view (right, top) render of full NC4touch behavioral apparatus including exposed interior
- **render_2_annotated.png:** annotated oblique view (front, right) render of interior touchscreen end of apparatus
- **render_3_annotated.png:** annotated front view render of electronics bay on touchscreen side of apparatus
- **render_4_annotated.png:** annotated oblique view (rear, right) render of interior feeder port end of apparatus
- **render_5_annotated.png:** annotated rear view render of electronics bay on feeder port end of apparatus
- **photo_1.png:** bench photo of full NC4touch behavioral apparatus
- **photo_2.png:** bench close-up photo of interior touchscreen end of apparatus
- **photo_3.png:** bench close-up photo of interior feeder port end of apparatus

### 3D Model Files 
- **nc4touch_TOP_ASSY.step:** top-level assembly of NC4touch behavioral apparatus with enclosing panels hidden 
- **nc4touch_SUB_feeder_port.step:** feeder port subassembly with IR sensors

