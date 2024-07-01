import os
from saladpy.data_locator import find_txt_file
from saladpy.input_file_extraction import read_input_file
from saladpy.time_rounder import find_nearest_time
from .times_2_title import times_2_title

#Switch to the _FOLDER folder if you're not already there and round times to the nearest available values.
def format(search_directory, times):

    input_file = find_txt_file(search_directory)

    #Round to nearest available time based on dt_data value
    _, split_file = read_input_file(search_directory)
    dt_data = float(split_file[0][4][9:])
    total_time = float(split_file[0][1][12:])
    total_time = total_time - (total_time % dt_data)

    rounded_times = []
    for time in times:
        rounded_time = float(find_nearest_time(search_directory, ['data', 'Run0'], time, dt_data, 'Clusters_Time')[0])
        if rounded_time <= total_time and not rounded_time < 0:
            rounded_times.append(rounded_time)

    if times == []:
        rounded_times.append(total_time)

    title_str = times_2_title(rounded_times)

    return input_file, rounded_times, title_str
