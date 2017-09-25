#! /usr/bin/python
'''
THIS CODE IS ONLY FOR PYTHON VERSION 3
***************************************************************************************
Objective: Utility Script - To count Actual Lines of Code in a file.
Notes: Counts LOC, single/multi line comments, blank lnes, for 'javascript, python, ruby, java'
Usage: python countLOC_python_v3.py
---------------------------------------------------------------------------------------
History:     Date:               Author:                 Update / Comments
---------------------------------------------------------------------------------------
1)       27th Jul 2014      Roland Castelino           Initial creation. supports javascript file
2)       19th Oct 2014      Roland Castelino           Added support for ruby, python, java (dictonary created)
                                                       Minor code changes
***************************************************************************************
'''

import os, sys

# Files accepted: javascript, ruby, python, java
fileType = ['.js', '.rb', '.py', '.java']
myPath = os.path.abspath(os.path.dirname(sys.argv[0]))
lang_dictonary = {
    '.js':{
            'language'      : "javascript",
            'multi_start'   : "/*",
            'multi_end'     : "*/",
            'single_line'   : "//",    
        },
    '.rb':{
            'language'      : "ruby",
            'multi_start'   : "=begin",
            'multi_end'     : "=end",
            'single_line'   : "#",                
        },
    '.py':{
            'language'      : "python",
            'multi_start'   : "'''",
            'multi_end'     : "'''",
            'single_line'   : "#",    
        },
    '.java':{
            'language'      : "java",
            'multi_start'   : "/*",
            'multi_end'     : "*/",
            'single_line'   : "//",     
        }
    }


def get_code_language():
    key = ''
    for code in list(lang_dictonary.keys()):
        if ext == code:
            key = code
            break
    return lang_dictonary[key]


def read_line_count(fname):
    code_type = get_code_language()

    # Counters to calculate Lines
    countBlank = 0
    countComments = 0
    countCommentsBlock = 0
    countTotalLOC = 0
    countTotalLines = 0
    multiCount = 0
    
    # Lines stored in an array
    myLines = open(fname).readlines()
    myNewLines = []

    # to make True when Comment Block encountered
    boolCommentBlock = False;
    countTotalLines = len(myLines)
    # Calculate number of Comments, Comment Blocks, Blank Lines, LOC
    for line in myLines:
        line = line.strip()
        if not boolCommentBlock and line.startswith(code_type['multi_start']):
            boolCommentBlock = True
            countCommentsBlock += 1
        elif(not boolCommentBlock):
            if line.startswith(code_type['single_line']):
                countComments += 1
            elif len(line.strip())>0:
                countTotalLOC += 1
            else:
                countBlank += 1
        # make boolCommentBlock False when '*/' encountered
        elif boolCommentBlock and line.startswith(code_type['multi_end']) or line.find(code_type['multi_end'])>=0:
            boolCommentBlock = False
    
    multiCount = countTotalLines - countComments - countTotalLOC - countBlank
    print("File ---> ",path[len(myPath):].split("/")[-1]," ---> ",code_type['language'])
    print("Single line comment   :", countComments)
    if multiCount == 0:
        print("Multi line block      :", countCommentsBlock)
    else:
        print("Multi line block      :", countCommentsBlock, " (", multiCount,") comment lines in block")
    print("Empty or Blank lines  :", countBlank)
    print("Actual lines of Code  :", countTotalLOC)
    print("Total lines in file   :", countTotalLines)

    return countTotalLOC


if __name__ == '__main__':
    print("******************************************")
    total_loc_count = 0
    file_count = 0
    for base, dirs, files in os.walk(myPath):
        for file in files:
            # Check the sub directorys
            if file.find('.') < 0:
                continue
            ext = (file[file.rindex('.'):]).lower()
            try:
                if fileType.index(ext) >= 0:
                    file_count += 1
                    path = (base + '/'+ file)
                    c = read_line_count(path)
                    print("------------------------------------------")
                    print(".%s : %d" % (path[len(myPath):], c))
                    print("------------------------------------------\n")
                    total_loc_count += c
            except:
                pass
print('Number of Files : %d' % file_count)
print('Total Actual Lines of Code : %d' % total_loc_count)
print("******************************************")