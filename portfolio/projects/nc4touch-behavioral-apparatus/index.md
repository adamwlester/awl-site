---
layout: project-detail-page
title: "NC4touch Behavioral Apparatus"
description: "Touchscreen-based behavioral apparatus for flexible, high-throughput cognitive testing with mice and rats."
summary: "Touchscreen-based behavioral apparatus for flexible, high-throughput cognitive testing with mice and rats."
hero: "images/hero.png"
model_src: "models/nc4touch-behavioral-apparatus.glb"
model_camera_orbit: "auto auto auto"
model_camera_target: "auto auto auto"
model_fov: "auto"
images:
  - src: "images/render_1.png"
    caption: "Oblique view (right, top) render of full NC4touch behavioral apparatus including exposed interior."
  - src: "images/render_2_annotated.png"
    caption: "Annotated oblique view (front, right) render of interior touchscreen end of apparatus."
  - src: "images/render_3_annotated.png"
    caption: "Annotated front view render of electronics bay on touchscreen side of apparatus."
  - src: "images/render_4_annotated.png"
    caption: "Annotated oblique view (rear, right) render of interior feeder port end of apparatus."
  - src: "images/render_5_annotated.png"
    caption: "Annotated rear view render of electronics bay on feeder port end of apparatus."
  - src: "images/photo_1.png"
    caption: "Bench photo of full NC4touch behavioral apparatus."
  - src: "images/photo_2.png"
    caption: "Bench close-up photo of interior touchscreen end of apparatus."
  - src: "images/photo_3.png"
    caption: "Bench close-up photo of interior feeder port end of apparatus."
published: true
---

<div class="content-groups">
<div class="content-group content-group-primary" markdown="1">

## Description

NC4touch is a three-screen, Raspberry Pi-controlled chamber with calibrated liquid-reward delivery, overhead video tracking, sensory cue delivery, and modular device I/O for flexible, high-throughput cognitive testing in mice and rats.

The enclosure consists of a trapezoidal workspace with three touchscreens at the front and a food-reward dispensing system in the rear. The frame uses 10 × 10 mm aluminum T-slot extrusion with SLA-printed brackets and mounts, and laser-cut acetal panels for the enclosure and electronics bays, keeping the electronics fully separated from the behavioral space.

A USB camera mounted above the system captures the full field of view, and removable, laser-cut, 3/16 in clear acrylic lid and floor panels provide visibility and can be easily removed to aid wipe-down cleaning.

The front panel includes three capacitive touchscreens, each with a cue RGB LED and a buzzer for trial timing and feedback. Each screen is driven by a dedicated FireBeetle 2 M0 microcontroller over a single GDI ribbon cable, with USB used for command and data. Using a dedicated controller per display lets the screens load and render images in parallel, so updates do not block each other and refresh times stay fast under load. Because rodents can behave like a floating ground, a thin copper-foil-laminated floor panel beneath the screens nests into the removable acrylic floor but stays attached to the frame to keep the ground path intact.

The rear panel integrates a 3D-printed feeder port assembly with IR sensors, a stainless-steel lick spout, and a panel-mount cue RGB LED. A peristaltic pump with a dual-motor controller provides calibrated liquid rewards via food-grade silicone tubing. The IR break-beam detects nose-in and feeder occupancy for precise dosing and event logging. All tubing, port components, and the spout are quick to remove for cleaning, with standard fittings and clear service access.

A Raspberry Pi manages task state, device I/O, and logging. It sends display updates to each screen via its dedicated microcontroller, controls the cue LEDs and buzzer, and triggers pump dosing. It receives touch events from all three screens and feeder IR signals, and timestamps these alongside the video stream from the overhead camera. Data are written to disk as compact CSV logs plus an optional frame-synchronized MP4 file to support reproducible analysis.

Single- or multi-chamber operation is supported. A single Raspberry Pi can run one or multiple daisy-chained chambers. Multi-chamber setups can be networked over Ethernet with a lightweight browser UI for monitoring and control. Optional PoE provides single-cable power and data to reduce clutter and simplify installation.

