from multiprocessing import Process


def deadloop():
    while True:
        pass


def main():
    p = Process(target=deadloop)
    p.start()
    deadloop()


if __name__ == '__main__':
    main()
