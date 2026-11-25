# Mean Stress Alignment

This chapter will explain the theory implemented in GageMap for mean stress alignment.

## Description

The following tasks are performed on a node-by-node basis for each vibratory mode within the SDR file. If multiple static load cases exist in the SDR file, static stress transformation will be performed for only the chosen static load case. Transformed static stress may also be scaled within the “Animate” and “Fatigue Assessment” tasks via a scale factor if the load case does not contain a rotational velocity or w2 if the load case does contain a rotational velocity.

Both cases below assume the following nodal quantities being available:
Mean stress/strain vectors:

> ![e1](images/msa/e1.png) (equations 180.1 & 180.2)

Vibratory stress/strain vectors:

> ![e2](images/msa/e2.png) (equations 180.3 & 180.4)

Form the following mean/vibratory stress/strain tensors:

> ![e3](images/msa/e3.png) (equations 180.5 & 180.6)
>
> ![e4](images/msa/e4.png) (equations 180.7 & 180.8)

## Case #1: Transformation of static stress into the maximum vibratory principal strain direction

Determine the principle strains and their directions from equation 180.8 above via an eigensolution technique. The eigenvalues of the strain tensor are the principle strains and the eigenvectors of the strain tensor are the corresponding direction vectors. Therefore we seek the solution to the following:

> ![e5](images/msa/e5.png) (equation 180.9)

Where,

> ![e6](images/msa/e6.png)
> ![e7](images/msa/e7.png)

It is assumed that ![i1](images/msa/i1.png) and the corresponding columns in ![i2](images/msa/i2.png) have been reordered such that ![i3](images/msa/i3.png).

Additionally if each column of ![i2](images/msa/i2.png)  represents the direction vector normal to the maximum principal strain plane, ![i2](images/msa/i2.png)  may be organized such that each row represents the corresponding direction vector by computing the transpose of ![i2](images/msa/i2.png).

Prior to transformation it should be verified that ![i2](images/msa/i2.png)  is a proper directional cosine matrix. This is true if the following relation holds:

> ![e8](images/msa/e8.png) (equation 180.10)

If ![i2](images/msa/i2.png) is not a proper DCM then each column of the matrix should be normalized to a unit vector.

Transform the static stress tensor into the ![i4](images/msa/i4.png) direction using one of the two formulas provided.

If each row of ![i2](images/msa/i2.png) represents a direction of principal strain then the following transformation applies:

> ![e9](images/msa/e9.png) (equation 180.11)

If each column of ![i2](images/msa/i2.png) represents a direction of principal strain then the following transformation applies:

> ![e10](images/msa/e10.png) (equation 180.12)

Where,

![i5](images/msa/i5.png) is the static stress tensor in the ![i4](images/msa/i4.png) direction.

## Case #2: Transformation of static stress into the maximum vibratory principal stress direction

Determine the principle strains and their directions from equation 180.7 above via an eigensolution technique. The eigenvalues of the stress tensor are the principle stresses and the eigenvectors of the stress tensor are the corresponding direction vectors. Therefore we seek the solution to the following:

> ![e11](images/msa/e11.png) (equation 180.9)

Where,

> ![e12](images/msa/e12.png)
> ![e13](images/msa/e13.png)

It is assumed that ![i6](images/msa/i6.png) and the corresponding columns in ![i2](images/msa/i2.png) have been reordered such that ![i7](images/msa/i7.png) .

Additionally if each column of ![i2](images/msa/i2.png) represents the direction vector normal to the maximum principal stress plane, ![i2](images/msa/i2.png) may be organized such that each row represents the corresponding direction vector by computing the transpose of ![i2](images/msa/i2.png).

Prior to transformation it should be verified that ![i2](images/msa/i2.png) is a proper directional cosine matrix. This is true if the following relation holds:

> ![e14](images/msa/e14.png) (equation 180.10)

If ![i2](images/msa/i2.png) is not a proper DCM then each column of the matrix should be normalized to a unit vector.

Transform the static stress tensor into the ![i8](images/msa/i8.png) direction using one of the two formulas provided.

If each row of ![i2](images/msa/i2.png) represents a direction of principal stress then the following transformation applies:

> ![e15](images/msa/e15.png) (equation 180.11)

If each column of ![i2](images/msa/i2.png) represents a direction of principal stress then the following transformation applies:

> ![e16](images/msa/e16.png) (equation 180.12)

Where,

![i5](images/msa/i5.png) is the static stress tensor in the ![i8](images/msa/i8.png) direction
