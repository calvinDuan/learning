import time
import concurrent.futures


def outer_function(msg):

    def inner_function():
        print(msg)
    return inner_function


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function


class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display():
    print('display function ran')


@decorator_function
def display_info(name: str, age: int):
    print(f'Hi, I am {name} and I am {age} yrs old. ')


def my_timer(orig_func):
    def wrapper_func(*args, **kwargs):
        start_time = time.time()
        result = orig_func(*args, **kwargs)
        end_time = time.time()
        length = end_time - start_time
        print(f'Function executed in {length} seconds')
        return result
    return wrapper_func


class MyTimer(object):
    def __init__(self, orig_func):
        self.orig_func = orig_func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.orig_func(*args, **kwargs)
        end_time = time.time()
        length = end_time - start_time
        print(f'class method executed in {length} seconds')
        return result


def write_sleeping(sec: int) -> str:
    print(f'Start sleeping \x1b[8;30;43m{sec}\x1b[0m seconds')
    time.sleep(sec)
    return f'Done sleeping... {sec}'


@my_timer
def test_sleep():
    sec_list = [5, 4, 3, 2, 1]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        thread_list = [executor.submit(write_sleeping, sec) for sec in sec_list]
        for threads in concurrent.futures.as_completed(thread_list):
            print(threads.result())


@MyTimer
def test_alternative_sleep():
    sec_list = [5, 4, 3, 2, 1]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(write_sleeping, sec_list)
    for result in results:
        print(result)


@my_timer
def my_add(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    # my_func = outer_function('hi')
    # my_func()
    # decorated_display = decorator_function(display)
    # decorated_display()
    # display()
    # display_info("calvin", 26)
    # print(my_add(1, 2))
    test_sleep()
    test_alternative_sleep()