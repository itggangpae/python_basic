"""
#내장 함수 사용
print(max(10,30, 50))
print(max([100,300,200]))
print(max('Hello World'))
print(range(10))
print(range(3, 10))
print(range(3, 10, 2))
"""

"""
#Call By Value
def f(t):
    t = 10
    print("t:", t)

#a가 저장하고 있는 20이라는 데이터를 넘겼으므로 함수를 호출해도 a가 가리키고 있는 데이터는 변경되지 않음
a = 20
f(a)
print("a:", a)
"""

"""
#Call By Reference
def f(t):
    t[0] = 100

li = [1, 2, 3]

f(li)

print(li[0])
"""

"""
#매개변수의 기본값 사용
def f(n, step=1):
    return n+step;

a = 1
#순서대로 값을 대입해서 호출
result = f(a,10)
print(result)

b = 1
#첫번째 매개변수에만 값을 대입해서 호출
result = f(b)
print(result)

#매개변수 이름을 이용해서 매개변수를 대입해서 호출
result = f(step=2, n=10)
print(result)
"""


"""
#sum 함수의 도움말 확인 과 사용
help(sum)
print(sum([100, 200, 300], 2))

#두번째 매개변수를 생략해서 실행
print(sum([100, 200, 300]))
"""


"""
# unpacking
def unpacking(first, second):
    print('첫번째 데이터:', first)
    print('두번째 데이터:', second)

unpacking(*[100, 200])
print()
unpacking(*(100, 200))
print()
unpacking(*{100, 200})
print()
unpacking(*{"a": 100, "b": 200})
print()
"""

"""
# unpacking
def personal_info(name, age, gender):
    print('이름:', name)
    print('나이:', age)
    print('성별:', gender)

person = {"name": "아담", "age": 25, "gender": "남자"}
personal_info(**person)
"""

"""
# 가변 매개변수
def merge_string(*text_list):
    print('text_list:', type(text_list))
    result = ''
    for s in text_list:
        result = result + " " + s
    return result
print(merge_string('안녕하세요', '반갑습니다'))
print(merge_string('오늘은', '날씨가', '매우 춥습니다.'))
"""

"""
#가변 매개변수와 함께 사용하는 일반 매개변수
def print_args(argc, *argv):
    for i in range(argc):
        print(argv[i])

print_args(3, "argv1", "argv2", "argv3")

print_args(argc=3, "argv1", "argv2", "argv3")
"""

"""
def print_args(*argv, argc):
        for i in range(argc):
                print(argv[i])

print_args("argv1", "argv2", "argv3", argc=3)
print_args("argv1", "argv2", "argv3", 3)
"""

"""
#정의되지 않은 매개변수
def userURIBuilder(server, port, **param):
    print('param:', type(param))
    uri = "http://" + server + ":" + "/"
    for attr in param:
        uri = uri + attr + "=" + param[attr] + "&"
    return uri

print(userURIBuilder("test.com", "8080", id="cyberadam", pw="metaverse"))
print(userURIBuilder("test.com", "8080", id="cyberadam", pw="metaverse", nick="군계"))
"""


"""
#재귀 구현
def some_func(count):
    if count > 0:
        some_func(count-1)
    else:
        return
    print(count)

some_func(5)
"""

"""
#합계
def tot(n):
    if n == 1:
        return 1
    elif n > 1:
        return tot(n - 1) + n

print(tot(5))

print(tot(10))

print(tot(100))
"""

"""
#팩토리얼
def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return factorial(n - 1) * n

print(factorial(5))

print(factorial(10))

print(factorial(100))
"""


"""
#피보나치 수열
def fibonacci(n):
        if n == 1 or n == 2:
                return 1
        else:
                return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))
print(fibonacci(7))
print(fibonacci(10))
"""

"""
#하노이의 탑
def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks - 1, startPeg, 6 - startPeg - endPeg)
        print(startPeg, "번 기둥의", ndisks, "번 고리를 ", endPeg, "번 기둥에 옮깁니다.")
        hanoi(ndisks - 1, 6 - startPeg - endPeg, endPeg)

hanoi(ndisks=3)
"""


"""
#기존 방식
def isPalindrome(s):
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

print(isPalindrome('eros'))
print(isPalindrome('역삼역'))
print(isPalindrome('Ada'))
"""


"""
#함수에 애너테이션 추가
def clip(text:str, max_len: 'int > 0' = 80) -> None:
    print(text)
    print(max_len)

clip("Annotation", 100)
help(clip)
"""

"""
def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

print(isPalindrome('eros'))
print(isPalindrome('역삼역'))
print(isPalindrome('Ada'))
"""


