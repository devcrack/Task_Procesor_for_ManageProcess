from shutil import copyfile
import os
import errno
import pathlib
from main.utils import date_time 


home = os.path.expanduser('~')
fles_dir = home + '/hipcc_data/'


def crt_dir(pth_dir):
    try:
        os.makedirs(pth_dir)                      
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


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
    dte_time = '-' + date_time.get_date_time_own_format()
    dest_file = './' + fle_name + dte_time + '.dat'
    
    copyfile(src_pth_fle, dest_file)
    
    return dest_file



def crt_dir_user(user_tag):
    """ 
    Create the user directory and all its nested directories.


    Args:
        user_tag(string): Is a tag for identified the directory of this user.

    Returns:    
        VOID
        
    """
    dict_dir = ['Hard_Sphere', 'Soft_Sphere', 'Yukawa', 'Dynamic']                              
    fll_pth = fles_dir + user_tag
    try:
        os.makedirs(fll_pth)
        for a_directory in dict_dir:
            if not os.path.exists(fll_pth + '/' + a_directory):
                os.makedirs(fll_pth + '/' + a_directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def list_usr_dir(usr):
    data = {}
    data[usr] = {}
    fll_pth =  fles_dir+ usr
    # Abriendo el directorio del usuario
    crrnt_dir = pathlib.Path(fll_pth)
    ptr_dat = data[usr]
    for directories_inside in crrnt_dir.iterdir():
        ptr_dat[directories_inside.name] = []
        # Abriendo cada archivo dentro de los
        # directorios que estan dentro del directorio de usuario.
        current_directory_nested = pathlib.Path(directories_inside)
        for files_in_directory in current_directory_nested.iterdir():
            ptr_dat[directories_inside.name].append(files_in_directory.name)
        ptr_dat[directories_inside.name].sort()
    return data
    
if __name__ == "__main__":
    crt_dir('aurelio@gmail.com')
    