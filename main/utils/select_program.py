from main.task_s.task1 import *

def program_execute(id_prog, frac_v):
    if id_prog == 0:
        exe_hrdsphere.delay(frac_v)
    if id_prog == 1:
        print('Executing Soft Sphere')
    if id_prog == 2:
        print('Executing Yukawa')

