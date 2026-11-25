# Model Tab - Mean Stress Alignment

## Overview

The mean stress alignment is a task used in GageMap to align  mean/static stresses into either the vibratory/dynamic maximum principal strain direction or the vibratory/dynamic maximum principal stress direction.  Once generated, mean stress aligned values become available in both the Animation Task and Fatigue Assessment task.  Each pass through the analysis produces a mode dependent variable.

The Mean Stress Alignment task is available in the "Animate" or "Fatigue" tab on the left side panel. The tab is located along the top of the panel.

## Limitations

In order to conserve on memory requirements, speed of use, and ease of use, a few limitations in the mean stress alignment task have been implemented. The limitations are as follows:

- User will be limited to retention in memory of one (1) component of the transformed stress tensor for a single static load case.
- Accessibility to other components will require an additional computation cycle.

## Aligning Mean Stress

1. Navigate to the "Mean Stress Alignment Setup" in the tab along the top of the left side panel in either the "Animate" or "Fatigue" Tabs.
2. In the "Compute new Alignment" section, select the static load to be aligned from the Static Load selection drop-down list.
3. Select the vibratory direction to align the static load selected above by selecting from the Vibratory direction drop-down list.
4. Select which component of the transformed stress tensor to be stored by selecting from the Store Component drop-down list.

> [!NOTE]
> When choosing either X, Y, or Z, the stored component is computed from a sorted eigenvector in the order of max_prin_absolute to min_prin_absolute. For example, if you choose the option of X (Max Prin), this max principal is the greatest absolute value of the three principals.

1. Click on Compute to compute the new stress alignment values.
2. If successful, the "Static Loads" field of the "Current Alignment" section will update.

## Contouring Aligned Mean Stress Values

The aligned static stress variable selected for storage is available as a mode dependent variable ("Static Stress Aligned").  The variable can be contoured by following the instructions below:

1. Navigate to the "Animation Setup" tab on either on the left side panel of either the "Model" or "Fatigue" tabs.
2. Select the Static Load Case from which the alignment was performed under the "Loads" section of the panel.  Enter the appropriate scale factor or RPM value in the "Scaling" section of the panel (see [Model Tab - Animation](task_modelAnim.md) for more details on how to use the Animator).
3. Select the desired mode from the Modes list. Enter any non-zero Mode Amplitude and set an appropriate Animation scale.
4. "Static Stress Aligned" will automatically be selected when a Mean Stress Alignment is selected. To return to this contour type from another setting, select "Other" from the "Animation Mode" dropdown and "Static Stress Aligned" from the "Contour Type" dropdown.
5. The model now reflects a contour of the computed mean stress alignment values.
6. To contour other modes, repeat steps 3 & 4.

> [!NOTE]
> In conjunction with the contouring, the static stress aligned variable is also available for plotting and mode scaling within the Fatigue Assessment Task.  The variable is available under the Static Type as Vibratory Aligned.

> [!NOTE]
> Static Stresses can only be alligned with a single mode at a time. If multiple modes in the animation have nonzero amplitudes, the static stresses will only be aligned with the *first* of these nonzero modes, and the contouring will reflect this alignment.
