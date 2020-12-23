from netmiko import Netmiko
import time 
from concurrent.futures import ProcessPoolExecutor, as_completed
from Exercise1a import device
from my_functions import ssh_command2
from datetime import datetime


def thread_as_completed():

    start_time = datetime.now()
    max_threads = 2

    pool = ProcessPoolExecutor(max_threads)

    my_future_list = []
    for i in device:
        my_future = pool.submit(ssh_command2, i)
        my_future_list.append(my_future)

    for my_future in as_completed(my_future_list):
        print("Result: " + my_future.result())
        end_time = datetime.now()
        print("Execution Time: {}".format(end_time - start_time))

thread_as_completed()

