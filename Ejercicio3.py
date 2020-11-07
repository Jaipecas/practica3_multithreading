import threading
import time


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        threadLock.acquire()
        time.sleep(1)
        print("Hilo " + self.name + " bebiendo vaso de agua")
        threadLock.release()
        print("Hilo " + self.name + " esta saciado")


if __name__ == '__main__':
    threadLock = threading.Lock()
    threads = []

    for i in range(20):
        thread = myThread(i)
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

print("Saliendo del hilo principal")