#!/usr/bin/env python3

import shutil
import os

def main():
    os.chdir('/Users/mstarling/Documents/repos/mycode/')
    shutil.move('raynor.obj', 'ceph_storage/')

    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
main()