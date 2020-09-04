# -*- coding: utf-8 -*-
__author__ = 'Aharon'
NUMBER_DIGIT_SIZE = 5


def sum_of_digits(number):
    """analyze number digit
    Args:
        number - the number to be analyzed(type string)
    Return the sum of all the digits
    like: input = 12345, return = 15
    """
    count = 0
    for i in number:
        count += int(i)
    return count


def check(input_number):
    """checking the input number
    Args:
        input_number - a string
        We will check some conditions on the input
    • if the input is a digit
    • if the input contain NUMBER_DIGIT_SIZE digits
    • if the input don't start with '0'
    • if the input is not empty
    Return value:
        True / False
    """
    if input_number.isdigit() \
            and len(str(input_number)) == NUMBER_DIGIT_SIZE \
            and str(input_number)[0] != str(0) \
            and input_number != '':
        return True
    return False


def from_number_to_digits(number):
    """
    Received a number
    Args:
        number - a digit number
    Return
        the number include ',' between 2 digits
    """
    result = ''
    for i in number:
        result += i + ','
    return result[:-1]


def asserts():
    assert check('12345') is True
    assert check('01234') is False
    assert check('1234a') is False
    assert check('1234') is False
    assert check(' ') is False
    assert from_number_to_digits('12345') == '1,2,3,4,5'
    assert sum_of_digits('12345') == 15


def main():
    asserts()
    while True:
        user_input = raw_input('Please insert a 5 digit number \n')
        if check(user_input):
            break

    print('{} {}'.format('You entered the number: ', user_input))
    print('{} {}'.format('The number include ",": ', from_number_to_digits(user_input)))
    print('{} {}'.format('The sum of digits is: ', sum_of_digits(user_input)))


if __name__ == '__main__':
    main()

    """
    example running:
        Please insert a 5 digit number
            12345
        You entered the number:  12345
        The number include ",":  1,2,3,4,5
        The sum of digits is:  15

Process finished with exit code 0
    """