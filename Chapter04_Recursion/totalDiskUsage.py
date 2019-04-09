import os

#A recursive python implementation of calculating immediate and cumulative
#disk space.
def diskUsage(path):
    """
    Input: a path
    Output: Total Disk Space being utilized by a folder/file
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            total += diskUsage(os.path.join(path,filename))
    
    print ( '{0:<7}'.format(total), path)
    return (total)

#Code Fragment 4.5: A recursive function for reporting disk usage 
#of a file system.