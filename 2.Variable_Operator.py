'''
#들여쓰기
num = 20
#블록마다 들여쓰기를 다르게 설정해도 되지만 권장하지 않음
if num >= 10:
    print("10보다 크다")
else:
  print("10보다 작다")
'''

"""
#파이썬 주석
# 이 줄은 라인 코멘트입니다
print("Hello World!")

print("Hello World!")   # 이것도 라인 코멘트입니다

'''
이것은 블럭 주석처럼 사용할 수 있음
큰따옴표 나 작은 따옴표 3개를 연속으로 적으면 주석이 아니고 여러 줄 문자열
'''
"""


"""
#가능한 작업 확인과 함수의 도움말 확인

#정수를 가지고 할 수 있는 작업 확인
print(dir(100))

#print에 도움말
help(print)
"""

"""
#파이선 예약어 확인
import keyword
print(keyword.kwlist)
"""

"""
#현재 사용 중인 파이썬에서 모듈을 찾는 순서 확인
import sys
print(sys.path)
"""

"""
#변수를 생성해서 값을 대입
counter = 100          # 정수 할당
miles   = 1000.0       # 부동 소수점
name    = "홍길동"     # 문자열

#변수의 값을 콘솔에 출력
print(counter)
print(miles)
print(name)

#반복문을 이용해서 counter 변수에 새로운 값을 대입
for counter in [1,2,3]:
    print(counter)

#기존에 저장된 값 대신에 마지막에 저장한 값을 출력
print(counter)
"""

"""
#예약어에 데이터를 할당
and = 1
print(and)
"""

"""
#기존 존재하는 이름에 데이터를 할당
print(abs(-3))
abs = 1
print(abs(-3))
"""

"""
#산술 연산자
a = 11
b = 2

add = a + b
sub = a - b
mul = a * b
div = a / b
mok = a //b
mod = a % b

print("a+b=",add)
print("a-b=",sub)
print("a*b=",mul)
print("a/b=",div)
print("a//b=",mok)
print("a%b=",mod)
"""

"""
#소녀시대 레드벨벳 블랙핑크 ITZY를 번갈아 보여주기
import time
i = 0
while i < 12:
    result = i % 4
    i = i + 1
    time.sleep(1)

    if result == 0:
        print("소녀시대")
    if result == 1:
        print("레드벨벳")
    if result == 2:
        print("블랙핑크")
    if result == 3:
        print("ITZY")
"""

"""
#크기 확인
pan = 10 > 3;
print("pan:",pan);

#동일성 확인
pan = 10 == 3;
print("pan:",pan);

date = '2019-01-01'
print(date == '2019-01-01')
print(date == '2018-12-31')

#문자의 크기 비교는 첫글자부터 순서대로 비교
#알파벳은 대문자와 소문자를 구분하며 소문자가 대문자보다 큼
print("레드벨벳" > "블랙핑크")
print("BlackPink" > "blackpink")

#연산 순서
print(10 == 10 + 1)
"""

"""
a = 20 #00000000 00000000 00000000 00010100
b = 12 #00000000 00000000 00000000 00001100

print("a&b=",a&b)
print("a|b=",a|b)
print("a^b=",a^b)
print("a<<2=", a<<2)
print("a>>2=", a>>2)

print()
b = -13 #11111111 11111111 11111111 11110011
print("a&b=",a&b)
print("a|b=",a|b)
print("a^b=",a^b)
print("b<<2=", b<<2)
print("b>>2=", b>>2)
"""

"""
#윤년 판별

#윤년은 2개의 조건 중 하나를 만족하면 됩니다.
#1. 4의 배수이고 100의 배수는 아닌 경우
#2. 400의 배수인 경우

year = 2019
leafcheck = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(year, "의 윤년 여부:", leafcheck)

year = 2020
leafcheck = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(year, "의 윤년 여부:", leafcheck)
"""

