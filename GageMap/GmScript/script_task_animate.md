# Animation Functions for Scripting

Using the GM.animate() function group, the following functions are available:

- [contour(contour_mode, contour_type, auto_scale)](#contourcontour_mode-contour_type-auto_scale)
- [scale(scale)](#scalescale)

## contour(contour_mode, contour_type, auto_scale)

**Description:**

Set the animation contour mode and type for use during animation.

**Arguments:**

- contour_mode = INTEGER

  > - 0 - Off
  > - 1 - Static Strain
  > - 2 - Static Stress
  > - 3 - Mean Aligned Stress
  > - 4 - Static Rotation
  > - 5 - Static Displacement
  > - 6 - Dynamic Strain
  > - 7 - Dynamic Stress
  > - 8 - Dynamic Rotation
  > - 9 - Dynamic Displacement
  > - 10 - Total Strain
  > - 11 - Total Stress
  > - 12 - Total Rotation
  > - 13 - Total Displacement
  > - 15 - Temperature
- contour_type = Dependent on Contour Mode used above, INTEGER

  > > - Contour Types for Static Strain:
  > >
  > >   > - 1 - Overall Max
  > >   > - 2 - Equivalent
  > >   > - 3 - Max Principal
  > >   > - 4 - Min Principal
  > >   > - 5 - X Component
  > >   > - 6 - Y Component
  > >   > - 7 - Z Component
  > >   > - 8 - XY Shear
  > >   > - 9 - YZ Shear
  > >   > - 10 - ZX Shear
  >
  > - Contour Types for Static Stress:
  >
  >   > - 1 - Overall Max
  >   > - 2 - Von Mises
  >   > - 3 - Max Principal
  >   > - 4 - Min Principal
  >   > - 5 - X Component
  >   > - 6 - Y Component
  >   > - 7 - Z Component
  >   > - 8 - XY Shear
  >   > - 9 - YZ Shear
  >   > - 10 - ZX Shear
  > - Contour Types for Dynamic or Total Strain:
  >
  >   > - 1 - Overall Max
  >   > - 2 - Equivalent
  >   > - 3 - Max Principals
  >   > - 4 - Principals Sum
  >   > - 5 - X Component
  >   > - 6 - Y Component
  >   > - 7 - Z Component
  >   > - 8 - XY Shear
  >   > - 9 - YZ Shear
  >   > - 10 - ZX Shear
  > - Contour Types for Dynamic or Total Stress:
  >
  >   > - 1 - Overall Max
  >   > - 2 - Von Mises
  >   > - 3 - Max Principals
  >   > - 4 - Principals Sum
  >   > - 5 - X Component
  >   > - 6 - Y Component
  >   > - 7 - Z Component
  >   > - 8 - XY Shear
  >   > - 9 - YZ Shear
  >   > - 10 - ZX Shear
  > - Contour Types for Static, Dynamic, or Total Rotations or Displacements:
  >
  >   > - 1 - USUM
  >   > - 2 - USUM with Phase
  >   > - 3 - X Direction
  >   > - 4 - Y Direction
  >   > - 5 - Z Direction
- auto_scale = (0=false, 1=true), INTEGER

**Example:**

> `anim = GM.animate()`
>
> `anim.contour(1,1,0)`

## scale(scale)

**Description:**

Sets the animation scale for the model.

**Arguments:**

- scale: new animation scale, FLOAT

Example:

> `gm = GM.main()`
>
> `anim = GM.animate()`
>
> `anim.scale(0.5)`
