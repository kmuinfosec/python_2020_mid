import random

symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
numbers = '0123456789'
lowercase_characters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def check_valid(password, password_strength):
    in_symbols = False
    in_numbers = False
    in_lowercase_characters = False
    in_uppercase_characters = False
    for each in password:
        if each in symbols:
            in_symbols = True
        if each in numbers:
            in_numbers = True
        if each in lowercase_characters:
            in_lowercase_characters = True
        if each in uppercase_characters:
            in_uppercase_characters = True
    if password_strength == 1:
        return in_lowercase_characters
    if password_strength == 2:
        return in_lowercase_characters and in_uppercase_characters
    if password_strength == 3:
        return in_lowercase_characters and in_uppercase_characters and in_numbers
    if password_strength == 4:
        return in_lowercase_characters and in_uppercase_characters and in_numbers and in_symbols

def generate_password(password_length, password_strength):
    password = ''
    candidate = ''
    if password_strength == 1:
        candidate = lowercase_characters
    elif password_strength == 2:
        candidate = lowercase_characters + uppercase_characters
    elif password_strength == 3:
        candidate = lowercase_characters + uppercase_characters + numbers
    elif password_strength == 4:
        candidate = lowercase_characters + uppercase_characters + numbers + symbols
    while True:
        for i in range(password_length):
            idx = random.randint(0, len(candidate) - 1)
            password += candidate[idx]
        if check_valid(password, password_strength):
            break
        password = ''
    return password

def main():
    password_length = int(input('패스워드 길이를 입력해주세요. >> '))
    password_strength = int(input('패스워드 강도를 입력해주세요. >> '))
    password = generate_password(password_length, password_strength)
    print('생성된 패스워드는 {} 입니다.'.format(password))

if __name__ == '__main__':
    main()