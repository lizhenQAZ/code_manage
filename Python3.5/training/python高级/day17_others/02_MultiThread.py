from threading import Thread


def deadloop():
    while True:
        pass


def main():
    t = Thread(target=deadloop)
    t.start()
    deadloop()


if __name__ == '__main__':
    main()
