.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo


.. _workflows-recomended:

============================
Workflows recomended
============================

The following streaming workflows are available inside Scipion (import workflow option) and through WorkflowHub and cover different levels of automated SPA processing, from basic acquisition monitoring to complete 3D reconstruction. They can be used as provided or customized to meet the requirements of each facility.

Simple Processing
^^^^^^^^^^^^^^^^^

**Purpose** Basic preprocessing and acquisition monitoring.

**Processing**
Movies → Motion correction
Motion-corrected micrographs → CTF estimation
Quality filters for micrograph curation

**Main plugins** pwem, Xmipp3, MotionCor2, Cistem

2D SmartScope
^^^^^^^^^^^^^

**Purpose** Automated screening with real-time feedback to SmartScope.

**Processing**
Movies → Motion correction
MaxShift analysis
CTF estimation + CTF consensus
AI-based micrograph quality assessment
Particle picking
Automatic box size estimation
Particle extraction
Streaming 2D classification
2D class quality assessment
Feedback to SmartScope

**Main plugins** pwem, Xmipp3, MotionCor2, MIFFI, Cistem, SmartScope, SPHIRE, CryoAssess

2D Xmipp
^^^^^^^^

**Purpose** Complete streaming SPA preprocessing and 2D classification.

**Processing**
Movies → Motion correction
CTF estimation
Dose, MaxShift and tilt analysis
Micrograph categorization
CTF consensus
Deep Micrograph Cleaner
Duplicate particle removal
Automatic box size estimation
Picker training
Particle picking
Streaming 2D classification

**Main plugins** pwem, Xmipp3, MotionCor2, MIFFI, Cistem, EMFacilities, SPHIRE, Gautomatch, Relion, RePiC

2D Relion
^^^^^^^^^

**Purpose** Streaming processing from movies to 2D classes using Relion.

**Processing**
Movies → Motion correction
CTF estimation
Quality filters
Automatic box size estimation
Picker training
Particle picking
2D classification (25k, 50k and 100k particles)

**Main plugins** pwem, Relion, MotionCor2, Cistem, Xmipp3

2D CryoSPARC
^^^^^^^^^^^^

**Purpose** Streaming processing from movies to 2D classes using CryoSPARC.

**Processing**
Movies → Motion correction
CTF estimation
Quality filters
Automatic box size estimation
Picker training
Particle picking
2D classification (25k, 50k and 100k particles)

**Main plugins** pwem, CryoSPARC, MotionCor2, Cistem, Xmipp3

3D Relion
^^^^^^^^^

**Purpose** Automated streaming workflow from movies to an initial 3D reconstruction.

**Processing**
Movies → Motion correction
CTF estimation
Quality filters
Automatic box size estimation
Picker training
Particle picking
2D classification (25k, 50k and 100k particles)
3D reconstruction (first 200k particles)
Automatic 2D/3D class selection
Multiple unsymmetrized 3D models

**Main plugins** pwem, Relion, MotionCor2, Cistem, Xmipp3

3D CryoSPARC
^^^^^^^^^^^^

**Purpose** Automated streaming workflow from movies to an initial 3D reconstruction.

**Processing**
Movies → Motion correction
CTF estimation
Quality filters
Automatic box size estimation
Picker training
Particle picking
2D classification (25k, 50k and 100k particles)
3D reconstruction (first 200k particles)
Automatic 2D/3D class selection
Multiple unsymmetrized 3D models

**Main plugins** pwem, CryoSPARC, MotionCor2, Cistem, Xmipp3