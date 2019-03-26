from flask import Flask, make_response, request
from flask import jsonify

import main.task_s.task0 as task0
import main.configure
import main.machine.process_lite as p_lite
import main.machine.md_heavy as p_md_hvy
import main.utils.simple_mnge_files as dummy_sys_file

flask_app = Flask(__name__)

flask_app.config.from_object('main.configure.Development_Config')

celery_instance = task0.make_celery(flask_app) #Creating celery Instance


""" Get the petition with the json attached for process the request """
@flask_app.route('/start_work' , methods=['POST'])
def api():
    data = None
    """ HOW THE FUCK CAN REFACTOR THIS if make_response dont works in externall function """
    try:
        try:
            data = request.json
        except:
            raise ValueError

        if data is None:
            raise ValueError
        try:
            if data:
                print(data)
        except:
            raise KeyError
    except ValueError:
        print('Error 1: Error con los datos recibidos (bad request)')
        return make_response('bad request', 400)

    except KeyError:
        print('Error2: Error con lso datos del json')
        return make_response('data error', 409)

    #From we doing some insteresting stuffs
    call_task(data)

    return make_response('Chido', 200)



@flask_app.route('/create_user' , methods=['POST'])
def crte_user():
    data = None
    try:
        try:
            data = request.json
        except:
            raise ValueError

        if data is None:
            raise ValueError
        try:
            if data:
                print(data)
        except:
            raise KeyError
    except ValueError:
        print('Error 1: Error con los datos recibidos (bad request)')
        return make_response('bad request', 400)

    except KeyError:
        print('Error2: Error con los datos del json')
        return make_response('data error', 409)
    usr_tg = data['user_mail']
    dummy_sys_file.crt_dir(usr_tg)
    return make_response('User correctly created', 200)



def call_task(input):
    id_prog = input['id_process']
    fv = input['frac_vol']
    usr = input['user_mail']
    
    if id_prog == 0:
        exe_hrdsphere.delay(fv,usr)
    if id_prog == 1:
        it = input['ini_temp']
        exe_softsphere.delay(fv, it, usr)
    if id_prog == 2:
        it = input['ini_temp']
        exe_yuk_hs.delay(fv, it, usr)        
    if id_prog == 3:
        exe_dyn_mdl.delay(fv, usr)




"""Tasks implemented in Celery."""


@celery_instance.task
def exe_hrdsphere(frac_vol, user):    
    p_lite.exe_hard_sphere(frac_vol, user)



@celery_instance.task
def exe_softsphere(frac_vol, init, user):
    p_lite.exe_soft_sphere(frac_vol, init, user)



@celery_instance.task
def exe_yuk_hs(frac_vol, init, user):
    p_lite.exe_yukawa_hs(frac_vol, init, user)



@celery_instance.task
def exe_dyn_mdl(frac_vol, user):
    p_md_hvy.exe_dyn_mdl(frac_vol, user)    

