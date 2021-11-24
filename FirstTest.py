def is_prime(num: int) -> bool:
    res = False
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    divisor = 3
    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 2
    return True


def get_prime(limit: int) -> (list, list):
    prime_list = list()
    non_prime_list = list()
    for num in range(1, limit + 1):
        if is_prime(num):
            prime_list.append(num)
        else:
            non_prime_list.append(num)
    return prime_list, non_prime_list


def list_to_string(num_list: list, cols) -> str:
    num_str = ""
    for index in range(len(num_list)):
        if (index + 1) % cols == 0:
            num_str += f'{num_list[index]: >3}' + "\n"
        else:
            num_str += f'{num_list[index]: >3}' + " "
    return num_str


def format_nums(limit: int, cols: int) -> (str, str):
    primes, non_prime = get_prime(limit)
    primes_string = list_to_string(primes, cols)
    nums_string = list_to_string(non_prime, cols)
    return primes_string, nums_string


def main():
    primes_string, nums_string = format_nums(100, 5)
    primes = f'Prime Numbers Are:\n{primes_string}'
    nums = f'None Prime Numbers Are:\n{nums_string}'
    print(primes)
    print(nums)


if __name__ == '__main__':
    main()
