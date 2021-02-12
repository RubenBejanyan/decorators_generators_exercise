import string
import re
import itertools


def valid_password(password):
    my_pass = ''.join(password)
    if not re.search(r'[0-9]', my_pass):
        return False
    elif not re.search(r'[a-z]', my_pass):
        return False
    elif not re.search(r'[A-Z]', my_pass):
        return False
    elif not re.search(r"[\\!\"#$%'()*+,\-./:;=?@[\]^_`{|}~]", my_pass):
        return False
    return True


def password_generator(length=8):
    if length < 8:
        print(f'password length must be at least 8 characters\npassword with {length} characters is not reliable')
        return
    else:
        my_letters = string.ascii_letters
        my_numbers = string.digits
        my_spec_symbols = ''.join(x for x in string.punctuation if x not in '<>')
        my_pool = f'{my_numbers}{my_letters}{my_spec_symbols}'
        pass_gen = filter(valid_password, itertools.product(my_pool, repeat=length))
        while True:
            try:
                yield ''.join(next(pass_gen))
            except StopIteration:
                yield '!!!generator is empty!!!'
                return
