def generate_password(password_length, password_strength):
    password = ''
    '''
    YOUR CODE
    '''
    return password

def main():
    password_length = int(input('패스워드 길이를 입력해주세요. >> '))
    password_strength = int(input('패스워드 강도를 입력해주세요. >> '))
    password = generate_password(password_length, password_strength)
    print('생성된 패스워드는 {} 입니다.'.format(password))

if __name__ == '__main__':
    main()