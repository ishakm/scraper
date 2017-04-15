# Scraper

Type: `python scraper.py` to run the python script.

Downloads lecture files from CS61A course (http://cs61a.org/) with Windows Task Scheduler. Stay on track without having to download lecture files every week.

The method to schedule a Python script depends on your operating system. The general steps for Windows operating systems are given below. 
For more information about scheduled tasks, see the Windows help. For Unix and Linux systems, use [cron or crontab](https://kb.iu.edu/d/afiz).

For more information on running a script or model at a prescribed time, see the blog post [Scheduling a Python script or model to run at a prescribed time](https://blogs.esri.com/esri/arcgis/2013/07/30/scheduling-a-scrip/).

### Scheduling Tasks

1. Open the Task Scheduler wizard.
    1. Click the Windows **Start** menu, click **Control Panel > Administrative Tools** and click **Task Scheduler**.
    
        Note: If **Control Panel** is in category view, click **System and Security**, click **Administrative Tools**, then click **Task Scheduler**.
    
2. Double-click **Add Scheduled Task** (or **Create Basic Task**).
3. Complete the options on the wizard. 
These options include when you want the scheduled task to run, the path to the script you want to run, and any arguments to the script. Run scheduler **every 2 days** in order to correspond with lecture days.
