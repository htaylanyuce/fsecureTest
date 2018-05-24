#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 19:56:45 2018

@author: hamit taylan
"""

from ftplib import FTP
import webbrowser as wb
import subprocess
import os
import sys
from pathlib import Path
import tkinter
from tkinter import messagebox

ftpURL = 'ftp.f-secure.com'
directory = 'support/tools/fsdiag'
fileName = 'fsdiag_standalone.exe'

def fetchFTP(ftpURL,directory,fileName):
    """ fetches the ftpURL file """

    if(not fileTest(fileName)):
        try:
            print('file does not exist')
            ftp = FTP(ftpURL)
            ftp.login()
            ftp.cwd(directory)
            ftp.retrbinary('RETR ' + fileName, open(fileName, 'wb').write)
            "ftp.retrbinary(fileName, open(fileName, 'wb').write)"
            ftp.quit()
        except:
            "print(e)"
            print('Connection Error')
            sys.exit('Cannot fetch file')

def openOtherProgram():
    """ run a program other than standalone program
        -  run Internet explorer, if not
        -  run a cmd
    """

    flag = False

    try:
        ie = wb.get(wb.iexplore)
        ie.open('fsecure.com')
        flag = True
    except:
        try:
            subprocess.call('start', shell=True)
            flag = True
        except:
            flag = False
    return flag

def runStandAlone(fileName):
    """ run the standalone file fetched from fsecure ftp """

    p = subprocess.Popen(fileName, shell=True)
    p.communicate()

def fileTest(testFile):
    """ check if the file exist """

    currentDirectory = os.getcwd()
    path = Path(currentDirectory + str('/') + testFile)

    return path.is_file()

def showBox(testFile):
    """ open the messagebox to show whether we have file in the same directory"""

    root = tkinter.Tk()
    root.withdraw()
    doesFileExist = fileTest(testFile)
 
    if doesFileExist:
        messagebox.showinfo("File "+testFile+ " exists!", "Success")
    else:
        messagebox.showinfo("File "+testFile+ " does not exist", "Failure")

fetchFTP(ftpURL,directory,fileName)
flag = openOtherProgram()
if flag:
    runStandAlone(fileName)

showBox('fsdiag.7z')

sys.exit(0)

