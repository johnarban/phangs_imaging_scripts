execfile('../scripts/header_ngc4321south.py')
execfile('../scripts/line_list.py')

do_use_pbmask = False
linetag = 'co21'
specmode = 'cube'    
restfreq_ghz = line_list[linetag]
max_loop = 20
pb_limit = 0.25
uvtaper = None    

input_vis_7m = 'ngc4321south_7m_co21.ms'
cube_root_7m = 'ngc4321south_co21_7m'

input_vis_combo = 'ngc4321south_956_co21.ms'
cube_root_combo = 'ngc4321south_co21_12m+7m'

input_vis_12m = 'ngc4321south_12m_co21.ms'
cube_root_12m = 'ngc4321south_co21_12m'

do_image_7m = True
do_image_combo = True
do_image_12m = True

smallscalebias_7m = 0.6
smallscalebias_combo = 0.8
smallscalebias_12m = 0.8

execfile('../scripts/phangsImagingPipeline.py')
