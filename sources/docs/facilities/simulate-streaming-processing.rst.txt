.. _simulate-streaming-processing:

========================================
Simulate streaming processing
========================================

For this we are assuming you have installed Scipion and all necessary EM packages.
**This is a draft page**

Simulation of acquisition:
==========================

use scripts/simulate_acquisition.py

Sample usage would be:

scipion run scripts/simulate_acquisition.py '/home/pablo/desarrollo/scipion/data/tests/jmbFalconMovies/Falcon_*.mrcs' /home/pablo/desarrollo/scipion/data/tests/microscope_stream/


Usage: simulate_acquisition.py INPUT_PATTERN OUTPUT_FOLDER

* INPUT_PATTERN: input pattern matching input files.
* OUTPUT_FOLDER: where to create the output links.

Once you run it you will get a movie each 30 seconds in the OUTPUT_FOLDER

Next steps would be to:

1. Create a empty project
2. Add and "import movies protocol" pointing to the "OUTPUT FOLDER" and execute it (activate streaming)
3. Add any movie alignment(motioncorr, optical alignment,....) and choose the output (movies) from step 2
4. Add a ctf estimation protocol and choose the output of step 3 (you'll need to wait until there is any output)
5. Add a monitor summary (Ctrl+F) and search for summary.
