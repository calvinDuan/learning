from typing import Any


class Dog(object):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.woof_time = 0

    def say_hi(self):
        print(f'Hi, my name is {self.name}, and I am {self.age} years old!')

    def bark(self, time):
        self.woof_time += time
        print(f'{self.name} says: {"woof!" * self.woof_time}')


class SelfMadeDict(object):
    def __init__(self, my_dict: dict):
        self._dict = my_dict

    def __repr__(self) -> str:
        string_dict = str()
        for key in self._dict:
            string_dict += f'{key}: {str(self._dict[key])}, '
        string_dict = string_dict[:-2]
        return f'{{{string_dict}}}'

    def sort_key_inc(self):
        key_list = list()
        sorted_dict = dict()
        for key in self._dict:
            key_list.append(key)
        key_list.sort()
        for keys in key_list:
            sorted_dict[keys] = self._dict[keys]
        self._dict = sorted_dict

    def sort_key_dec(self):
        key_list = list()
        sorted_dict = dict()
        for key in self._dict:
            key_list.append(key)
        key_list.sort()
        for keys in reversed(key_list):
            sorted_dict[keys] = self._dict[keys]
        self._dict = sorted_dict

    def sort_val_inc(self):
        val_list = list()
        sorted_dict = dict()
        for key in self._dict:
            val_list.append(self._dict[key])
        val_list.sort()
        for sort_val in val_list:
            for keys, val in self._dict.items():
                if val == sort_val:
                    sorted_dict[keys] = val
        self._dict = sorted_dict

    def sort_val_dec(self):
        val_list = list()
        sorted_dict = dict()
        for key in self._dict:
            val_list.append(self._dict[key])
        val_list.sort()
        for sort_val in reversed(val_list):
            for keys, val in self._dict.items():
                if val == sort_val:
                    sorted_dict[keys] = val
        self._dict = sorted_dict

    def get_key(self, val: Any):
        target_key = list(self._dict.keys())[list(self._dict.values()).index(val)]
        return target_key


if __name__ == '__main__':
    d = dict()
    d["One Hundred"] = 100
    d["Three Hundred"] = 300
    d["Two Hundred"] = 100
    test_dict = SelfMadeDict(d)
    print(f'The original dictionary is\n{test_dict}')
    test_dict.sort_key_inc()
    print(f'Testing sort dict by key with increasing order\n{test_dict}')
    test_dict.sort_key_dec()
    print(f'Testing sort dict by key with decreasing order\n{test_dict}')
    test_dict.sort_val_inc()
    print(f'Testing sort dict by value with increasing order\n{test_dict}')
    test_dict.sort_val_dec()
    print(f'Testing sort dict by value with decreasing order\n{test_dict}')
    test_key = test_dict.get_key(100)
    print(f'The key for value 200 is {test_key}')
