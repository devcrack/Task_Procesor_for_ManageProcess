import os
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

    exe = os.chdir(prg_path + '/01Sk_HSphere/Benny_Version')     
    exe = os.getcwd()
    pcs = sbp.Popen([exe + '/01Hard_Spheere', str(frac_vol)], stdout=sbp.PIPE, stderr=sbp.PIPE)
    out, error = pcs.communicate()

    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())        
    if not pcs.poll():
        print("Program hard_sphere execute finish")



def exe_soft_sphere(fv, it):
    """ 
    Execute the program of soft sphere 


    Args:

        fv (float):Volumen Fraction for do the calculates.
        it (float):Initial tempeture
        Returns:
            void:nothing :p
    """


    exe_p = os.chdir(prg_path + '/02SK_Soft_Sphere')
    exe_p = os.getcwd()
    pcs = sbp.Popen([exe_p + '/02SSphere', str(fv), str(it)], stdout=sbp.PIPE, stderr=sbp.PIPE)       
    out, error = pcs.communicate()
    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())        
    if not pcs.poll():
        print("Program soft_sphere execute finish")



if __name__ == "__main__":
    exe_soft_sphere(0.5, 0.1)
