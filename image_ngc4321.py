# &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%
# PREPARATION AND CONTROL FLOW
# &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%

# --------------------------------------
# User inputs
# --------------------------------------

out_root = 'ngc4321'
tag = '956'
phase_center = 'J2000 12h22m54.8s +15d49m19s'
source_vel_kms = 1571
vwidth_kms = 500

calibrated_files = {'12m_1':'../../2015.1.00956.S/science_goal.uid___A001_X2fb_X2b7/group.uid___A001_X2fb_X2b8/member.uid___A001_X2fb_X2b9/calibrated/calibrated_final.ms',
                    '12m_2':'../../2015.1.00956.S/science_goal.uid___A001_X2fb_X2c1/group.uid___A001_X2fb_X2c2/member.uid___A001_X2fb_X2c3/calibrated/calibrated_final.ms',
#                    '7m_1':'',
#                    '7m_2':''
                    }

# --------------------------------------
# Overall control flow
# --------------------------------------

execfile('../scripts/line_list.py')

# Extract data
script_copy = False
script_extract_co21 = False
script_extract_c18o21 = False
script_extract_continuum = False

# Image data
script_image_chan0 = False
script_image_cube = True

script_image_co21 = True
script_image_c18o21 = False
script_image_cont = False

# &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%
# EXTRACTION
# &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%

# --------------------------------------
# Copy the data
# --------------------------------------

if script_copy:
    do_copy = True
    do_split = True
    do_extract = False
    do_combine = False
    execfile('../scripts/extractLineData.py')

# --------------------------------------
# Extract line data
# --------------------------------------

# 12CO 2-1
linetag = 'co21'
restfreq_ghz = line_list[linetag]
chan_dv_kms = 2.5

if script_extract_co21:
    do_copy = False
    do_split = False
    do_extract = True
    do_combine = True
    execfile('../scripts/extractLineData.py')

# C18O 2-1
linetag = 'c18o21'
restfreq_ghz = line_list[linetag]
chan_dv_kms = 5.0

if script_extract_c18o21:
    do_copy = False
    do_split = False
    do_extract = True
    do_combine = True
    execfile('../scripts/extractLineData.py')

# --------------------------------------
# Extract continuum data
# --------------------------------------

if script_extract_continuum:
    do_recopy = True
    do_flag = True
    do_average = True
    do_statwt = True
    lines_to_flag = lines_co+lines_13co+lines_c18o
    execfile('../scripts/extractContinuum.py')

# &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%
# IMAGING
# &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%

# --------------------------------------
# Image channel 0
# --------------------------------------

if script_image_chan0:
    
    if script_image_co21:
        do_end_to_end = True
        do_start_with_pbmask = True
        input_vis = 'ngc4321_956_co21_chan0.ms'
        cube_root = 'ngc4321_co21_chan0'
        uvtaper = None
        linetag = 'co21'
        specmode = 'mfs'
        restfreq_ghz = line_list[linetag]
        execfile('../scripts/imageImage.py')

    if script_image_c18o21:
        do_end_to_end = True
        do_start_with_pbmask = True
        input_vis = 'ngc4321_956_c18o21_chan0.ms'
        cube_root = 'ngc4321_c18o21_chan0'
        uvtaper = None
        linetag = 'c18o21'
        specmode = 'mfs'
        restfreq_ghz = line_list[linetag]
        execfile('../scripts/imageImage.py')

    if script_image_cont:
        do_end_to_end = True
        do_start_with_pbmask = True
        input_vis = 'ngc4321_956_cont.ms'
        cube_root = 'ngc4321_cont'
        uvtaper = None
        specmode = 'mfs'
        restfreq_ghz = ''
        execfile('../scripts/imageImage.py')

# --------------------------------------
# Image cubes
# --------------------------------------

if script_image_cube:

    if script_image_co21:
        do_end_to_end = True
        do_start_with_pbmask = False
        
        input_vis = 'ngc4321_956_co21.ms'
        cube_root = 'ngc4321_co21'
        uvtaper = None
        linetag = 'co21'
        specmode = 'cube'
        restfreq_ghz = line_list[linetag]

        execfile('../scripts/imageImage.py')

    if script_image_c18o21:
        do_end_to_end = True
        do_start_with_pbmask = False
        
        input_vis = 'ngc4321_956_c18o21.ms'
        cube_root = 'ngc4321_c18o21'
        uvtaper = None
        linetag = 'c18o21'
        specmode = 'cube'
        restfreq_ghz = line_list[linetag]

        execfile('../scripts/imageImage.py')