"""
#12의 배수 구하기
#1-100까지에서 3의 배수이고 4의 배수 개수 구하기
cnt = 0
loop = 0
for i in range(1,101):
    loop = loop + 1
    if i % 3 == 0:
        loop = loop + 1
        if i % 4 == 0:
            cnt = cnt + 1
print("12의 배수 개수: ", cnt, "개")
print("루프 횟수: ", loop, "번")
print("=================")

cnt = 0
loop = 0
for i in range(1,101):
    loop = loop + 1
    if i % 4 == 0:
        loop = loop + 1
        if i % 3 == 0:
            cnt = cnt + 1
print("12의 배수 개수: ", cnt, "개")
print("루프 횟수: ", loop, "번")
"""

"""
#논리 함수
L1 = [True, True, False]
print(L1)
print(all(L1))
print(any(L1))

L2 = [1, 1, 0]
print(L2)
print(all(L2))
print(any(L2))

L3 = [3 > 0, 3 > 2, 2 == 2]
print(L3)
print(all(L3))
print(any(L3))
"""

"""
#연산자 축약
a = 10
a += 5 # a = 10 + 5
print("a:", a)
a *= 2 # a = 15 * 2
print("a:", a)
"""

"""
#자료형 확인 및 저장된 데이터의 참조 코드 확인
a = 20
b = 20
print("a가 가리키고 있는 곳의 id:", id(a))
print("a의 자료형:", type(a))
print("b가 가리키고 있는 곳의 id:", id(b))

a = 10 + 20
print("a가 가리키고 있는 곳의 id:", id(a))
b = 30
print("b가 가리키고 있는 곳의 id:", id(b))

a = 30 + 40
print("a가 가리키고 있는 곳의 id:", id(a))
"""

"""
#데이터 자료형 변환
print(int(10.7))
print(int("10"))
#print(int("10.7"))
print(int(True))
print("==========")

print(float("10.7"))
print(float(True))
print("==========")

print(bool(20))
print(bool(0.0))
print(bool(True))
print("==========")

print(str(10.7))
"""


"""
#bool 자료형
a = True
b = False

#True 는 상황에 따라 1 False 는 0으로 해석
print(a == 1)     # True가 출력됨
print(b != 0)     # False가 출력됨
print(a + b)      # 1
print(not a)      #False
"""

"""
#콘솔 출력
print (1,2)
print (3,4)

print(1,2, end= ' ')
print(3,4)

print(1,2,3,4, sep='\t')
"""

"""
#서식을 이용한 출력
txt1 = '자바'
txt2='파이썬'
num1= 5
num2=10
num3=3.141569
print('나는 %s보다 %s에 더 익숙합니다.' %(txt1, txt2))
print('%d + %d = %d' %(num1, num2, num1+num2))
print('작년 세계 경제 성장률은 전년에 비해 %d%% 포인트 증가했다.' %num1)
print('파이는 소수 세째 자리에서 반올림 하면 %.2f 입니다.' %num3)
"""

"""
print("My name is {}".format('Adam'))
print('{}은 {}를 좋아합니다.'.format('Adam', '신촌 라이브 카페'))
print('{1}은 {0}을 보고 만들었습니다.'.format('원빈', 'Adam'))
"""


"""
name = 'Adam'
birth = '1997년 12월 12일'
print(f"{name}의 생년월일은 {birth}입니다.")

one = 1
two = 2
print(f"{one}집은 제네시스로 어느 정도 성공했고 {two}집은 엑소더스로 폭망했습니다.")
"""

"""
name = input('이름:')
print(name)
age = int(input('나이:'))
print(age)
print(type(age))
"""


"""
#공백으로 분할해서 입력
data = input("입력 (x y z) : ")

L = data.split()
x, y, z, = L[0], L[1], L[2]

print(x)
print(y)
print(z)

#,로 구분해서 입력
x, y, z = input("데이터 입력 (a,b,c) : ").split(',')

print(x)
print(y)
print(z)
"""

"""
url = 'http://search.hani.co.kr/Search?command=query&keyword='
keyword = input('검색어를 입력하세요:')
url = url + keyword
url = url + '&media=news&submedia=&sort=d&period=all&datefrom=2000.01.01&dateto=2019.06.22&pageseq=0'
print(url)
"""