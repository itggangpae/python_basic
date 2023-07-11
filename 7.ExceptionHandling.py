"""
#예외 발생
def ten_div(x):
    return 10 / x

print(ten_div(2)) #정상 수행
print(ten_div(0)) #예외 발생
"""

"""
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except:    # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.')
"""


"""
y = [10, 20, 30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
except IndexError:           # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
    print('잘못된 인덱스입니다.')
"""

"""
y = [10, 20, 30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError as e:                    # as 뒤에 변수를 지정하면 에러를 받아옴
    print('숫자를 0으로 나눌 수 없습니다.', e)    # e에 저장된 에러 메시지 출력
except IndexError as e:
    print('잘못된 인덱스입니다.', e)
"""


"""
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
"""


"""
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
finally:                     # 예외 발생 여부와 상관없이 항상 실행됨
    print('코드 실행이 끝났습니다.')
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
finally:                     # 예외 발생 여부와 상관없이 항상 실행됨
    print('코드 실행이 끝났습니다.')
"""


"""
try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                                 # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
    print(x)
except Exception as e:                             # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.', e)
"""


"""
def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:                                 # x가 3의 배수가 아니면
            raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
        print(x)
    except Exception as e:                             # 함수 안에서 예외를 처리함
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise    # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김

try:
    three_multiple()
except Exception as e:                                 # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('스크립트 파일에서 예외가 발생했습니다.', e)
"""


"""
x = int(input('3의 배수를 입력하세요: '))
assert x % 3 == 0, '3의 배수가 아닙니다.'    # 3의 배수가 아니면 예외 발생, 3의 배수이면 그냥 넘어감
print(x)
"""


"""
class NotThreeMultipleError(Exception):    # Exception을 상속받아서 새로운 예외를 만듦
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')

def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:                     # x가 3의 배수가 아니면
            raise NotThreeMultipleError    # NotThreeMultipleError 예외를 발생시킴
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)

three_multiple()
"""


