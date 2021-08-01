from string import ascii_uppercase, ascii_lowercase, digits, punctuation

def valid(password):
    if len(password) != 8:
        return False
    
    has_uppercase = False    
    for c in ascii_uppercase:
        if c in password:
            has_uppercase = True
    
    has_lowercase = False
    for c in ascii_lowercase:
        if c in password:
            has_lowercase = True
    
    has_digit = False
    for c in digits:
        if c in password:
            has_digit = True
            
    has_punct = False
    for c in punctuation:
        if c in password:
            has_punct = True
    
    return has_uppercase and has_lowercase and has_digit and has_punct        


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
