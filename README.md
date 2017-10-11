# Scripts Contained
* __CSVmaker/extractLines__: Extract specific lines of an input file. (Shell x2)
  * extractLines: uses top and head. Slower method.
  * extractLines2: uses sed. Faster method.
* __CSVmaker/generateCSV__: Generate a CSV of any number of rows and columns. (Shell)
* __CSVmaker/maxOfColumn.py__: Find the maximum value of a column in a CSV. (Python x3)
  * maxOfColumn.py: uses a dictionary. 3rd fastest for lots of rows, 2nd fastest for lots of columns (but incorrect).
  * maxOfColumn2.py: uses a regex. 2nd fastest for lots of rows, times out for lots of columns.
  * maxOfColumn3.py: uses .split(). 1st place for both categories.
* __bigFileMaker/generateFile__: Generate a file of any number of lines.
* __massFileMaker/massTouch__: Generate any number of files.
* __filenamesContaining__: List all filenames containing a string. (Shell)
* __filesContaining__: List all files containing a string. (Shell)
* __listTxts__: List first 5 lines of all .txt files. (Shell)
* __numFilesContaining, numFilesContainingPython__: Count number of files containing a string. (Shell/Python)
* __renameExt__: Rename all file extensions. (Shell)
