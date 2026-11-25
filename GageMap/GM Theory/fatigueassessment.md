# Determination of Modal Scale Factors

GageMap has the ability to determine the modal scale factors such that a node will reside at 100% of the material fatigue limit. This modal scale factor is determined using the following for each active node group:

> 1. Determine the dynamic stress limit using each nodes static stress.
> 2. Compute the ratio of the node dynamic stress to the vibratory limit.
> 3. Identify the node with the highest ratio – this is the limiting node.
> 4. The inverse of the ratio computed in #2 is the mode scale factor for the group.
> 5. The minimum modal scale factor for each group is the modal scale factor,

For example if the vibratory limit for a particular node is 116 ksi and the nodal stress is 1,500 ksi the ratio is 1,500/116 = 12.931. If this is the node with the highest ratio the modal scale factor would be 1/12.931 = 0.077.

  

## Application of Modal Scale Factors

The modal scale factors are then multiplied by the each gage nominal strain & stress values to arrive at strain & stress limits. In addition the modal scale factor is multiplied by the actual tip timing deflection to determine deflection limits.
