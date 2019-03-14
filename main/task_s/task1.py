""" This kind of task are so lite """
from celery import shared_task
import main.machine as machine

@shared_task
def exe_hrdsphere(frac_vol):
    machine.process_lite.exe_hard_sphere_by_user(frac_vol)
