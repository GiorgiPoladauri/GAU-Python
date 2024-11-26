# This code demonstrates how to use Python’s threading module to run two tasks concurrently. The main program initiates two threads, t1 and t2, each responsible for executing a specific task. The threads run in parallel, and the code provides information about the process ID and thread names. The os module is used to access the process ID, and the ‘threading' module is used to manage threads and their execution.

import threading
import os

def task1():
	print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task 1: {}".format(os.getpid()))

def task2():
	print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task 2: {}".format(os.getpid()))

if __name__ == "__main__":

	print("ID of process running main program: {}".format(os.getpid()))

	print("Main thread name: {}".format(threading.current_thread().name))

	t1 = threading.Thread(target=task1, name='t1')
	t2 = threading.Thread(target=task2, name='t2')

	t1.start()
	t2.start()

	t1.join()
	t2.join()



 
# This code uses a thread pool created with concurrent.futures.ThreadPoolExecutor to run two worker tasks concurrently. The main thread waits for the worker threads to finish using pool.shutdown(wait=True). This allows for efficient parallel processing of tasks in a multi-threaded environment.

import concurrent.futures

def worker():
	print("Worker thread running")

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker)
pool.submit(worker)

pool.shutdown(wait=True)

print("Main thread continuing to run")
