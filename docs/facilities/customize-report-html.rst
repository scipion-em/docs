.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _customize-html-report:

=========================
HTML report customization
=========================

.. :contents:: Table of Contents


0. Before we start
------------------
* We'll get started with an environment variable so that you can directly copy
  and paste all commands in this guide. Replace the values with the right path
  for your Scipion installation.

  .. code-block:: bash

      $ export SCIPION_DIR=/usr/local/scipion

* You'd also need a project with a Monitor Summary executed. We'll use the result of running scipion demo. If you don't have it yet, run scipion demo in your terminal:

  .. code-block:: bash

      $ scipion demo

* Open the directory of Scipion as a PyCharm project (or the editor of your choice).


1. Changing the logo
----------------------

The html code used by the summary monitor is in
`pyworkflow/templates/execution.summary.template.html
<https://github.com/I2PC/scipion/blob/master/pyworkflow/templates/
execution.summary.template.html>`_.
If we want to use a customized version, we'll have to modify this file.
It's always a good idea to keep a copy of the
original:

.. code-block:: bash

    $ cd $SCIPION_DIR
    $ cp pyworkflow/templates/execution.summary.template.html pyworkflow/templates/execution.summary.template.original.html

Now we open `pyworkflow/templates/execution.summary.template.html
<https://github.com/I2PC/scipion/blob/master/config/templates/execution.summary.template.html>`_.
to locate the logo and replace the url. We must choose a logo-sized image,
otherwise it'll change the layout of the page:

.. code-block:: html

    <BODY>
    <a id='refreshBtn'
       data-toggle="tooltip" title="Toggle auto refresh" data-placement="bottom"
       href="#" class="btn btn-info btn-lg">
        <span class="glyphicon glyphicon-refresh"></span>
    </a>
    <DIV id="content" class="clearfix container">
        <H1><img class="valign" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Logo_CNB.jpg/120px-Logo_CNB.jpg">&nbsp;&nbsp; Project %(projectName)s </H1>
        <DIV class="row">
            <DIV class="column column-5">

If our summary monitor is running, the next time it refreshes it should have the
new logo. If it isn't running, we can make a copy of the protocol to see the new
HTML.

* Right click on the summary monitor and choose *copy*:

  .. figure:: /docs/images/html_report_tutorial/copy_monitor_summary.png
     :align: center
     :alt: Copy monitor summary

* Adjust the refresh time to a lower amount, so it finishes quicker. Then launch
  protocol:

  .. figure:: /docs/images/html_report_tutorial/restart_monitor_summary.png
     :align: center
     :alt: restart monitor summary

* Click on Analyze results -> open html report to see the report with the new logo:

  .. figure:: /docs/images/html_report_tutorial/analyze_results.png
     :align: center
     :alt: analyze results

  .. figure:: /docs/images/html_report_tutorial/report_new_logo.png
     :align: center
     :alt: new logo


2. Removing a column from the table
------------------------------------

In this example we will remove the *DefocusU* column from the table:

.. figure:: /docs/images/html_report_tutorial/mic_table.png
   :align: center
   :alt: mic table

To do this, we have to go one step further and dig into the javascript code of
the html report, which you can find `after the closing of </body>
<https://github.com/I2PC/scipion/blob/master/pyworkflow/templates/execution.summary.template.html#L301>`_.
The first bit of code we find is the variable `report`. This variable has a few
`%(keywords)s`, which are used by Scipion to transfer data from the protocols
watched by the Summary Monitor to the HTML report.

.. code-block:: javascript

    var report ={
        date:"%(dateStr)s",
        project:"%(projectName)s",
        scipionVersion:"%(scipionVersion)s",
        acquisition:[
            %(acquisitionLines)s
        ],
        runs:[
            %(runLines)s
        ],
        ctfData: %(ctfData)s,
        movieGainData: %(movieGainData)s,
        systemData: %(systemData)s
    }

Then, we have a bunch of Javascript functions. It is a good idea to take a look
at the `populateReport()
<https://github.com/I2PC/scipion/blob/d1a60f69960d1079bbbecde5bf3f5f4017b36927/pyworkflow/templates/execution.summary.template.html#L1035-L1042>`_,
function, which has the high level functions responsible of each visible section
in the HTML report. In our case, we'll want to go check `addMicTable()`.

.. code-block:: javascript

    function populateReport(){
        addAcquisition();
        addRuns();
        addCTFChart();
        addMovieGainChart();
        addSystemChart();
        addMicTable();
    };

