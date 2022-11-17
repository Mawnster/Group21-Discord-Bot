#Helper functions for issues related to linux and windows cross platform runtime
from sys import platform

#operating system helper function for paths
def os_path_helper(path_check):
    if(platform == "linux"):
        return path_check.replace("\\", "/")
    return path_check