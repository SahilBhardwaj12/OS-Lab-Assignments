import os

def task1_process_creation(n=3):
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            print(f"Child PID: {os.getpid()}, Parent PID: {os.getppid()}, Message: Hello from child {i+1}")
            os._exit(0)
    for i in range(n):
        os.wait()

if _name_ == "_main_":
    task1_process_creation(3)