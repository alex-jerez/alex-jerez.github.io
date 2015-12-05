import threading
import time

var = 0 
lock = threading.Lock()

def countTo(num):
    global var 
    lock.acquire()
    for number in range(num):
        var += 1
        print var
        time.sleep(1)
    lock.release()
def Main():
    thread1 = threading.Thread(target=countTo, args=(5,))
    thread2 = threading.Thread(target=countTo, args=(8,))
    thread1.start()
    thread2.start()

    print "Main finished"

if __name__ == "__main__":
    Main()
