---
layout: project-detail-page
title: "Wireless Mobile Feeder Robot"
summary: "A mobile feeder robot for delivering liquid rewards to rats during circular track experiments"
hero: "images/render_1.png"
model: "models/wireless-mobile-feeder-robot.glb"
images:
  - src: "images/render_1.png"
    caption: "three-quarter view (front, right, top) render of feeder robot"
  - src: "images/render_2.png"
    caption: "oblique view (right, top) render of robot and rat inside ICR arena"
  - src: "images/render_3.png"
    caption: "top view render of robot and rat on track"
  - src: "images/render_4_annotated.png"
    caption: "annotated top view render of feeder and rat"
  - src: "images/render_5_annotated.png"
    caption: "annotated right view render of robot body"
  - src: "images/render_6_annotated.png"
    caption: "annotated left view render of robot body"
  - src: "images/photo_1.png"
    caption: "in-rig photo of assembled robot body on track"
  - src: "images/photo_2.png"
    caption: "close-up photo of feeder dish and cue LED"
  - src: "images/photo_3.png"
    caption: "close-up photo of dish-pivot stepper and pulley"
---

<div class="content-groups">
<div class="content-group content-group-primary" markdown="1">

## Description

This mobile feeder robot was designed for use with another portfolio project: the [Instantaneous Cue Rotation Arena](https://www.cadcrowd.com/3d-models/instantaneous-cue-rotation-arena).

As part of the ICR Arena, the feeder robot tracks rats on a circular track and delivers precisely timed, spatially targeted liquid food rewards. Drive is provided by dual stepper motors, with an inner set of rollers riding in a groove along the inner track wall for guided motion.

The robot receives two streams of position information: an overhead camera that tracks both the rat and an onboard tracking LED on the robot to provide absolute poses in arena coordinates, and an onboard Pixy module that provides a local measurement of the rat’s position relative to the robot. Robot motion commands supply incremental odometry. All measurements are mapped into a track-aligned 1D coordinate (angular position along the circumference), with the robot’s pose from the LED-based overhead tracking used to correct the Pixy measurements.

An extended Kalman filter fuses overhead tracking data from the rat and robot (identified by red and green LEDs), Pixy, and odometry to estimate the rat’s angular position and velocity as well as the robot–rat offset. The controller maintains a fixed offset by regulating robot speed with a PID loop that tracks a commanded relative angle, closing the loop from sensing to state estimate to actuation.

IR proximity sensors mounted on the robot’s front provide safety guardrails and slow or stop motion if an unexpected obstacle is detected. Wireless commands and overhead tracking data are relayed through XBee-PRO Series 1 modules, and all control logic runs on an Arduino Due powered by an 11.1 V LiPo battery, eliminating the need for a commutator.

Liquid reward is dispensed from a feeder dish mounted on a retractable arm that extends 60 cm ahead of the robot along the inner track wall. In its default state the dish remains out of reach. During reward delivery, the dish pivots into position via a NEMA 14–driven pulley system using 1/16 in jacketed steel cable, illuminates a reward light, and dispenses liquid reward via a hydraulic solenoid valve. The fluid line and light lead run through steel conduit, and a second steel conduit carries a polymer-lined guide for the pivot cable. These conduits prevent rats from accessing and chewing through exposed lines.

To minimize odor and visual cues, a rear-mounted cleaning module continuously clears the track. A dual-shaft stepper motor drives the wheel from its front shaft and, via a 3D-printed elliptical-pulley belt drive on the rear shaft, actuates a neoprene flap that scoops debris into a trap. The elliptical pulleys impart a burst of speed at contact with the track surface so the flap knocks debris loose rather than smearing it. A polyurethane foam wiper is periodically wetted with ethanol from an onboard reservoir through a second hydraulic solenoid valve to keep the track clean. The entire rear cleaning assembly can be removed via a thumbscrew for cleaning.

## Validation & Performance

**Behavioral performance:**  
Peer-reviewed methods paper documents apparatus and behavioral outcomes (see References)  

**Stable use:**  
Deployed in-rig and in vivo across 2 experiments  

## Materials & Fabrication

**Body and mechanical structures:**  
- Hand-machined acrylic panels  
- CNC-milled UHMW polyethylene arm  
- Hand-machined aluminum mounts and brackets  

**Drive and motion:**  
- Front NEMA 14 and rear dual-shaft NEMA 17 stepper motors with pulley drive  
- Hand-lathed UHMW polyethylene inner guide rollers with 1/2 in bearings running in the wall groove  

**Actuation and fluidics:**  
- Two Parker Series 3 miniature 2-way valves for reward delivery and ethanol dosing  
- Food-grade silicone tubing  
- 3/16 and 3/8 in steel conduit  
- NEMA 11 stepper with hand-lathed UHMW polyethylene cable pulley for feeder-arm pivot attached to 1/16 in jacketed steel cable  
- Hand-machined UHMW polyethylene feeder dish  
- FDM-printed polycarbonate elliptical timing pulley on the dual-shaft NEMA 17 rear shaft for flapper drive with GT2 belt  

**Sensing and control electronics:**  
- Arduino Due main controller  
- STMicroelectronics L6470 AutoDriver stepper driver  
- XBee-PRO Series 1 wireless modules  
- Pixy (CMUcam5) vision module  
- Sharp GP2Y0D810Z0F IR proximity sensors  

**Power and switching:**  
- 11.1 V LiPo battery (3S, ~6400 mAh class)  
- Omron G3SD-Z01P-PD-US solid-state relay for solenoid activation  

**Fasteners and hardware:**  
- Standard metric fasteners, washers, springs, magnets, and aluminum posts  
- Thread-lock on vibration-prone joints  

## Release

- **CAD:** full assembly STEP available in portfolio (see 3D Model Files)
- **Software:** 
  - Firmware repo: [https://github.com/adamwlester/icr-system](https://github.com/adamwlester/icr-system)
- **Related portfolio entry:** [Instantaneous Cue Rotation Arena](https://www.cadcrowd.com/3d-models/instantaneous-cue-rotation-arena)

## References

For additional details, see the published methods manuscript featuring this system and performance comparisons with an earlier fixed-feeder variant:
- Lester, A. W., Kapellusch, A. J., & Barnes, C. A. (2020). [A novel apparatus for assessing visual cue-based navigation in rodents](https://doi.org/10.1016/j.jneumeth.2020.108667). Journal of Neuroscience Methods, 338, 108667.


</div>
<div class="content-group content-group-secondary" markdown="1">

## Role & Contributions

- Conceived, designed, and maintained end to end
- Fabricated and assembled key hardware
- Coordinated machining/fabrication of select parts
- Authored control software
- Designed and executed behavioral validation

## Highlights & Key Specs

**Drive and motion:**  
- Stepper-motor-driven robot with wireless control and onboard microcontroller and 11.1 V power  
- Commutator-free operation  
- Embedded Arduino Due microcontroller and motor driver  

**Tracking:**  
Dual-source tracking fused with an extended Kalman filter using overhead-camera and Pixy (CMUcam5) inputs for smooth position/velocity tracking  

**Reward delivery:**  
- Retractable feeder arm extends ~60 cm and pivots for access during reward  
- Hydraulic solenoid valve dispenses liquid reward  
- Synchronized event timestamps  

**Track cleaning:**  
Integrated track-cleaning module with neoprene flap and ethanol wiper to minimize odor and visual cues  

## Deployment & Status

**Development:**  
Completed, Aug 2015–May 2017  

**Deployment:**  
Barnes Lab, University of Arizona (2 studies)  

**Status:**  
Retired, May 2017–Aug 2021, Barnes Lab  

## Licensing

- **Hardware:** CERN-OHL-W-2.0
- **Software:** MIT
- **Documentation:** CC-BY-4.0


</div>
</div>
