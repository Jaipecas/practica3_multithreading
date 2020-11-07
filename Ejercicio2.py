import threading
import time


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        threadSemaphore.acquire()
        time.sleep(3)
        print("Hilo " + self.name + " ha entrado en el tunel")
        threadSemaphore.release()
        time.sleep(1)
        print("Hilo " + self.name + " ha salido del tunel")


if __name__ == '__main__':
    threadSemaphore = threading.Semaphore(1)
    threads = []

    for i in range(21):
        thread = myThread(i)
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

print("Saliendo del hilo principal")
