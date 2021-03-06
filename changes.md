# Salstat – Changes

This file outlines the changes that have occurred in the development of the SalStat statistics package.

## Version:

### salstat.20140516 (code: "Louise")

* Fixed CSV import bug that only imported a sample of data
* Fixed bugs with grid's column & row deletion / insertion
* Handles unicode input, analysis, output and charts (now handles downloads from data.un.org)
* Hidden tabs
* Fixed chart's legend placement bugs
* Charts can use a variable as x-axis labels (e.g., years)
* Removed unecessary files

### salstat.20140507 (code: "Jell")

* Now uses charts (courtesy of HighCharts)
* Does cross-tabulations (crosstabs)
* Has a range of descriptive statistics (including 9 forms of quantile)
* Re-designed descriptives dialog
* Imports CSV better
* Also imports Excel (.xls, .xlsx), Libre Office (.ods), SAS (version 8+) and HTML tables from file
* Scrapes HTML tables from URLs
* Many other fixes

### 20030911 (codenamed 'Texas!')

1. Replaced he wxPlotCanvas with the wxPyPlot module. Save As... works now along with print previews, setup and printing.
2. Added transformations dialog box. It should work too!

### 20030513 (codenamed "Watchdog")

1. Removed SciPy's plt feature, replaced with a modified wxPlotCanvas;

### 20030311 (codenamed "Abacus")

1. Added chi square test.
2. Hacked the GUI a bit more to make it slightly better - works best on Windows.
3. Added the SciPy plt graphing features - allows plots that are reasonable. Can be saved as BMP's, JPEG's, PNG's or TIFF's.

### 20021105 (codenamed "Pugh")

Big changes made to SalStat:
1. Now has an init file created in the users home directory to keep user defined sizes and positions (sod the registry!). Also contains the last few files accessed and the last directory - that sort of thing.
2. Scripting - SalStat is now more powerful with the addition of scripting, using Python. Access this by going to the menu, click on "Analyse", then select "Scripting Window". Type in some Python stuff, and see the output on the html window - see the manual for more details on how to access the statistical functions of the SalStat scripting API. Users can access the data on the grid, descriptive stats and all the tests available. This enables people to write their own tests.
3. Graphs / Charts - very basic bar charts are available. Sorry no export yet which only makes them good for checking the data, but this will be extended in the future to make them better.
4. Bug fixes - the bug that arose when getting descriptives should have been fixed.
5. The manual has been re-written and is more extensive in its coverage with screenshots and the suchlike. There is a pdf and plain text version included in the release.
6. Availability of all-in-ones - Windows and Linux now has single downloadable files which means that users don't have to download and install Python and wxPython if they don't want to - all the necessary files are included. Obviously the size of the files is much larger, but this is hard to avoid. The Python source code is also included, as is the manual in pdf and html format.
7. General code cleanups, minor bugfixes and hopefully more help documentation should also be available. The scripting facility also has its own help pages (in the normal place! Just click on help and have a look at what's there).
8. (maybe) simple effects on the anova and their nonparametric equivilents? If this has been done, it is intended to be one of the most usable aspects, so please test this and let me know what you think.
9. The output of analyses may be printed
10. Interface cleanup - the dialogs should now look a lot better than they did before!
11. Number of missing data is now shown.

### 20020803 (release 03/08/2002 codenamed "storm")

Fixed small bug in between subjects anova and added Cochranes Q test. Named
"storm" cos there is a storm outside right now.

### 20020702 (release 02/07/2002 codenamed "Dave")

Rewrote code in an OO fashion. Much faster and smaller now!

### 20020611 (release 11/06/2002)

Improved hypertext help system: Buttons now work, and the help documentation
(under topics) is better (even complete?)

### 20020606 (release 06/06/2002)

Added Friedmans test, 2 sample sign test, and f test for variance ratios. Help
has been extended with entries about tests.

### 20020601 (release 01/06/2002)

Not much difference from the last version, but a few "help" pages have been added.

### 20020514 (release 14/05/2002)

anova routines now work better - only columns selected by the user are used. Save data now works better, although data needs to be "blocked" (ie, no empty spaces). Nominal descriptives have been added.

### 20020505 (release 05/05/2002)

Added one sample sign test and single factor within subjects anova - anova has been tested against results from SPSS and a book, and are accurate, but further testing would still be appreciated. CSV data (Comma Separated Values - where data are separated by commas) can also be loaded via a nice little hack courtesy of Python.

