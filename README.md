# Password Strength Calculator

With this script you can verify password strength on a scale from 1 to 10 depending on length, used character types and if it is blacklisted. Password blacklist is top 25 worst passwords from [2017 Splash rating](https://13639-presscdn-0-80-pagely.netdna-ssl.com/wp-content/uploads/2017/12/Top-100-Worst-Passwords-of-2017a.pdf).

# Quickstart

Start the script in the command line and type password to check password strength.
Or import get_password_strength function from password_strength.py file to use in your project.
Default file path to password blacklist is 'passwords.txt', or it can be stated in the function call.

### Example of import using interactive Python interpreter 

```python
>>> from password_strength import get_password_strength
>>> get_password_strength('qwerty', 'blacklist_example.txt')
1
>>> get_password_strength('asdfghqwerty')
5
>>> get_password_strength('C00lH@ckeRr11')
10
```

### Example of script launch on Linux, Python 3.5:

```bash

$ python password_strength.py
Input password: hello@world
Password strength is: 6

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
