import time
import threading
import concurrent.futures


def writing_file():
    with open('lesson3.py', 'r') as docs:
        file = docs.readlines()
        file.append(f'    print(\'hello world\')\n')
    with open('lesson3.py', 'w') as docs:
        docs.writelines(file)


def letters():
    for i in range(97, 123):
        print(chr(i))
        print(f'letters time before sleep: {time.perf_counter()}')
        time.sleep(1)
        print(f'letters time after sleep: {time.perf_counter()}\n')


def numbers():
    time.sleep(0.5)
    for i in range(1, 26):
        print(f'\x1b[8;36;40m {i} \x1b[0m')
        print(f'\x1b[8;36;40m numbers time before sleep: {time.perf_counter()} \x1b[0m')
        time.sleep(1)
        print(f'\x1b[8;36;40m numbers time after sleep: {time.perf_counter()} \x1b[0m\n')


def test_thread_without_lock():
    t1 = threading.Thread(target=letters)
    t2 = threading.Thread(target=numbers)
    t1.start()
    t2.start()


def write_sleeping(sec: int) -> str:
    print(f'Start sleeping \x1b[8;30;43m{sec}\x1b[0m seconds')
    time.sleep(sec)
    return f'Done sleeping... {sec}'


def test_sleep():
    start_time = time.perf_counter()
    sec_list = [5, 4, 3, 2, 1]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        thread_list = [executor.submit(write_sleeping, sec) for sec in sec_list]
        for threads in concurrent.futures.as_completed(thread_list):
            print(threads.result())
    end_time = time.perf_counter()
    print(f'Finished in {end_time - start_time} seconds')


def test_alternative_sleep():
    start_time = time.perf_counter()
    sec_list = [5, 4, 3, 2, 1]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(write_sleeping, sec_list)
    for result in results:
        print(result)
    end_time = time.perf_counter()
    print(f'Finished in {end_time - start_time} seconds')


def test_args(a: int, b: int):
    print(a)
    print(b)
    time.sleep(2)
    print("end of test arg")


def inf_func():
    while True:
        print("I am still doing something")
        time.sleep(0.5)


def test_daemon():
    t1 = threading.Thread(target=test_args, args=[1, 2])
    t2 = threading.Thread(target=inf_func, daemon=True)
    t1.start()
    t2.start()


def letters_lock():
    for i in range(1, 27):
        lock1.acquire()
        print(chr(i+96))
        lock2.release()


def numbers_lock():
    for i in range(1, 27):
        lock2.acquire()
        print(f'\x1b[8;36;40m {i} \x1b[0m')
        lock1.release()


def test_lock():
    t1 = threading.Thread(target=letters_lock)
    t2 = threading.Thread(target=numbers_lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    # writing_file()
    # test_thread_without_lock()
    # t1 = threading.Thread(target=test_args, args=[1, 2])
    # t2 = threading.Thread(target=test_alternative_sleep)
    # t2.start()
    # t1.start()
    # t1.join()
    # test_sleep()
    # test_alternative_sleep()
    # test_daemon()
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    lock2.acquire()

    test_lock()
    print("end of function")