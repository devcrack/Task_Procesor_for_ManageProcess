def exe_hard_sphere_by_user(frac_vol):
    print('Hard Sphere Executing\n\n\n')
    print ('Volumen Fraction = 'frac_vol)
    
"""     path = os.chdir('/home/yo/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version')                                                                                                    # Aqui cambiamos el directorio base en la ejecucion del programa.
    path = os.getcwd()
    print(path)
    hard_sphere_process = subprocess.Popen([path + '/01Hard_Spheere', fraction_volumen.strip()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)                                              # Ejecutamos el proceso para el calculo de esferas duras.
    out, error = hard_sphere_process.communicate()
    if out:
        print('OK', out)
    if error:
        print('Error', error.strip())
        return ':('
    if not hard_sphere_process.poll():
        print("Program hard_sphere execute finish")
 """