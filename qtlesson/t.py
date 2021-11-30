import time
from threading import Thread


def a(a,b):
    print(a+b)


if __name__ == '__main__':
    thread = Thread(target=a, (1,2))
