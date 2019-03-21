import os
import subprocess as sbp


home = os.path.expanduser('~')

prg_dir = '/core_programs//NSCGLE_Theory'

prg_path = home + prg_dir

def exe_dyn_mdl(fv):
    """ 
    Execute the program of dynamic module 


    Args:

        frac_vol (float):Volumen Fraction for do the calculates.

        Returns:
            void:nothing :p
    """

    exe = os.chdir(prg_path + '/dynamic_mdl-0.1')     
    exe = os.getcwd()    
    pcs = sbp.Popen([exe + '/a.out', str(fv)], stdout=sbp.PIPE, stderr=sbp.PIPE)
    out, error = pcs.communicate()
    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())        
    if not pcs.poll():
        print("Dynamic Module execute finish")


if __name__ == "__main__":
    exe_dyn_mdl(0.5)