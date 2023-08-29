import threading

def sum(name, value):
    for i in range(0,value):
        print(f"{name} : {i}")
        

t1 = threading.Thread(target=sum, args=('No 1 thread', 10))
t2 = threading.Thread(target=sum, args=('No 2 thread', 10))

t1.start()
t2.start()

print("Main Thread")

#while True:
#    print("activate main")
#    time.sleep(2.0)
    