from .ssalad_ClusterAnalysis import *
from .Molclustpy_visualization_funcitons import *
from SpringSaLaDpy.input_file_extraction import read_input_file
from SpringSaLaDpy.time_rounder import find_nearest_time
from SpringSaLaDpy.data_locator import *

def plot(search_directory, times, bins=[]):
    
    if os.path.split(search_directory)[1][-7:] == '_FOLDER':
        plotting_path = search_directory
    else:
        plotting_path = os.path.join(search_directory, os.path.split(search_directory)[1][:-12] + '_FOLDER')

    input_file = find_txt_file(plotting_path)

    #Round to nearest available time based on dt_data value
    _, split_file = read_input_file(plotting_path)
    dt_data = float(split_file[0][4][9:])
    total_time = float(split_file[0][1][12:])

    rounded_times = []
    for time in times:
        rounded_time = float(find_nearest_time(search_directory, ['data', 'Run0'], time, dt_data, 'Clusters_Time')[0])
        if rounded_time <= total_time and not rounded_time < 0:
            rounded_times.append(rounded_time)

    if times == []:
        rounded_times.append(total_time)

    ca = ClusterAnalysis(input_file)
    ca.getMeanTrajectory(SingleTraj=False)
    ca.getSteadyStateDistribution(SS_timePoints=rounded_times)

    plotClusterDistCopy(plotting_path, rounded_times, bins)