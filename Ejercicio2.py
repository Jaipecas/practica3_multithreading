import threading
import time


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Hilo " + self.name)
        time.sleep(3)
        threadSemaphore.acquire()
        print("Hilo " + self.name + " ha entrado en el tunel")
        time.sleep(1)
        print("Hilo " + self.name + " ha salido del tunel")
        threadSemaphore.release()


if __name__ == '__main__':
    threadSemaphore = threading.Semaphore()
    threads = []

    print("Hilos esperando fuera del tunel: ")

    for i in range(20):
        thread = myThread(i)
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

print("Saliendo del hilo principal")