"""
def plus(a, b):
    return a+b
plus.__doc__ = "2개의 숫자 데이터를 받아서 덧셈한 결과를 리턴해주는 함수"

def minus(a,b):
    '''
    2개의 숫자 데이터를 받아서 뺄셈한 결과를
    리턴해주는 함수
    '''
help(plus)
help(minus)
"""

"""
def f(a, b, c = 1):
    localx = 1
    localy = 2
    return 1

print(f.__name__)
print()
print(f.__defaults__)
print()
print(f.__code__)
print()
print(f.__globals__)
"""


"""
# 함수를 변수에 저장
def print_something(a):
    print(a)

p = print_something
p(123)
"""

"""
# 함수를 매개변수로 사용
def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def cal(func, a, b):
    return func(a, b)


print(cal(plus, 1, 2))
print(cal(minus, 1, 2))
"""

"""
#함수 리턴
def hello_korean():
    print('안녕하세요.')


def hello_english():
    print('Hello.')


def get_greeting(where):
    if where == 'K':
        return hello_korean
    else:
        return hello_english


hello = get_greeting('K')
hello()

hello = get_greeting('E')
hello()
"""


"""
#lambda
def g(func):
    return [func(x) for x in range(-10, 10)]

print(g(lambda x:x * x + 3 * x -10))

print(g(lambda x:x*x*x))
y = 10
print(g(lambda x: x + y))
"""

"""
#map
import datetime

def f(x):
    return x*x

li = [i for i in range(10000)]

print('반복문을 이용한 실행')
s1 = datetime.datetime.now()

for imsi in li:
    print(f(imsi), end=" ")
s2 = datetime.datetime.now()

print('\nmap을 이용한 실행')
s3 = datetime.datetime.now()
result = list(map(f,li))
s4 = datetime.datetime.now()

print("\n반복문 작업 시작 시간:", s1)
print("반복문 작업 종료 시간:", s2)
print("\nmap 작업 시작 시간:", s3)
print("map 작업 종료 시간:", s4)
"""

"""
#filter
def odd(x):
    return x % 2 == 1

li = [1,2,3,4,5]
print('filter를 이용한 홀수 골라내기')
result = list(filter(odd, li))
print(result)
"""

"""
li = [1,2,3,4,5]
print('lambda와 filter을 이용한 실행')
result = list(filter(lambda x : x%2==0, li))
print(result)
"""

"""
#reduce
from functools import reduce
result = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
print(result)
"""

"""
from functools import reduce

li = [70, 80, 98, 77, 95]
#전통적으로 최대값 구하기
def maximum(li):
    default = 0
    for e in li:
        if default < e:
            default = e
    return default
print(maximum(li))

#reduce 활용하여 최대값 구하기
print(reduce(lambda a,b: a if a > b else b ,li))
"""

"""
#zip
a = "Adam"
b = [1, 2, 3, 4]
c = ("하나", "둘", "셋", "넷")

print(list(zip(a, b, c)))
print(set(zip(a, b, c)))
print(dict(zip(a, b)))
"""

"""
L1 = ["A", "B", "C", "D"]
L2 = ["가", "나", "다", "라"]

for i, j in zip(L1, L2):
    print(i, j)
"""

"""
#중첩 함수
import math
#외부 함수
def stddev(*args):
    #내부 함수 - 평균
	def mean():
		return sum(args)/len(args)
    #내부 함수 - 분산
	def variance(m):
		total = 0
		for arg in args:
			total += (arg - m ) ** 2
		return total/(len(args)-1)
	v = variance(mean())
    #표준편차를 리턴하는 함수
	return math.sqrt(v)

print(stddev(2.3, 1.7, 1.4, 0.7, 1.9))

mean()
"""


"""
def scope_test():
    # 지역 변수 a 생성
    a = 1
    print('a : {0}'.format(a))


a = 0
scope_test()
print('a : {0}'.format(a))
"""

"""
#변수의 유효범위
def outer():
    a = 1

    def inner():
        nonlocal a
        print("함수의 외부 함수에 있는 a:{0}".format(a))
        a = 10

    inner()
    print("내부함수에서 변경한 경우의 a:{0}".format(a))


a = 0
outer()
print("a:{0}".format(a))
"""


"""
def outer():
    a = 1

    def inner():
        global a
        print("함수의 외부에 있는 a:{0}".format(a))
        a = 10

    inner()


a = 0
outer()
print("a:{0}".format(a))
"""


"""
#closure
def calc():
    a = 3
    b = 5

    def mul_add(x):
        return a * x + b  # 함수 바깥의 지역 변수 a, b를 사용하여 계산

    return mul_add  # mul_add 함수를 반환


c = calc()
print(c(1), c(2))
"""


"""
def calc():
    a = 3
    b = 5
    return lambda x: a * x + b  # 람다 표현식을 반환


c = calc()
print(c(1), c(2))
"""




