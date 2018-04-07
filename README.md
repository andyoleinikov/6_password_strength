# Password Strength Calculator

With this script you can verify password strength on a scale from 1 to 10 depending on length, used character types and if it is blacklisted. Password blacklist could be found for example [here](https://github.com/danielmiessler/SecLists/tree/master/Passwords) and passed as an argument.

# Quickstart

Start the script in the command line and type password to check password strength.
Or import get_password_strength function from password_strength.py file to use in your project.
Specify the path to a file when using this script from the command line.
```bash
$ python password_strength.py <path to file>
```

### Example of import using interactive Python interpreter 

```python
>>> from password_strength import get_password_strength
>>> get_password_strength('qwerty', ['qwerty', '1234'])
1
>>> get_password_strength('asdfghqwerty')
5
>>> get_password_strength('C00lH@ckeRr11')
10
```

### Examples of script launch on Linux, Python 3.5:

```bash

$ python password_strength.py
Input password:
Password strength is: 6

$ python password_strength.py darkweb2017-top100.txt
Passwords black list is loaded
Input password:
Password strength is: 1

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
