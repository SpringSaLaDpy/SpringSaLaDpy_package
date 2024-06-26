import numpy as np
from .ClusterCrossLinking import CrossLinkIndex
from .times_2_title import *
from saladpy.data_locator import *
from saladpy.input_file_extraction import read_input_file
from saladpy.time_rounder import find_nearest_time

def plot(search_directory, times, hist=False):     
    #txtfile = r"Examples\Nephrin-Nck-NWasp\Final_version_test_SIMULATIONS\Simulation0_SIM_SIMULATIONS\Simulation0_SIM_FOLDER\Simulation0_SIM.txt"
    #vf = r'Examples\Nephrin-Nck-NWasp\Final_version_test_SIMULATIONS\Simulation0_SIM_SIMULATIONS\Simulation0_SIM_FOLDER\viewer_files\Simulation0_SIM_VIEW_Run2.txt'

    if os.path.split(search_directory)[1][-7:] == '_FOLDER':
        plotting_path = search_directory
    else:
        plotting_path = os.path.join(search_directory, os.path.split(search_directory)[1][:-12] + '_FOLDER')
    
    txtfile = data_file_finder(plotting_path, [], search_term='.txt')
    vf = data_file_finder(plotting_path, ['viewer_files'], run = 0)

    #ss_tps = np.arange(0.02, 0.05+0.01, 0.01)

    #AS = ["PRM", "SH3_1", "SH3_2","SH3_3","SH2","pTyr_1_2", "pTyr_3"]  # active sites

    #AS = ['sh3', 'prm']
    #AS = ['SH3', 'PRM', ]

    #Round to nearest available time based on dt_data value
    _, split_file = read_input_file(os.path.split(txtfile)[0])
    dt_data = float(split_file[0][4][9:])
    total_time = float(split_file[0][1][12:])

    rounded_times = []
    for time in times:
        rounded_time = float(find_nearest_time(plotting_path, ['data', 'Run0'], time, dt_data, 'Clusters_Time')[0])
        if rounded_time <= total_time and not rounded_time < 0:
            rounded_times.append(rounded_time)

    if times==[]:
        rounded_times.append(total_time)

    title_str = times_2_title(rounded_times)

    CLI = CrossLinkIndex(txtfile, ss_timeSeries=rounded_times)

    print(CLI)
    #d = cl.mapSiteToMolecule()
    #rif = ReadInputFile(txtfile)
    #print(rif.getReactiveSites())
    #print(len(cl.getActiveSiteIDs())) 
    CLI.getSI(vf) 
    CLI.getSI_stat() 
    CLI.plot_SI_stat(color='k', fs=16, xticks=None, yticks=None, hist=hist, title_str=title_str)
    #CLI.plot_SI_stat(color='c', xticks=None, yticks=None)