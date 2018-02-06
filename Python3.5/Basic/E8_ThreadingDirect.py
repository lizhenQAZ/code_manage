import threading
import time


def saysorry():
    print("Sorry!")
    time.sleep(1)


def thread_main():
    for i in range(5):
        t = threading.Thread(target=saysorry())
        t.start()


if __name__ == '__main__':
    thread_main()