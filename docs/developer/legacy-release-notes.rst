.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _legacy-release-notes:

============================
Legacy release notes
============================

v.0.2.2 Titanium (6 Feb 2014)
-----------------------------

* Export/Import workflow template in .json format
* Improved Runs Graph: (expand/collapse, small nodes, tooltips and keep positions)
* Get working the Relion polishing
* Review and update of the tutorials (specially the introdocutory one)
* Updated Spider protocols and tools
* Last fixes after Initial Volume WebTool
* MPI steps parallelization improved (95%)

v.0.1.4 Sillicon (6 Jun 2014)
-----------------------------

* Improved handling of large logs files (preview, refresh, colors...for web and tk)
* Fixed the use of MPI process in Parallel Protocols.
* Stored protocol steps in a separated .sqlite file (for performance)
* Stored objects creation time.
* Allowed selection of individual items from a set.
* Completion of the MDA workflow with all protocols and updated the
  Spider script parsing (Tapu visit) and Custom mask wizard
* More processing tests with ribo tutorial, and PcV viruses.
* Showj visualization now directly from the .sqlite files...Improved the
  Creation of subsets

v.0.1.3 Aluminium (9 May 2014)
--------------------------------

* Managing multiple runs selection (in Tk and Web): Copy and Delete
* Re-factored the Visualizers to use "Views", now more centralized between Tk and Web
* Re-factored the wizards in Web
* Improved read of big log files.
* Test files are centralized in DataSets and their are automatically downloaded.
* Added Groups and Lines for more compact parameters in Protocol Form
  (also working with Expert Level and Condition)
* Improved developer documentation (architecture and welcome guide)

v.0.1.2 Magnesium (10 Apr 2014)
--------------------------------

* Relion protocols completed (2D, 3D refine and classify, wizards, viewer...and web)
* Frealign 9.07 update (refine, wizards, viewers...and web)
* Protocols to import/export EMX format
* Created Protocol steps view
* Created Data view (and checked Relations inheritance, such as CTF)
* Improved tests datasets and classes.
* Improved way to create Materials & Methods, citations and summary (added bibtex parsing)
* Centralized execution under *scipion* entry script (also generation of stats)
* More protocols added from Scipion week

v.0.1.1 Sodium (10 Mar 2014)
----------------------------

* Missing release, due SAB visit.

v.0.1.0 Neon (10 Feb 2014)
---------------------------

* Missing release, due Scipion week for Xmipp protocols porting.

v.0.0.9 Fluor (10 Jan 2014)
----------------------------

* Mainly documentation and bug fixing.

v.0.0.8 Oxygen (18 Dic 2013)
----------------------------

* Changes:

    * BIG re-design, in both Web and Tk interfaces (automatic refresh also)
    * Wizards and Analyze results refined.
    * Added Twiki small subset of hypertext tags for Helps and Summaries
    * Scipion Day and several starting protocols.

* Known issues:

    * Memory leak (when the Tkinter GUI is open for long time, the RAM is
      consumed)
    * Performance issues with big datasets (Laura issues and RM complaints)
    * Need to handle multiple plots from Analyze results in Web (example
      ML3D)

v.0.0.7 Nitrogen (11 Nov 2013)
-------------------------------

* Added relations (For CTF, Aligment is missing)
* Developed first SPIDER protocols (align, filter, dimension reduction and classification) MDA workflow
* Included protocol viewer with Forms( ProtocolViewer) in Tkinter and Web
* More wizards for Tkinter and Web (adapted for SPIDER protocols)
* Improved protocols main interface.


v.0.0.6 Carbon (4 Oct 2013)
---------------------------

* Data classes are not sub-classes per packages, now they have a common Scipion representation and storage (sqlite). Added related convert.py modules for conversion.
* Web: fix styles, wizards.


v.0.0.5 Boron (5 Sept 2013)
---------------------------

* Missed release due vacations of team members

v.0.0.4 Beryllium (6 Aug 2013)
------------------------------

* Design changes:

    * All elements in a Set should contains an unique ID inside the set, that should be maintained in transformations of the set.
    * Eman version have been changed to 2.1, carrying different access using hdf and json

* Xmipp protocols:
    * OnlyAlignCL2D
    * RotSpectra
    * KerdenSOM
    * ML3D
    * Filters, Mask

* Eman protocols:
    * Boxing
    * Initial model

* GUI

    * Graph tree is working on Web
    *  Wizards on Tkinter
    *  Form improved, now using Tabs, include summary and parameters validations.
    * Basic analyze results of some protocols.
    * First try with web visualization of volumes with Astex and
      Chimera-WebGL

* Tests
    * Update new tests for protocols.
    * Running Buildbot for continuous integration.


v.0.0.3 Lithium (5 Jul 2013)
----------------------------

* Protocol execution:

    * Basic launch and update of protocols.

* Some Xmipp protocols, starting with Eman boxing, CTFFIND included
* GUI

    * Graph tree is working on Tkinter
    * Basic way of editing execution hosts and Host view in projects.

* Tests

    * Setup of the general organization of the tests and creation of several ones.
    *  First try with Buildbot