import threading
import time
from random import randint

disponible = True

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global disponible
        print("Hilo: " + self.name)
        time.sleep(0.5)
        condition.acquire()
        if disponible == False:
            condition.wait()
        disponible = False
        s = randint(1,10)
        print("Hilo " + self.name + " bebiendo vaso de agua " + "esperate " + str(s) + " segundos")
        time.sleep(s)
        print("Estaba de muerte, hilo: " + self.name)
        print("Hilo " + self.name + " esta saciado")
        notify()
        condition.release()

def notify():
    global disponible
    disponible = True
    condition.notifyAll()

if __name__ == '__main__':
    condition = threading.Condition()
    threads = []

    print("Hilos esperando para beber: ")
    for i in range(20):
        thread = myThread(i)
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

print("Saliendo del hilo principal")

