from .ssalad_ClusterAnalysis import *
from .Molclustpy_visualization_funcitons import *
from .Composition_calculator import composition_calc
from .Format import format

def plot(search_directory, times, bins=[]):
    
    input_file, rounded_times, _, title_str = format(search_directory, times)

    ca = ClusterAnalysis(input_file)
    ca.getMeanTrajectory(SingleTraj=False)
    ca.getSteadyStateDistribution(SS_timePoints=rounded_times)

    composition_calc(search_directory, title_str, bins)