def hard_sphere_exe():
    return 'Hard_Sphere Executed'

def soft_sphere_exe():
    return 'Soft_Sphere Executed'

def yukawa_exe():
    return 'Yukawa  Executed'


def program_execute(argument):
    chafa_switcher = {
        0: hard_sphere_exe,
        2: soft_sphere_exe,
        3: yukawa_exe,        
    }
    function = chafa_switcher.get(argument, lambda: "invalid Argument for be Processed")


