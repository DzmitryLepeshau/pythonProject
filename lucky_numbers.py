from sys import setrecursionlimit


def sum_of_square_digits(num):
    num_str = str(num)
    i = 0
    result_int = 0
    while i < len(num_str):
        sqr_of_one_digit = int(num_str[i]) * int(num_str[i])
        result_int = result_int + sqr_of_one_digit
        i += 1

    return result_int


# print(sum_of_square_digits(347))

setrecursionlimit(10)


def is_happy_number(number):
    i = 1
    result = 0
    while result != 1 and i <= 10:
        print('test')
        result = sum_of_square_digits(number)
        if result == 1:
            return True
        else:
            number = result
            i += 1
    return False


print(is_happy_number(19))
