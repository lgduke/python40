import threading
import time

def thread_1():
    while True:
        print("activate thread1")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1)
t1.start()

while True:
    print("activate main")
    time.sleep(2.0)
    