from random import choice, shuffle
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

all_symbols = ascii_uppercase + ascii_lowercase + digits + punctuation

def make_password():
    chars = []
    chars.append(choice(ascii_uppercase))
    chars.append(choice(ascii_lowercase))
    chars.append(choice(digits))
    chars.append(choice(punctuation))
    for _ in range(4):
        chars.append(choice(all_symbols))
    shuffle(chars)
    password = ''.join(chars)
    return password

pw = make_password()
assert valid(pw)
print ('Your password is:', pw)
