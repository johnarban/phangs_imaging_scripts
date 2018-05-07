# This script runs the calibration scripts, first making sure that any
# additional flagging commands are added to the queue.

# Note that this is a pure python script. It *calls* casapy but it
# should not be run inside CASA.

# Edit the "Control Flow" section to use the script.

import os
import phangsPipelinePython as pp
import glob

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Control Flow
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# ... a text list. The script will process only these galaxies.

only = ['ngc6300']

# ... skip these galaxies

skip = []

# ... set as '12m' or '7m'. Leave it as None to process all data.

just_array = ['7m']

# Steps

overwrite_previous = True
update_flags = False
run_calibration = False
just_print_commands = True

# Flag sets whether to only run scripts when there is no calibrated data

do_only_new = False

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Define various routines and functions
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Run the script
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

gals = pp.list_gal_names()

array_list = ['12m', '7m']

# starting directory
base_dir = os.getcwd()+'/'

# get the galaxy name and array and directory list

for gal in gals:
    
    if len(only) > 0:
        if only.count(gal) == 0:
            print "Skipping "+gal
            continue
    if len(skip) > 0:
        if skip.count(gal) > 0:
            print "Skipping "+gal
            continue

    for array in array_list:
        
        if len(just_array) > 0:
            if just_array.count(array) == 0:
                print "Skipping "+array
                continue
        
        uvdata_dict = pp.get_uvdata_key(
            gal=gal,
            just_array=array)
        
        for this_dir in uvdata_dict.keys():
            
            target_dir = base_dir + this_dir

            # change directory to the relevant directory

            os.chdir(target_dir)           

            # test if the calibrated/ directory is present.
            has_calibrated = len(glob.glob('calibrated/')) > 0

            # if present and requested remove the calibrated data, else fast forward
            if has_calibrated:
                if overwrite_previous == False:
                    print ""
                    print "... for directory: " + this_dir
                    print "... calibrated/ directory exists and overwrite_previous set to False."
                    print "... skipping this directory.."
                    print ""
                    continue
                else:
                    command = 'rm -rf calibrated/'
                    if just_print_commands:
                        print "I would run: " + command
                    else:
                        print command
                        os.system(command)
            
            # edit the flagging file used for the pipeline run
            
            # TBD
                        
            # run the calibration script with a non-interactive command call to CASA

            os.chdir('script/')
            pipescript_name = glob.glob('*.casa_pipescript.py')
            if len(pipescript_name) == 0:
                print ""
                print "... for directory: " + this_dir
                print "... no pipeline script found. Proceeding to next directory."
                print ""
            casa_command = 'casapipe-5.1.1 -c '
            command = casa_command + pipescript_name[0]
            if just_print_commands:
                print "I would run: " + command
            else:
                print command
                os.system(command)
            

# go back to the original directory
os.chdir(base_dir)
