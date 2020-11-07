import threading
import time


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Lanzando hilo: " + self.name)
        time.sleep(3)
        print("%s: %s" % (self.name, time.ctime(time.time())))


if __name__ == '__main__':
    threads = []

    for i in range(21):
        thread = myThread(i)
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

print("Saliendo del hilo principal")
