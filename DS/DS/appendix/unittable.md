# Integration Table

The purpose of the integration table is to pre-define what units can be
integrated and what the new units and scalar need will be. The integration
table is loaded in the to application via the File->Import menu. Once loaded it
is a available to both the frequency domain integration that can be done on the
**Spectrum Plots** and the time domain integration that can configured on the
**Setup Editor**. The integration can be done in either place.
Integration done on the plot via the frequency domain can be on a per user per
plot basis, integration done in the setup panel is available the same to all
plots and users.

Integration table domain change coding:

| Domain Change | Code |
| --- | --- |
| Differentiation | -1 |
| None | 0 |
| Single Integration | 1 |
| Double Integration | 2 |

Integration table layout, this is formatted in the actual file as a comma separated variable

| Input Units | Int Code | Output Units | Scale |
| --- | --- | --- | --- |
| Text | -1 .. 2 | Text | Numeric |

example integration table text:

```
#diff=-1, normal=0, 1xIntegrate = 1, 2xIntegrate = 2
#inputUnits,(-1 0 1 2),outputUnits,conversion scale
g,1,ips,386.089
g,1,milps,386089
g,1,mps,9.80665
g,1,mmps,9806.65
ips,1,mil,1000
mps,1,mm,1000
g,2,inches,386.089
g,2,mil,386089
g,2,meters,9.80665
g,2,mm,9806.65
ips,-1,g,0.00259008
mps,-1,g,2.59008e-06
mmps,-1,g,0.101972
mil,-1,ips,0.001
```
