#!/usr/bin/env python
"""Initial rehack in python of Rancher Installation CI file"""

import os
import subprocess
import shlex
import tarfile
import shutil

RANCHER_BASE_FILENAME = 'rancher-linux-amd64-'
RANCHER_BASE_URL = 'https://github.com/rancher/cli/releases/download/'

#--------------------------------------------------------------------------------------

def called_command_line_output(command_string):
    """Cleans and then calls a command line command"""
    output = shlex.split(command_string)
    return subprocess.call(output)

def untarred_file(filename):
    """Takes a tarred file and extracts its contents into a folder of the same name"""
    tar = tarfile.open(filename)
    tar.extractall()
    tar.close()

#--------------------------------------------------------------------------------------

def rancher_install(version='v0.6.1'):
    """Installs chosen Rancher version in current folder and cleans up"""
    if not os.path.isfile('./rancher'):
        # define some local variables
        rancher_file_name = '{}{}.tar.gz'.format(RANCHER_BASE_FILENAME, version)
        rancher_url = '{}{}/{}'.format(RANCHER_BASE_URL, version, rancher_file_name)

        print('Installing Rancher ({})'.format(version))
        # continuing to use cURL here as not sure the best way to replace
        # its functionality in python yet. This needs to be changed as defeats point
        # of porting to python...
        called_command_line_output('curl -Ls -o {} {}'.format(rancher_file_name, rancher_url))
        # untar the file and clean up where it lives - there is probably a unified way of doing this
        untarred_file(rancher_file_name)
        # move rancher file to base folder
        shutil.move('./rancher-{}/rancher'.format(version), './')
        # clean up leftover tar file and folder
        shutil.rmtree('./rancher-{}'.format(version))
        os.remove(rancher_file_name)
        return print('Finished installing Rancher ({})'.format(version))
    return print('Rancher already installed')

#--------------------------------------------------------------------------------------

if __name__ == '__main__':
    rancher_install()
