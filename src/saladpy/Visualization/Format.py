import os
from saladpy.data_locator import find_txt_file
from saladpy.input_file_extraction import read_input_file
from saladpy.time_rounder import find_nearest_time
from .times_2_title import times_2_title

#Switch to the _FOLDER folder if you're not already there and round times to the nearest available values.
def format(search_directory, times):
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
        rounded_time = float(find_nearest_time(plotting_path, ['data', 'Run0'], time, dt_data, 'Clusters_Time')[0])
        if rounded_time <= total_time and not rounded_time < 0:
            rounded_times.append(rounded_time)

    if times == []:
        rounded_times.append(total_time)

    title_str = times_2_title(rounded_times)

    return input_file, rounded_times, plotting_path, title_str
