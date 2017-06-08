#!/usr/bin/env python
# Written by Qusai Abu-Obaida
"""This script writes the execution file and the list of AOCV files for each lib in order to run validate all check"""
import glob
import os
import itertools
from collections import defaultdict

def main():
    # deletes old files from previous run
    old_files = glob.glob('um*_files')
    for old in old_files:
        os.remove(old)
    if os.path.isfile("validation_run.sh"):
        os.remove("validation_run.sh")

    # gets aocv files
    aocv_files = glob.glob("AOCV_*/*.aocv")
    grouped_files = defaultdict(list)
    for x in aocv_files:
        grouped_files[(os.path.basename(x)).split("_")[0]].append(x)
    # creates the execution file
    exec_file = open("validation_run.sh", 'w+')
    for library, files in grouped_files.items():
        # creates a separate list of full path files for each library
        files_list = open("%s_files" % library, 'w+')
        for i in files:
            files_list.write(os.path.abspath(i))
            files_list.write("\n")
        # full path for the library folder
        library_folder = os.path.abspath(library)
        # writes the commands to the execution file
        command = "/slowfs/us01dwt3p268/proj_ref_flows/TOOLS/AOCVM/aocv_validation_all -file_list %s_files -libsrc " \
                  "%s/liberty/logic_synth/" % (library_folder, library_folder)
        exec_file.write(command + '\n')
    os.system('chmod +x validation_run.sh')
    print ('''execution file created: validation_run.sh

Don't forget to use settdk''')


if __name__ == '__main__':
    main()
