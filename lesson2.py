import math
import stringcolor

print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'A': 1234, 'B': 5678, 'C': 9876}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

print(stringcolor.cs(f'Number\tSquare\tCube', "orchid"))
for x in range(1, 11):
    print(f'{x:2d}\t\t{x * x:3d}\t\t{x * x * x:4d}')


def test_format_options():
    for style in range(8):
        for font_color in range(30, 38):
            test_string = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(font_color), str(bg)])
                test_string += f'\x1b[{format}m Testing {format} \x1b[0m'
            print(test_string)
        print('\n')


def grocery():
    apple_name = 'Apples'
    bread_name = 'Bread'
    cheese_name = 'Cheese'

    num_apple = 3
    num_bread = 4
    num_cheese = 2

    prc_apple = 0.5
    prc_bread = 1.5
    prc_cheese = 2.25
    print(f'{"My Grocery List":^30s}\n'
          f'{"=" * 30:<30s}\n'
          f'{apple_name}\t{num_apple:10d}\t\t${prc_apple * num_apple:>5.2f}\n'
          f'{bread_name}\t{num_bread:10d}\t\t${prc_bread * num_bread:>5.2f}\n'
          f'{cheese_name}\t{num_cheese:10d}\t\t${prc_cheese * num_cheese:>5.2f}\n')


if __name__ == '__main__':
    test_format_options()
    grocery()
