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
import platform

def checkOS():
    """ check the operating system """

    if not (platform.system() == 'Windows'):
        sys.exit(0)

def fetchFTP(ftpURL,directory,fileName):
    """ fetches the ftpURL file """

    if(not fsecureFileExist(fileName)):
        try:
            print('standalone is being downloaded')
            ftp = FTP(ftpURL)
            ftp.login()
            ftp.cwd(directory)
            ftp.retrbinary('RETR ' + fileName, open(fileName, 'wb').write)
            ftp.quit()
        except:
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

def fsecureFileExist(testFile):
    """ check if the file exist """

    currentDirectory = os.path.split(os.path.realpath(os.sys.argv[0]))[0]

    return os.path.isfile(os.path.join(currentDirectory, testFile))


ftpURL = 'ftp.f-secure.com'
directory = 'support/tools/fsdiag'
fileName = 'fsdiag_standalone.exe'
path_to_desktop = os.path.join(os.environ['USERPROFILE'],'Desktop')

checkOS()
fetchFTP(ftpURL,directory,fileName)
flag = openOtherProgram()
if flag:
    runStandAlone(fileName)

if os.path.isfile(os.path.join(path_to_desktop, 'fsdiag.7z')):
    print('fsdiag.7z exists on Desktop')
else:
    print('fsdiag.7z does not exists on Desktop')

sys.exit(0)
