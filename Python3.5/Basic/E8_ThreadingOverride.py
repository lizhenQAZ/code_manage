import threading
import time


class mythread(threading.Thread):
    def run(self):
        print("Sorry!")
        time.sleep(1)


def thread_main():
    for i in range(5):
        t = mythread()
        t.start()


if __name__ == '__main__':
    thread_main()