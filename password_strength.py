import re
import os


def load_blacklist(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as text_file:
            return text_file.read().split('\n')
    return []


def check_password_length(password):
    password_strength = 0
    if len(password) > 4:
        password_strength += 1
    if len(password) > 6:
        password_strength += 1
    if len(password) > 10:
        password_strength += 1
    if len(password) > 12:
        password_strength += 1
    return password_strength


def check_char_types(password):
    password_strength = 0
    flag_uppercase = False
    flag_lowercase = False
    flag_digit = False
    if re.search('[0-9]', password):
        flag_digit = True
        password_strength += 1
    if re.search('[A-Z]', password):
        flag_uppercase = True
        password_strength += 1
    if re.search('[a-z]', password):
        flag_lowercase = True
        password_strength += 1
    if re.search('[$#@]', password):
        password_strength += 1
    if flag_digit and flag_lowercase and flag_uppercase:
        password_strength += 1
    return password_strength


def get_password_strength(password, filepath_to_blacklist='passwords.txt'):
    password_strength = 0
    password_blacklist = load_blacklist(filepath_to_blacklist)
    if password in password_blacklist:
        return 1
    if len(password) == 0:
        return None
    if len(set([letter for letter in password])) > 1:
        password_strength += 1
    password_strength += check_password_length(password)
    password_strength += check_char_types(password)
    return password_strength


if __name__ == '__main__':
    password_for_test = input('Input password: ')
    print(
        'Password strength is:',
        get_password_strength(password_for_test))
