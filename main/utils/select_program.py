def hard_sphere_exe():
    print('Hard_Sphere Executed')

def soft_sphere_exe():
    print('Soft_Sphere Executed')

def yukawa_exe():
    print('Yukawa  Executed')


def program_execute(id_prog):
    if id_prog == 0:
        hard_sphere_exe()
    if id_prog == 1:
        soft_sphere_exe()
    if id_prog == 2:
        yukawa_exe()