* Remove the column name from the header:

  .. code-block:: javascript

        if ('defocusU' in report.ctfData){
            cols.push(
                      // {"title": "DefocusU (µm)",
                      //   "render": $.fn.dataTable.render.number( ',', '.', 2)},
                      {"title": "Astigmatism (µm)",
                       "render": $.fn.dataTable.render.number( ',', '.', 3)},
             ...

* Don't add DefocusU data to the rows:

  .. code-block:: javascript

       if ('defocusU' in report.ctfData){
           rowValues.push(
                          // report.ctfData.defocusU[index]*1e-4,
                          report.ctfData.astigmatism[index]*1e-4,
                          report.ctfData.resolution[index],
                     ...

* Re-run the summary monitor, check the table and voila! Defocus column is gone:

  .. figure:: /docs/images/html_report_tutorial/mic_table_without_defocus.png
     :align: center
     :alt: mic table without defocus


3. Adding a column to defocus table
-------------------------------------

In this section, we'll add the fit quality value to the micrograph table.
As we have seen in the beginning of the previous example, the template has some
keywords that are used by Scipion to provide data to the HTML report.
In this example, we'll see where Scipion generates that data and modify it.
Pay attention to the last step of example 2: the data of the defocusU column is
accessed with `report.ctfData.defocusU[index]*1e-4`.
In the report variable, we see that `ctfData` is assigned a keyword to be
replaced by Scipion:

`pyworkflow/templates/execution.summary.template.html
<https://github.com/I2PC/scipion/blob/master/pyworkflow/templates/execution.summary.template.html#L301>`_:

.. code-block:: javascript

    var report ={
        date:"%(dateStr)s",
        project:"%(projectName)s",
        scipionVersion:"%(scipionVersion)s",
        acquisition:[
            %(acquisitionLines)s
        ],
        runs:[
            %(runLines)s
        ],
        ctfData: %(ctfData)s, // we need to find how does scipion generate this ctfData
        movieGainData: %(movieGainData)s,
        systemData: %(systemData)s
    }

The place where Scipion performs the replacement of all the `%(keywords)s` is in
`pyworkflow/em/protocol/monitors/report_html.py
<https://github.com/I2PC/scipion/blob/d1a60f69960d1079bbbecde5bf3f5f4017b36927/pyworkflow/em/protocol/monitors/report_html.py#L392>`_.

* First, we can take a look at which data is available in the monitor's input
  protocols. In our case, the fit quality is in the SetOfCtf. We can click on
  CTFFIND's **`Analyze results`** button to open its output (or double click in
  any output set). Then we can inspect all the data available for this set by
  clicking on **Display -> Columns**.

  .. figure:: /docs/images/html_report_tutorial/set_of_ctf_columns.png
     :align: center
     :alt: set of ctf columns

* Next, we need to add the `_fitQuality` field to ctfData. Lets look for it in
  `report_html.py <https://github.com/I2PC/scipion/blob/d1a60f69960d1079bbbecde5bf3f5f4017b36927/pyworkflow/em/protocol/monitors/report_html.py#L448>`_:

  .. code-block:: python

    args = {'projectName': projName,
            'startTime': pwutils.dateStr(project.getCreationTime(), secs=True),
            'dateStr': pwutils.prettyTime(dt=tnow, secs=True),
            'projectDuration': pwutils.prettyDelta(tnow-project.getCreationTime()),
            'projectStatus': "FINISHED" if finished else "RUNNING",
            'scipionVersion': os.environ['SCIPION_VERSION'],
            'acquisitionLines': acquisitionLines,
            'runLines': runLines,
            'ctfData': ctfData,  ############## WE LOOK FOR THIS ##################
            'movieGainData': movieGainData,
            'systemData': systemData,
            'refresh': self.refreshSecs
            }

  .. code-block:: python

    ctfData = json.dumps(data)  ####### NOW WE LOOK FOR "data" ########

  .. code-block:: python

    data = {} if self.ctfMonitor is None else self.ctfMonitor.getData()  ####### Lets check whats in this getData() ########

  `pyworkflow/em/protocol/monitors/prototol_monitor_ctf.py
  <https://github.com/I2PC/scipion/blob/d1a60f69960d1079bbbecde5bf3f5f4017b36927/pyworkflow/em/protocol/monitors/protocol_monitor_ctf.py#L246>`_

  .. code-block:: python

    def getData(self):
        def get(name):
            try:
                self.cur.execute("select %s from %s" % (name, self._tableName))
            except Exception as e:
                print("MonitorCTF, ERROR reading data from db: %s" %
                      os.path.join(self.workingDir, self._dataBase))
            return [r[0] for r in self.cur.fetchall()]

        data = {
            'defocusU': get('defocusU'),
            'defocusV': get('defocusV'),
            'astigmatism': get('astigmatism'),
            'ratio': get('ratio'),
            'idValues': get('ctfID'),
            'resolution': get('resolution'),
            'fitQuality': get('fitQuality'),   ###### FIT QUALITY IS ALREADY HERE!!! YAY ########
            'imgMicPath': get('micPath'),
            'imgPsdPath': get('psdPath'),
            'imgShiftPath': get('shiftPlotPath')
         }
        # conn.close()
        return data

* Now we just need to add it at the same place where we previously deleted de DefocusU.

  - First we add a name for the column:

    `pyworkflow/templates/execution.summary.template.html
    <https://github.com/I2PC/scipion/blob/master/pyworkflow/templates/execution.summary.template.html#L301>`_:

    .. code-block:: python

        if ('defocusU' in report.ctfData){
            cols.push(
                      {"title": "Fit Quality",
                       "render": $.fn.dataTable.render.number( ',', '.', 2)},
                      {"title": "Astigmatism (µm)",
                       "render": $.fn.dataTable.render.number( ',', '.', 3)},

  - Then add data to the rows:

    .. code-block:: python

        if ('defocusU' in report.ctfData){
            rowValues.push(
                           report.ctfData.fitQuality[index],
                           report.ctfData.astigmatism[index]*1e-4,
                           report.ctfData.resolution[index],

* Run the summary again and check that we have our new column:

  .. figure:: /docs/images/html_report_tutorial/mic_table_with_fit_quality.png
     :align: center
     :alt: mic table with fit quality



