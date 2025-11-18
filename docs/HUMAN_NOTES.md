# HUMAN NOTES

### Random
^#[ ]\S+

### List of project slugs
nc4touch-behavioral-apparatus
omniroute-maze-system
instantaneous-cue-rotation-arena
track-mounted-feeder-cart
nc4gate-automatable-gate-module
two-axis-feeder-gantry
adjustable-aluminum-projector-mount
wireless-mobile-feeder-robot
silicon-probe-microdrive-housing
dual-bundle-electrode-drive
fischer-344-rat-model
roller-bearing-cable-guide

#### Personal projects
modular-rolling-tool-wall
hidden-drawer-nightstand
adjustable-tv-easel-stand
foldable-adjustable-painting-easel


### 3D Model Conversion

**SolidWorks SLDPRT/SLDASM → STEP AP214 using SolidWorks Assistant**
- Export SolidWorks parts/assemblies as STEP AP214 (`.step`) **with these STEP options**:
  - File format: `STEP`
  - Output as: `Solid / Surface geometry`
  - Set STEP configuration data: `OFF`
  - Export face/edge properties: `ON`
  - Split periodic faces: `ON`
  - Export 3D curve features: `ON`
  - Output coordinate system: `Default`

**Convert STEP to glTF (.glb) using CAD Assistant:**
- Open STEP in **CAD Assistant** (no special import options; use defaults).
- In CAD Assistant, **Save As → glTF 2.0 (Binary .glb)** with:
  - Format: `glTF 2.0` → `Binary (.glb)`
  - Units: `From source` (millimeters from STEP)
  - Transformation format: `Compact`
  - Node name format: `InstanceOrProduct`
  - Mesh name format: `Product`
  - Export UV for elements without texture maps: `OFF`
  - Merge faces within the same part: `ON`
  - Merge faces within 16-bit indices limit: `ON`

**(Optional) Make faces transparent in Blender 4.3.2:**
- Import the `.glb` into Blender: **File → Import → glTF 2.0 (.glb/.gltf)**
- Select each object that should be semi-transparent:
  - In **Material Properties → Surface → Principled BSDF**, lower **Alpha** from `1.0` to `0.1` (or desired value)
  - In **Material Properties → Settings → Surface**, set **Render Method** to `Blended`
- Export back to `.glb`: **File → Export → glTF 2.0** with:
  - **Format:** `glTF Binary (.glb)`
  - **Include → Data:** uncheck `Cameras` and `Punctual Lights`
  - **Compression:** check `Compression` (keep the default numeric values)
  - **Animation:** uncheck `Animation`