## 패스워드 생성기(Password Generator)

아래의 코드를 이용하여 사용자에게 패스워드의 길이(password_length)와 패스워드 강도(password_strength)를 입력 받아 다음과 같은 조건에 맞는 패스워드를 생성하는 generate_password 라는 함수를 완성 하세요.

### 조건
1. 패스 워드 길이(password_length)는 6이상 15이하의 자연수로 주어진다.

2. 패스 워드 강도(password_strength)는 1이상 4이하의 자연수 이며, 다음과 같은 문자로 패스워드가 구성 됨을 의미 한다.
   * 1 : 알파벳 소문자(abcdefghijklmnopqrstuvwxyz)로만 패스워드가 구성
   * 2 : 알파벳 소문자와 대문자(ABCDEFGHIJKLMNOPQRSTUVWXYZ)로만 패스워드가 구성
   * 3 : 알파벳 소문자, 대문자 그리고 숫자(0123456789)로만 패스워드가 구성
   * 4 : 알파벳 소문자, 대문자, 숫자 그리고 특수문자(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)

3. 패스워드 강도에 맞는 패스워드를 생성할 때, 패스워드 강도로 요구하는 문자들을 하나 이상 사용해야 한다. 예를 들어 패스워드 강도가 3인 경우 패스워드에는 반드시 알파벳 소문자, 대문자, 숫자가 각각 한 번 이상은 등장해야 한다.

### 코드
```python
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
```

### 입력 예시 #1
```
패스워드 길이를 입력해주세요. >> 6
패스워드 강도를 입력해주세요. >> 1
```

### 출력 예시 #1
```
생성된 패스워드는 aeuizo 입니다.
```

### 입력 예시 #2
```
패스워드 길이를 입력해주세요. >> 8
패스워드 강도를 입력해주세요. >> 2
```

### 출력 예시 #2
```
생성된 패스워드는 TMAngKem 입니다.
```

### 입력 예시 #3
```
패스워드 길이를 입력해주세요. >> 10
패스워드 강도를 입력해주세요. >> 3
```

### 출력 예시 #3
```
생성된 패스워드는 4cyE7C9C16 입니다.
```

### 입력 예시 #4
```
패스워드 길이를 입력해주세요. >> 15
패스워드 강도를 입력해주세요. >> 4
```

### 출력 예시 #4
```
생성된 패스워드는 |Z|Xd.t5V3Z+s<+ 입니다.
```