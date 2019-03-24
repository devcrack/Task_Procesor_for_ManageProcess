from shutil import copyfile
import os
from main.utils import date_time

def cpy_file_to_usr_dir(src_pth_fle, dest_pth, fle_name):
    """ 
    Copy a file from the source path file to the user directory


    Args:
        src_pth_fle(string): source path to the file to copy.

        dest_pth(string): Destination path to the file to copy. 

        fle_name(string): Name of file to copy.
        

        Returns:
        dest_file(string): Complete path of the file copied to the user folder.
    """
    os.chdir(dest_pth)
    dte_time = '-' + date_time.get_date_own_format()
    dest_file = './' + fle_name + dte_time + '.dat'
    
    copyfile(src_pth_fle, dest_file)
    
    return dest_file
