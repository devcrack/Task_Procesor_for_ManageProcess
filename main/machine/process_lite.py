import os.path
import subprocess as sbp


home = os.path.expanduser('~')

prg_dir = '/core_programs/Bank_Mdls'

"""/home/<USER_DIRECTORY>/core_prg/Bank_Mdls  """
prg_path = home + prg_dir


def exe_hard_sphere(frac_vol):
    """ 
    Execute the program of hard sphere 


    Args:

        frac_vol (float):Volumen Fraction for do the calculates.

        Returns:
            void:nothing :p
    """
    exe = prg_path + '/01Sk_HSphere/Benny_Version/01Hard_Spheere' 
    
    pcs = sbp.Popen([exe, str(frac_vol)], stdout=sbp.PIPE, stderr=sbp.PIPE)
    
    out, error = pcs.communicate()

    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())
        return ':('
    if not pcs.poll():
        print("Program hard_sphere execute finish")


if __name__ == "__main__":
    exe_hard_sphere(0.5)
