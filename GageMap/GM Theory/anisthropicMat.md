# Anisotropic Materials

If material properties are found in the database file they will be read and applied to the appropriate element type for computation of face and gage stresses. The 6x6 material stiffness matrix is formed according to the relation:

> ![eq1](images/am/eq1.png)

where,

> ![eq2](images/am/eq2.png)

and

> ![eq3](images/am/eq3.png)

or

> ![eq4](images/am/eq4.png)

with

> ![eq5](images/am/eq5.png)

Either major, minor or both Poisson ratios may be defined. GageMap will form and report the material stiffness matrix by selecting Options > Model Info. Once the material stiffness matrix is formed, GageMap will transform the matrix such that it is parallel with either the face or strain gage coordinate system according to the relation:

> ![eq6](images/am/eq6.png)

where

> ![eq7](images/am/eq7.png)

and l1, l2, l3, m1, m2, m3, n1, n2, n3 form the elements of the direction cosine matrix relating the face or strain gage coordinate.
