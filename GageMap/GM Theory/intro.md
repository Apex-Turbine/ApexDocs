# Introduction

This manual will help explain the theories behind GageMap.

## Overview

GageMap is a multi-platform software application designed to reduce product cycle time by implementing rigorous analytical processes in performing pre-test planning and post-test analysis of vibratory measurement instrumentation. The pre-test portion of GageMap incorporates a methodology that allows the engineer to make trade-offs between mode identification, mode visibility, data integrity, and geometry to determine optimum locations for measurement. The post-test allows the engineer to assess the fidelity of the measured responses and correlate the measurements with predictions. A properly executed pre- and post-test plan results in a structural model that can be used to determine various response properties throughout the structure quite easily.

GageMap relies on an analytical basis for assessing sensor placement and for optimizing sensor locations. The analytical basis is in the form of a finite element model. GageMap supports the most popular finite element solvers in use today: ABAQUS, ANSYS, and NASTRAN. GageMap generally supports 2-D and 3-D continuum and shell element types.  See each converter section for specifics.

## Chapters

- [Strain and Stress Computation](strainStress.md)
- [Pre-Test Optimization](PreTestOpt.md)
- [Cyclic Symmetry](css.md)
- [Anisotropic Materials](anisthropicMat.md)
- [Mean Stress Alignment](meanStress.md)
