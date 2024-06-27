from .ssalad_ClusterAnalysis import *
from .Molclustpy_visualization_funcitons import *
from .Format import format

def plot(search_directory, times, bins=[]):
    
    input_file, rounded_times, plotting_path, title_str = format(search_directory, times)

    ca = ClusterAnalysis(input_file)
    ca.getMeanTrajectory(SingleTraj=False)
    ca.getSteadyStateDistribution(SS_timePoints=rounded_times)

    plotClusterDistCopy(plotting_path, rounded_times, bins, title_str)