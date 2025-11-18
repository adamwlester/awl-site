---
layout: project-detail-page
title: "Dual-Bundle Electrode Drive"
summary: "Split-bundle implant for dual-region tetrode recordings in freely moving rats."
hero: "images/render_1.png"
model: "models/dual-bundle-electrode-drive.glb"
images:
  - src: "images/render_1.png"
    caption: "three-quarter view (rear, left, top) render of the complete dual-bundle drive with FreeLynx cover and Halo-18 components"
  - src: "images/render_2_annotated.png"
    caption: "annotated exploded three-quarter view (rear, left, top) render of major assemblies, excluding cap and cover"
  - src: "images/render_3_annotated.png"
    caption: "annotated cross-section view render of the drive body and core with bundle guide"
  - src: "images/render_4_annotated.png"
    caption: "annotated three-quarter view (rear, left, bottom) render of the bundle guide subassembly"
  - src: "images/render_5_annotated.png"
    caption: "annotated three-quarter view (rear, left, top) render of the complete dual-bundle drive with FreeLynx cover and Halo-18 components"
  - src: "images/render_6_annotated.png"
    caption: "annotated exploded three-quarter view (rear, left, top) render of the FreeLynx cover with LED and diffuser stack"
  - src: "images/render_7.png"
    caption: "three-quarter view (rear, left, top) render of the drive cap and adjustable weight"
  - src: "images/render_8.png"
    caption: "exploded three-quarter view (rear, left, top) render of the drive cap and adjustable weight"
  - src: "images/photo_1.png"
    caption: "bench photo of the fully assembled drive with cap installed"
  - src: "images/photo_2.png"
    caption: "close-up bench photo showing the drive body and core with bundle guide"
---

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

**Mass:**  
~24 g for drive body, core, bundle guide, shuttles, and guide cannulae

**Shuttles:**  
M1 × 0.20 screws; ~9 mm total dorsal–ventral travel

**Bundles:**  
Two independently adjustable 9-tetrode bundles

**Cover:**  
Magnetically aligned cover for NeuraLynx FreeLynx with integrated LED tracking diffuser and thumb screw

**Cap:**  
Magnetically aligned cap with thumb screw retention and adjustable weights for acclimation

## Materials & Fabrication

**Structure:**  
SLA-printed resin body, bundle guide, cap, and cover components

**Shuttles:**  
Machined M1 screws and UHMW polyethylene shuttle plates

**Electronics:**  
Surface-mount LEDs integrated in headstage cover

**Hardware:**  
Standard hardware including #0-80 and M1 fasteners, washers, springs, neodymium magnets, center post

## Validation & Performance

**Stable use:**  
In-rig and in vivo use with stable recordings for 2 studies and 9 implants total.

## Deployment & Status

**Development:**  
Completed, Aug 2019–Jun 2020

**Deployment:**  
Barnes Lab, University of Arizona (2 studies)

**Status:**  
Active, Jun 2020–present, Barnes Lab

## Release

**CAD:** 
- STEP files available in portfolio (see 3D Model Files)
- Select additional files (i.e., drive body) withheld due to third-party IP
- **On request:** assembly notes

## Licensing

- **Hardware:** CERN-OHL-W-2.0
- **Documentation:** CC-BY-4.0

### Attribution

- Inspired by the NeuraLynx Halo-18; Halo-18-compatible geometry; independent, non-affiliated design. NeuraLynx and FreeLynx are trademarks of their owner; names used for identification only.
- Special thanks and acknowledgement to Anders Lundberg, designer of the Halo-18, for informal guidance during scoping; all engineering decisions and CAD were produced independently.

## References

- (content not provided)

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