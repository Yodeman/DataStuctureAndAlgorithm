import os

def disk_usage(path):
    """Return the number of bytes used by a file or folder and any descendants."""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for subdir in os.listdir(path):
            child_path = os.path.join(path, subdir)
            total += disk_usage(child_path)
    print('{0:>7}'.format(total), path)
    return total

disk_usage(r"C:\Users\USER\Desktop\my_pythonfiles_\DSandALGO\\")