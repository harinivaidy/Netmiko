from pprint import pprint
from netmiko import Netmiko
import threading
from Exercise1a import device
from my_functions import ssh_command
from datetime import datetime


def main():

    start_time = datetime.now()
    print(start_time)
    print("\n")

    for i in device:
        my_thread = threading.Thread(target = ssh_command, args = (i,))
        my_thread.start()

    main_thread = threading.currentThread()
    for j in threading.enumerate():
        if j != main_thread:
            print(j)
            j.join()

    print("\n")
    end_time = datetime.now()
    print(end_time)
    print("\n")
    print("Execution Time : {}".format(end_time-start_time))  

main()
