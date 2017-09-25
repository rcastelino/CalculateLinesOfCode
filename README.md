# Introduction - Calculate 'Actual' Lines Of Code

Python script: useful utility to calculate lines of code for all major languages (java, ruby, objective-c, python, javascript)

## Objective: 
Anyone who writes code wants to have less lines to meet the objective of the program. This utility script helps to identifying real lines of code and prints to console:
- type of file and language
- comments (single and multi-line)
- empty / blank lines
- actual lines of code
- total LOC; for each file in the directory.

## Usage:
- on MacOS / Linux, simply copy the executable in the code root direcotry and execute it (double click). 
- on Windows, copy the .py file in the code root directory and execute it via command prompt. (Pre-req - python.exe to be installed. More details --> https://docs.python.org/3/faq/windows.html)

## Supports Python version 2 and 3

## Sample Console Output
(This output is when executed from a directory having .py and .java file)

******************************************

File --->  countLOC_python_v3.py  --->  python

Single line comment   : 8

Multi line block      : 1  ( 14 ) comment lines in block

Empty or Blank lines  : 13

Actual lines of Code  : 96

Total lines in file   : 131

./countLOC_python_v2.py : 96

------------------------------------------

File --->  sampleTestFile.java  --->  java

Single line comment   : 21

Multi line block      : 2  ( 19 ) comment lines in block

Empty or Blank lines  : 28

Actual lines of Code  : 110

Total lines in file   : 178

./sampleTestFile.java : 110

------------------------------------------


Number of Files : 2

Total Actual Lines of Code : 206

******************************************

# MIT License

Copyright (c) 2017 Roland Castleino

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.