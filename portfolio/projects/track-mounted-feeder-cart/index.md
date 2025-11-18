---
layout: project-detail-page
title: "Track-Mounted Feeder Cart"
summary: "Mobile feeder cart for controlled on-track liquid reinforcement with gated feeder access for rodent circular track experiments"
hero: "images/render_1.png"
model: "models/track-mounted-feeder-cart.glb"
images:
  - src: "images/render_1.png"
    caption: "three-quarter view (front, right, top) render of track-mounted feeder cart installed on Dome system platform"
  - src: "images/render_2_annotated.png"
    caption: "annotated three-quarter view (front, right, top) render of feeder cart system components"
  - src: "images/render_3_annotated.png"
    caption: "annotated three-quarter view (front, right, top) render of gated feeder port, close-up"
  - src: "images/render_4.png"
    caption: "right cross-section view render of gated feeder port, gate open"
  - src: "images/render_5.png"
    caption: "right cross-section view render of gated feeder port, gate closed"
  - src: "images/render_6.png"
    caption: "three-quarter view (front, left, top) render of tether guide clamp, close-up"
  - src: "images/photo_1.png"
    caption: "bench photo of prototype track-mounted feeder cart assembly"
  - src: "images/photo_2.png"
    caption: "combined bench close-up photos of gated feeder port, open and closed"
---

<div class="project-columns">
<div class="project-column project-column-left" markdown="1">

## Description

This mobile feeder cart maintains a fixed offset to a rat running on a circular track and dispenses liquid rewards through a servo-gated feeder port, enabling continuous reinforcement while constraining the animal’s movement options.

The cart uses waterjet-cut 1/16 in clear polycarbonate panels and 1/8 in 6061 aluminum plate, with SLA-printed brackets and standard fasteners throughout for easy replication and repair.

A 3D-printed feeder port is supplied by a peristaltic pump via 1/16 in ID food-grade silicone tubing. Access to the port is controlled by a compact micro-servo-actuated vertical gate that can fully block or expose the port. An infrared (IR) break-beam across the port detects nose-in for precise dosing and event logging. Alternate feeder ports at either end of the cart can be used to drop rewards onto the track ahead of or behind the rat via a quick-disconnect tube fitting.

The cart integrates an overhead tether guide for wired electrophysiology that rides on a curved rail above the track. A low-friction trolley with five adjustable 1/4 in roller bearings keeps the cable centered over the animal and travels with the cart.

A microcontroller controls the pump, gate, and sensors, while a central drive motor rotates the cart assembly to track the rat’s position.

Drive is provided from a central pillar assembly at the platform center; the motor’s torque is transmitted via two 0.25 in coupling rods linking the central pillar to the cart’s drive interface. The central pillar incorporates alignment and load-bearing components (timing-belt pulleys, quick-disconnect bushing, sealed ball and thrust bearings) to ensure smooth rotation and a serviceable setup.

This feeder cart was designed for use with the Dome system, a rodent augmented-reality apparatus in which visual stimuli are projected onto the inside of a circular dome surrounding a circular track. The updated cart design retains compatibility with the Dome system while adding modular features like the feeder port, improved access control, and streamlined fabrication.

## Validation & Performance

**Stable use:**  
In-rig and in vivo use with stable operation for 2 experiments  

## Materials & Fabrication

**Frame and panels:**  
Waterjet-cut 1/16 in clear polycarbonate side walls and end plates, and 1/8 in 6061 aluminum frame members  

**Drive and motion:**  
Central pillar assembly, two 0.25 in coupling rods, sealed ball bearings, threaded track roller  

**Feeder and gate:**  
- SLA-printed feeder port and gate arm, bottle holder and mount  
- Takasago RP-CIII series peristaltic pump, 9 g micro servo, Adafruit IR break-beam sensor 2167, 1/16 in ID food-grade silicone tubing  

**Tether guide:**  
- SLA-printed tether-roller housing  
- Waterjet-cut 1/8 in 6061 aluminum curved guide components  
- Five 1/4 in roller bearings  

## Release

- **CAD:** STEP files available in portfolio (see 3D Model Files)
- **On request:** assembly notes; additional design files

## References

The original Dome system and cart design that this version was adapted from are described in detail in the following methods article:
- Madhav, M. S., Jayakumar, R. P., Lashkari, S. G., Savelli, F., Blair, H. T., Knierim, J. J., & Cowan, N. J. (2022). The Dome: a virtual reality apparatus for freely locomoting rodents. Journal of Neuroscience Methods, 368, 109336.


</div>
<div class="project-column project-column-right" markdown="1">

## Role & Contributions

- Conceived, designed, and fabricated the system
- Developed all CAD models and assemblies
- Primary maintainer

## Highlights & Key Specs

**Drive and motion:**  
Central pillar drive with two 0.25 in coupling rods for smooth rotation and fixed-offset tracking  

**Access control:**  
Micro-servo-actuated vertical gate with repeatable full block/expose states  

**Reward delivery:**  
- Peristaltic pump with food-grade silicone lines  
- Quick-disconnect forward/rear drop ports  

**Detection and timing:**  
IR break-beam at port for nose-in timestamping and precise dosing  

**Ephys support:**  
Overhead tether guide with low-friction trolley and commutator integration  

## Deployment & Status

**Development:**  
completed, Feb 2024–Mar 2024  

**Deployment:**  
NC4 Lab, University of British Columbia (2 studies)  

**Status:**  
active, Mar 2024–present, NC4 Lab  

## Licensing

- **Hardware:** CERN-OHL-W-2.0
- **Documentation:** CC-BY-4.0


</div>
</div>
