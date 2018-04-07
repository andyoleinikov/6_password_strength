import re
import os
import string
import getpass
import sys


def load_blacklist(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as text_file:
            return text_file.read().split('\n')
    return []


def check_password_length(password):
    password_strength = 0
    small_length = 4
    normal_length = 6
    good_length = 10
    great_length = 12
    if len(password) > small_length:
        password_strength += 1
    if len(password) > normal_length:
        password_strength += 1
    if len(password) > good_length:
        password_strength += 1
    if len(password) > great_length:
        password_strength += 1
    return password_strength


def check_char_types(password):
    password_strength = 0
    flag_uppercase = False
    flag_lowercase = False
    flag_digit = False
    symbols_pattern = '[{}]'.format(string.punctuation)
    if re.search('[0-9]', password):
        flag_digit = True
        password_strength += 1
    if re.search('[A-Z]', password):
        flag_uppercase = True
        password_strength += 1
    if re.search('[a-z]', password):
        flag_lowercase = True
        password_strength += 1
    if re.search(symbols_pattern, password):
        password_strength += 1
    if all([flag_digit, flag_lowercase, flag_uppercase]):
        password_strength += 1
    return password_strength


def get_password_strength(password, password_blacklist=[]):
    password_strength = 0
    if password in password_blacklist:
        return 1
    if not password:
        return None
    if len(set([letter for letter in password])) > 1:
        password_strength += 1
    password_strength += check_password_length(password)
    password_strength += check_char_types(password)
    return password_strength


if __name__ == '__main__':
    filepath = ''
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    blacklist = load_blacklist(filepath)

    if blacklist:
        print('Passwords black list is loaded')

    password_for_test = str(
        getpass.getpass(prompt='Input password: ', stream=None))

    print(
        'Password strength is:',
        get_password_strength(password_for_test, blacklist))
