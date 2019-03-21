from flask import Flask, make_response, request
from flask import jsonify

from main.utils import select_program
import main.task_s.task0 as task0
import main.configure
import main.machine.process_lite as p_lite


flask_app = Flask(__name__)

flask_app.config.from_object('main.configure.Development_Config')

celery_instance = task0.make_celery(flask_app) #Creating celery Instance


""" Get the petition with the json attached for process the request """
@flask_app.route('/lite_task' , methods=['POST'])
def api():
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
        print('Error2: Error con lso datos del json')
        return make_response('data error', 409)

    #From we doing some insteresting stuffs
    call_task(data)

    return make_response('Chido', 200)




def call_task(input):
    id_prog = input['id_process']
    f_v = input['frac_vol']
    
    if id_prog == 0:
        exe_hrdsphere.delay(f_v)
    if id_prog == 1:
        it = input['ini_temp']
        print('Executing Soft Sphere\n')
        print('Initial temp', it)
        print('volumen factor', f_v)
    if id_prog == 2:
        print('Executing Yukawa')    



@celery_instance.task
def exe_hrdsphere(frac_vol):    
    p_lite.exe_hard_sphere(frac_vol)


@celery_instance.task
def exe_softsphere(frac_vol, init):
    p_lite.exe_soft_sphere(frac_vol, init)