Mechanical and electrical design emphasize maintainability and replication. Panels are flat-pattern, laser-cut parts with captive fasteners where appropriate. 3D-printed brackets localize loads and register panel geometry. All external connectors are panel-mount for strain relief and quick replacement. Front and rear electronics bays are isolated from the behavioral space to protect components and simplify wipe-down.

## Validation & Performance

**Bench validation:** 
- End-to-end verification across touch detection, cue delivery, pump dosing, synchronized video, and CSV logging
- Validation performed on single- and multi-chamber setups using the browser UI and PoE

**Timing and data integrity:**
- Frame-aligned MP4 confirmed millisecond event–video alignment
- Chambers wrote synchronized session logs to shared storage

**Networked operation:**
- Multi-chamber control over Ethernet with shared code, firmware, and image directories
- No desynchronization observed during concurrent runs

**Behavioral performance:** 
- 3/3 tested rats completed an eight-stage visual discrimination task with stage-wise performance gains, meeting the ≥77 percent correct advancement criterion at each stage

## Materials & Fabrication

**Frame:**
- Miniature T-slotted aluminum extrusion; associated T-nuts and fasteners
- Custom SLA-printed frame-to-panel joining brackets

**Enclosure and electronics bays:**
- Laser-cut POM-C (acetal) sidewalls and electronics panels
- Laser-cut clear acrylic top, floor, and grounding panel
- SLA-printed brackets for panel registration and service access
- SLA-printed clips and cable mounts

**Displays and controllers:** 
- Three capacitive touchscreens (DFRobot Fermion DFR0669)
- Three FireBeetle 2 M0 (DFR0652) development board controllers

**Cue delivery:** 
- Four Dialight 8 mm RGB panel indicators (6201121317F)
- Gravity digital buzzer (DFR0032)

**Camera:** 
- DFRobot 8 MP USB camera (FIT0729)
- Dedicated SLA-printed camera mount assembly

**Feeder system:**
- SLA-printed feeder port assembly
- Adafruit IR break-beam sensor (2167)
- TFS RP-CIII ring pump
- Stainless-steel tubing, food-grade silicone tubing, and glass vials

## Release

**CAD:**  
Design files including SolidWorks assemblies and parts, cutting templates, and documentation: [https://osf.io/8q9tk](https://osf.io/8q9tk)

**Software:**   
Firmware and software repo: [https://github.com/NC4Lab/TouchscreenApparatus](https://github.com/NC4Lab/TouchscreenApparatus)

**On request:**  
Additional design files; assembly notes  

## References

For additional details, see:  
- Modara, G., Lester, A. W., Schwein, I., & Madhav, M. S. (2025). NC4touch: An open-source modular touchscreen apparatus for rodent behavioral testing. bioRxiv. [link pending]


</div>
<div class="content-group content-group-secondary" markdown="1">

## Role & Contributions

- Co-conceived and co-architected the system
- Developed all CAD models and assemblies
- Led hardware validation (team of 3)
- Contributed to control firmware
- Primary hardware maintainer

## Highlights & Key Specs

**Workspace:**
- Trapezoidal chamber with isolated electronics bays
- Removable clear acrylic lid and floor for wipe-down cleaning

**Displays:**
- Three 3.5 in 320 × 480 capacitive touchscreens
- Three screen-dedicated microcontrollers
- GDI ribbon cable for display, USB for command and data

**Control:**
- Raspberry Pi 4 with PoE
- Single or multi-chamber orchestration via browser UI
- Unified I/O and logging

**Cue delivery:** 
- Front and rear interior panel RGB indicators
- Front interior panel buzzer

**Tracking:** 
- 8 MP USB overhead camera covering the full field of view

**Reward:** 
- IR break-beam for reward timing and logging
- Peristaltic pump for precise, repeatable food dosing

**Data:** 
- CSV logging
- Optional synchronized MP4 with millisecond event timestamps

## Deployment & Status

**Development:**  
Completed, Sep 2023–Nov 2024  

**Deployment:**  
- NC4 Lab, University of British Columbia (2 studies, 4 rigs)  
- Snyder Lab, University of British Columbia (1 study, 2 rigs)  

**Status:**  
Active, Nov 2024–present, NC4 Lab

## Licensing

**Hardware:** CERN-OHL-W-2.0  
**Software:** MIT  
**Documentation:** CC-BY-4.0


</div>
</div>
