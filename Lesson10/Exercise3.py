from netmiko import Netmiko
import time 
from concurrent.futures import ThreadPoolExecutor,wait,as_completed 
from Exercise1a import device
from my_functions import ssh_command2
from datetime import datetime


print("\n")
print("-" * 40)
print("Executing without Wait")
print("-" * 80)
print("\n")
def main():

    start_time = datetime.now()
    max_threads = 2

    for i in device:

        pool = ThreadPoolExecutor(max_threads)
        my_future = pool.submit(ssh_command2,i)

        print(my_future.done())
        time.sleep(5)
        print(my_future.done())

        print("Result: " + my_future.result())

    end_time = datetime.now()

    print("Execution time : {}".format(end_time-start_time)) 

main()

print("\n")
print("-" * 40)
print("Executing Wait")
print("-" * 80)
print("\n")

def wait_thread():

    start_time = datetime.now()
    max_threads = 1

    pool = ThreadPoolExecutor(max_threads)

    my_future_list = []
    for i in device:
        my_future = pool.submit(ssh_command2, i)
        my_future_list.append(my_future)

    wait(my_future_list)
    
    for my_future in my_future_list:
        print("Result" + my_future.result())
    
    end_time = datetime.now()
    print("Execution Time : {}".format(end_time - start_time))

wait_thread()  

print("\n")
print("-" * 40)
print("Print As Completed")
print("-"*40)
print("\n")

def thread_as_completed():

    start_time = datetime.now()
    max_threads = 2

    pool = ThreadPoolExecutor(max_threads)

    my_future_list = []
    for i in device:
        my_future = pool.submit(ssh_command2, i)
        my_future_list.append(my_future)

    for my_future in as_completed(my_future_list):
        print("Result: " + my_future.result())
        end_time = datetime.now()
        print("Execution Time: {}".format(end_time - start_time))

thread_as_completed()
        



















