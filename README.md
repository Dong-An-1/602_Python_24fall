EC602 Fall 2024

Assignment One

Posted: September 17, 2024 (in this document)
Due: October 1, 2024



Details
-------

Groups of 1, 2, or 3

Assignment value: one of 10 required weekly assignments.


Assignment Description
----------------------

Title: Searcher

Write an executable (command line) script that explores the 
current directory and reports on matching files.

This report will go to the terminal (stdout).


Example:


```
searcher filename-pattern
```

```
searcher -c text-to-search
```

```
searcher -t xlsx
```

```
searcher --date   startdate-enddate
```

These are combinable, with AND logic

```
searcher -c "sys.argv" --date 2021-2023 "*.py"
```

Note: this could be an extension or the built-in file type


Optional / Extra Credit Parts
-----------------------------
