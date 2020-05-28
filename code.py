import random
# import string

# 사용할 문자열을 정의 합니다. ( line 5 ~ line 12 )
symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# symbols = string.punctuation
numbers = '0123456789'
# numbers = string.digits
lowercase_characters = 'abcdefghijklmnopqrstuvwxyz'
# lowercase_characters = string.ascii_lowercase
uppercase_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# uppercase_characters = string.ascii_uppercase

def check_valid(password, password_strength):
    # password에 각각의 문자가 있는지 없는지 확인하기 위한 변수 ( line 16 ~ line 19 )
    in_symbols = False
    in_numbers = False
    in_lowercase_characters = False
    in_uppercase_characters = False
    # password의 내용을 확인하며 사용한 문자 종류를 확인 합니다. ( line 21 ~ line 29 )
    for each in password:
        if each in symbols:
            in_symbols = True
        if each in numbers:
            in_numbers = True
        if each in lowercase_characters:
            in_lowercase_characters = True
        if each in uppercase_characters:
            in_uppercase_characters = True
    # 각 패스워드의 조건에 따라 생성되어 있는지 확인 (line 31 ~ line 41)
    if password_strength == 1:
        return in_lowercase_characters and not in_uppercase_characters and not in_numbers and not in_symbols
    if password_strength == 2:
        return in_lowercase_characters and in_uppercase_characters and not in_numbers and not in_symbols
    if password_strength == 3:
        return in_lowercase_characters and in_uppercase_characters and in_numbers and not in_symbols
    if password_strength == 4:
        return in_lowercase_characters and in_uppercase_characters and in_numbers and in_symbols

def generate_password(password_length, password_strength):
    password = ''
    candidate = ''
    # password_strength에 따라 사용할 문자열을 저장 합니다. (line 47 ~ 54)
    if password_strength == 1:
        candidate = lowercase_characters
    elif password_strength == 2:
        candidate = lowercase_characters + uppercase_characters
    elif password_strength == 3:
        candidate = lowercase_characters + uppercase_characters + numbers
    elif password_strength == 4:
        candidate = lowercase_characters + uppercase_characters + numbers + symbols
    while True:
        # password_length 만큼 반복 하면서 패스워드를 생성 합니다. (line 57 ~ line 59)
        for i in range(password_length):
            idx = random.randint(0, len(candidate) - 1)
            password += candidate[idx]
        # 생성된 password가 password_strength에서 사용하는 모든 문자를 사용 했는지 확인을 합니다. (line 61 ~ 62)
        if check_valid(password, password_strength):
            break
        # 생성된 password가 조건에 만족하지 않으면, 초기화 하고 새로운 password를 생성 합니다.
        password = ''
    # 정상적으로 생성된 password를 리턴
    return password

def main():
    password_length = int(input('패스워드 길이를 입력해주세요. >> '))
    password_strength = int(input('패스워드 강도를 입력해주세요. >> '))
    password = generate_password(password_length, password_strength)
    print('생성된 패스워드는 {} 입니다.'.format(password))

if __name__ == '__main__':
    main()