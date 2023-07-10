"""
#부울 자료형 확인
print(bool([]))
print(bool(3))
print(bool(3+4))
"""

"""
#정수 자료형 저장 방법
a = 10
print("a =", a)
#정수 형변환
a = int('10')
print("a =", a)
#5진수로 변환
a = int('20', 5)
print("a =", a)
#실수를 정수로 변한 - 소수가 버려짐
a = int(10.8)
print("a =", a)
"""


"""
#실수형
import sys
print("실수 정보:", sys.float_info)
a = 1.2
b = 3e3
c=-0.2e-4
print(a, b, c)
a = int(1.7)
print("a:", a)
a = round(1.7)
print("a:", a)
"""

"""
#실수의 표현 범위 제한때문에 인한 문제
print('0.2 == (1.0-0.8):', (0.2 == (1.0-0.8)))
sum = 0
for i in range(0,1000):
    sum += 1
print("정수 1을 1000번 더한 결과:" , sum)

sum = 0.0
for i in range(0,1000):
    sum += 0.1
print("실수 0.1을 1000번 더한 결과:" , sum)
"""

"""
#복소수
print(1.2 + 1.3j)
print(complex(1.2, 1.3))
"""


"""
import math

print(math.pow(3, 2))
print(math.sqrt(3))
"""


"""
#decimal.Decimal
from decimal import Decimal
#부정확한 실수 연산
print((1234.567 + 45.67844) + 0.0004)
print(1234.567 + (45.67844 + 0.0004))
#정확한 실수 연산
print((Decimal('1234.567') + Decimal('45.67844')) + Decimal('0.0004'))
"""


"""
#random 모듈
import random

i = random.randint(1, 100)  # 1부터 100 사이의 임의의 정수
print(i)
f = random.random()   # 0부터 1 사이의 임의의 float
print(f)
f = random.uniform(1.0, 36.5)   # 1부터 36.5 사이의 임의의 float
print(f)
i = random.randrange(1, 101, 2) # 1부터 100 사이의 임의의 짝수
print(i)
i = random.randrange(10)  # 0부터 9 사이의 임의의 정수
print(i)
"""

"""
#Sequential Type의 공통 연산
msg = "Korea"
print(msg[0]) #0번째 글자
print(msg[-2]) #뒤에서 2번째 글자
print(msg[1:3]) #1번째부터 3번째 글자 앞까지
print(msg[0:5:2]) #0부터 5번째 글자 앞까지 2개씩 건너뛰면서
print(msg[:-1])#-1 번째까지 가져오기
print(msg[::-1])#반대로 출력

msg = "Hello" + "World"
print(msg)

msg = msg * 4
print(msg)
"""

"""
#문자열은 내부 데이터 수정이 안됨
msg = "hello"
msg[0] = 'f' #이런 문장은 에러
"""

"""
#문자열 추가 및 삭제
msg = "Hardware"
print("현재 msg의 id:", id(msg))

msg = msg + " and Shell"
print("현재 msg의 id:", id(msg))

msg = msg[:8] + ' Kernel' + msg[8:]
print(msg)
print("현재 msg의 id:", id(msg))

msg = msg[:15] + msg[20:]
print(msg)
"""

"""
#ESCAPE code(제어 문자)
print('''인생은 생각할 수록 아름답고
역사는 앞으로 발전한다''')
print('\t탭\n다음 줄')
print(r'\t탭\n다음 줄')
"""

"""
#문자열 포맷
data = [1,3,4]
print('최대값:{0:5d}\t최소값:{1:5d}'.format(max(data), min(data)))
"""

"""
#문자열의 서식 지정
# 문자열 맨 앞에 f를 붙이고, 출력할 변수, 값을 중괄호 안에 넣습니다.
s = 'korean_vodka'
n = 5

result1 = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'
print(result1)

s1 = 'left'
result1 = f'|{s1:<10}|'
print(result1)
# f-string 가운데 정렬
s2 = 'mid'
result2 = f'|{s2:^10}|'
print(result2)
# f-string 오른쪽 정렬
s3 = 'right'
result3 = f'|{s3:>10}|'
print(result3)

result = f'my  amount of alcohol {{{n}}}, {{n}}'
print(result)
"""

"""
# join() 메서드는 문자열을 결합하는데 사용되는 Separator를 join 메서드 앞에 사용
s = ','.join(['가나', '다라', '마바'])
print(s)
# 출력: 가나,다라,마바

s = ''.join(['가나', '다라', '마바'])
print(s)
# 출력 : 가나다라마바

# partition() 메서드는 문자열을 partition() 메서드의 첫번째 파라미터로 분리하여
# 그 앞부분(prefix), partition 분리자(separator), 뒷부분 (suffix) 등 3개의 값을 Tuple로 리턴
departure, _, arrival = "Seattle-Seoul".partition('-')
print(departure)
msg = "c:\\data\\data.txt"
#test의 존재여부
print(msg.find('test'))
#위의 문자열에서 파일의 확장자만 추출하기
ar = msg.split(".")
print("확장자:", ar[len(ar)-1])
print(msg.replace('data', 'python'))
"""

"""
msg = 'ggangpae1@gmail.com'
#위의 문자열에서 영문을 제외한 모든 글자 삭제
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
result = ''
for ch in msg:
    if ch in alphabet:
        result = result + ch
print(result)
"""

"""
msg = 'ggangpae1@gmail.com'
result = ''
for ch in msg:
    if ch.isalpha():
        result = result + ch
print(result)
"""

"""
instr = 'abcdef'
outstr = '123456'
trans = str.maketrans(instr, outstr)
msg = 'hello world'
print(msg.translate(trans))
"""

"""
#문자열 인코딩
import sys
print("현재 시스템의 입력 인코딩:", sys.stdin.encoding)
print("현재 시스템의 출력 인코딩:", sys.stdout.encoding)
b = '파이썬'.encode('utf-8')
print(b)
msg = b.decode('utf-8')
print(msg)
b = '파이썬'.encode('ms949')
print(b)
msg = b.decode('ms949')
print(msg)
"""

"""
#한글 처리
c = '한'
code = ord(c) - 0xAC00
chosung = code // (21*28)
jungsung = (code - chosung*21*28)//28
jongsung = (code - chosung*21*28 - jungsung*28)
print('초성:', chosung, "번째 글자")
print('중성:', jungsung, "번째 글자")
print('종성:', jongsung, "번째 글자")

print("========================")
c = '대'
code = ord(c) - 0xAC00
chosung = code // (21*28)
jungsung = (code - chosung*21*28)//28
jongsung = (code - chosung*21*28 - jungsung*28)
print('초성:', chosung, "번째 글자")
print('중성:', jungsung, "번째 글자")
print('종성:', jongsung, "번째 글자")
"""


"""
#re 객체
import re
match = re.match('[0-9]', '1234')
print(match.group())

match = re.match('[0-9]', 'abc')
print(match)

match = re.match('[0-9]+', '1234')
print(match.group())
"""


"""
import re
match = re.match('[0-9]+', ' 1234')
print(match)
match = re.match('\s[0-9]+', ' 1234')
print(match)
match = re.search('[0-9]+', ' 1234')
print(match)
"""


"""
#re 클래스의 메서드
import re
p = re.compile(r'[_a-zA-Z]\w*')
m = p.search('123 abc 123 def')
print(m.group())
m = p.findall('123 abc 123 def')
print(m)
p = re.compile('the')
print(p.findall('The cat was hungry, They were scared because of the cat'))
p = re.compile('the', re.I)
print(p.findall('The cat was hungry, They were scared because of the cat'))
"""


"""
import re
#주민등록번호 정규식 인스턴스 만들기
p = re.compile('(\d{6})-?(\d{7})')
num = '100000-2000000'
if p.search(num) != None:
    print("올바른 주민번호 형식입니다.")
else:
    print("올바른 주민번호 형식이 아닙니다.")
num = '10000-2000000'
if p.search(num) != None:
    print("올바른 주민번호 형식입니다.")
else:
    print("올바른 주민번호 형식이 아닙니다.")
"""


"""
import re
#문자열 분리
result = re.split('[:. ]+', 'apple banana:orange tomato')
print(result)
#문자열 찾기
result = re.findall("app\w*", 'application orange apple banana')
print(result)
#문자열 치환
result = re.sub("-","", "901225-1234567")
print(result)
result= re.sub("[:,|]", ",", "apple:orange banana|tomato")
print(result)
"""



"""
import re

p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
emails = ['python@mail.example.com', 'python+kr@example.com',  # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',  # 올바른 형식
          'python.dojang@e-xample.com',  # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']  # 잘못된형식

for email in emails:
    print(p.match(email) != None, end=' ')
"""

"""
txt = b'Hello'
for b in txt:
    print(b, end="\t")
print()
s1 = 'A\u0041'
print(s1)
b = '파이썬'.encode('utf-8')
print(b)
msg = b.decode('utf-8')
print(msg)
"""


"""
#list
li = [1,2,3]
print ("자료형:", type(li))
print ("길이:" , len(li))
print ("두번째 데이터:", li[1])
print ("뒤에서 두번째:", li[-1])
print ("두번째 부터 4번째 앞 까지:",li[1:3])
print ("리스트 결합:", li + li)
print ("리스트 반복:",li * 3)
"""

"""
li = list(range(4)) #range를 이용한 list 생성
print(li)
del li[::2]#짝수번째 데이터 삭제
print(li)
#리스트 내의 모든 객체 순회
for i in li:
    print(i, end="\t")
"""


"""
#list 의 list
innerlist = list(range(4))
outerlist = ['begin', innerlist, 'end']
print(outerlist)
innerlist[0] = 200
print(outerlist)
"""

"""
#정렬
data = [30,50,10,40,20]
data.sort()
print("오름차순:", data)
data.sort(reverse=True)
print("내림차순:",data)
"""

"""
data = ['Morning', 'Afternoon', 'evening' ,'Night' ]
data.sort()
print("대소문자 구분해서 정렬:", data)
data.sort(reverse=True)
print("내림차순 정렬:", data)
data.sort(key=str.lower, reverse=True)
print("내림차순 정렬:", data)
"""


"""
data = [30,50,10,40,20]
print("오름차순:", sorted(data))
print("내림차순:",sorted(data, reverse=True))


data = [30,50,10,40,20]
data = sorted(data)
print("오름차순:", data)
data.reverse()
print("내림차순:",data)
"""


"""
#array
from array import array
from random import random
from time import time

start = time()
floats = array('d', (random() for i in range(10 ** 7)))
end = time()
print(end - start)


start = time()
ar = []
for i in range(10 ** 7):
    ar.append(random())
end = time()
print(end - start)
"""


"""
#deque
from collections import deque
deq = deque()
for i in range(10 ** 7):
    deq.append(1)
"""

"""
from collections import deque

history = deque(maxlen=3)

data = ['두란', '레너드', '헌즈', '해글러']

for boxer in data:
    history.append(boxer)

for boxer in history:
    print(boxer)
"""



"""
#튜플
t = (1,2,3,2,2,3)
print("2의 개수:", t.count(2))
print("2의 위치:", t.index(2))
print("2의 위치:", t.index(2,3))
"""

"""
#튜플의 unpacking
x,y=1,2
x,y=y,x
print(x, y)

a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)
"""


"""
a = 5
if a > 5:
    a = a*2
    print(a)
else:
    a = a-4
    print(a)


a = 5
b = (a-4, a*2) [a>5]
print(b)
"""

"""
#레코드로서의 튜플
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in traveler_ids:
    print('%s/%s' % passport)
print()

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
"""


"""
from collections import namedtuple
City = namedtuple('City', 'name country population')
seoul = City('Seoul', 'Korea', 973.3)
print(seoul.name, seoul.country, seoul.population)
"""


"""
#set
hashset = set()
print(hashset)
hashset = {1,2,3}
print(hashset)
hashset = set((1,2,3,2))
print(hashset)
hashset = set('hello world')
print(hashset)
hashset = set([1,3,2])
print(hashset)
"""

"""
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
"""


"""
#dict
member = {'baseball':9, 'soccer':11,"volleyball":6}
print(member)
print(member['baseball'])
print(member['basketball'])
"""


"""
keys = ['one', 'two', 'three']
values = (1,2,3)
dic = dict(zip(keys, values))
for key in dic:
    print(key,":", dic[key])
"""

"""
#get을 이용한 if
a = 5
if a == 1:
    print("일")
elif a == 2:
    print("이")
elif a == 3:
    print("삼")
else:
    print("알 수 없음")

data = {1 : "일", 2 : "이", 3 : "삼"}
b = data.get(a, "알 수 없음")

print(b)
"""


"""
# 데이터를 생성하는 부분
class Person:
    def __init__(self):
        self.name = ""
        self.age = 0


person1 = Person()
person1.name = '아담'
person1.age = 25

person2 = {'name': "류시아", "age": 24}

# 데이터를 출력하는 부분
print('이름:', person1.name, '\t나이:', person1.age)

for key in person2:
    print(key, ":", person2[key], end='\t')

# 클래스의 속성을 name 에서 nick 으로 변경 하고 dict 의 name 도 nick으로 변경한 후 실행
"""


"""
table = []

person1 = {'name': "사이다", "age": 23}
person2 = {'name': "아담", "age": 25}
person3 = {'name': "류시아", "age": 24}

table.append(person1)
table.append(person2)
table.append(person3)

print('{0:10s}{1:10s}'.format('이름', '나이'))
for person in table:
    print('{0:10s}{1:10s}'.format(person['name'], str(person['age'])))

print()
table.sort(key=lambda d: d['name'])

print('{0:10s}{1:10s}'.format('이름', '나이'))
for person in table:
    print('{0:10s}{1:10s}'.format(person['name'], str(person['age'])))
"""


"""
players = []
players.append({'name':'권투', 'player':['마빈 해글러', '슈거레이 레너드', '토마스 헌즈']})
players.append({'name':'야구', 'player':['조계현', '최향남', '이대진']})
players.append({'name':'축구', 'player':['가린샤', '에우제비오', '차범근']})
players.append({'name':'배구', 'player':['배유나', '한유미']})
players.append({'name':'농구', 'player':['래리 존슨', '알론조 모닝', '레지 밀러', '스카티 피펜']})
players.append({'name':'당구', 'player':['브롬달', '이상천', '세이기너', '차유람']})

for sport in players:
    print('{0:5s}'.format(sport['name']))
    print('\t', end='')
    for player in sport['player']:
          print('{0:10s}'.format(player), end='')
    print('\n')
"""


"""
#enumerate
for idx, element in enumerate(['A', 'B', 'C']):
    print(idx, element)

for idx, key in enumerate({'name':'adam', 'address':'mokdong'}):
    print(idx, key)
"""


"""
#Comprehension
L = [i ** 2 for i in range(10)]
print(L)
"""

"""
# 0부터 4까지 3승을 해서 결과를 가져오기
li1 = [i ** 3 for i in range(5)]
print(li1)

li2 = ['태연', '아이린', '재경']
# li2에서 글자수가 3이상인 데이터만 추출하기
li3 = [i for i in li2 if len(i) > 2]
for imsi in li3:
    print(imsi)

li4 = [1, 2, 3]
li5 = [4, 5, 6]
result = [x * y for x in li4 for y in li5]
print(result)
"""


"""
L = [['a', 'b', 'c'], ['d', 'e', 'f']]
flatten = [j for i in L for j in i]
print(flatten)
extend = [[j + j for j in i] for i in L]
print(extend)
"""


"""
data = [0, 7, 6, 9, 2, 3]
T = tuple((i for i in data))
print(T)

text = "Adam"
S1 = set([i for i in text])
print(S1)
S2 = {i for i in text}
print(S2)

text = "Adam"
D = {i : text.count(i) for i in text}
print(D)
"""

"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
squares = [[x**2 for x in row] for row in matrix]
print(squares)

a = [n**2 for n in range(1, 11) if n % 2 == 0]
print(a)

b = [x for x in range(1, 11) if x > 4 if x % 2 == 0]
c = [x for x in range(1, 11) if x > 4 and x % 2 == 0]
print(b)
print(c)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0] for row in matrix if sum(row) >= 10]
print(filtered)

a = [n**2 if n % 2 == 0 else n ** 3 for n in range(1, 11)]
print(a)
"""


"""
#queue
import queue
li=['태연','아이린','재경']
singer=queue.Queue()
#singer=queue.LifoQueue()
for x in li:
    singer.put(x)

idx = 0
size = singer.qsize()
while idx < size:
    print(singer.get(idx))
    idx = idx + 1
print()
singer=queue.PriorityQueue()
singer.put((30, '태연'))
singer.put((25, '수지'))
singer.put((28, '아이린'))

idx = 0
size = singer.qsize()
while idx < size:
    print(singer.get(idx))
    idx = idx + 1
"""


"""
import queue
q=queue.Queue(2) #아이템이 2개만 저장가능하도록 설정
q.put('태연')
q.put('수지') #큐의 저장 한계
q.put('아이린') #다른 스레드가 아이템을 가지고 갈때까지 무한 대기
"""


"""
import queue
q=queue.Queue(2) #아이템이 2개만 저장가능하도록 설정
q.put_nowait('태연')
q.put_nowait('수지') #큐의 저장 한계
q.put_nowait('아이린')

q.get_nowait()
q.get_nowait()
q.get_nowait() #큐 인스턴스가 빈 경우
"""


"""
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'blue', 'green', 'red'])

print(counter['blue'])
print(counter['red'])
print(dict(counter))
"""


"""
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

from collections import Counter
total_shares = Counter()

# 데이터 개수 세기
for name, shares, price in portfolio:
    total_shares[name] += 1

print(total_shares)
print()

for x in total_shares:
    print(total_shares[x])


# price 의 합계 구하기
print()
total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += price
print(total_shares)

#상위 2개만 추출
print(total_shares.most_common(3))
"""


"""
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))

for x in holdings:
    print(x , " : ", holdings[x])
"""

"""
from collections import OrderedDict
keys = ['one', 'two', 'three']
values = (1,2,3)
dic = dict(zip(keys, values))
for key in dic:
    print(key,":", dic[key])
print("=====================")
dic = OrderedDict(zip(keys, values))
for key in dic:
    print(key,":", dic[key])
"""

"""
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product

l = [1,2,3]
for i in combinations(l,2):
	print(i)

l = ['A', 'B', 'C']
for i in combinations_with_replacement(l,2):
	print(i)

l = ['A', 'B', 'C']
for i in permutations(l): #r을 지정하지 않거나 r=None으로 하면 최대 길이의 순열이 리턴된다!
	print(i)

l1 = ['A', 'B']
l2 = ['1', '2']
for i in product(l1,l2,repeat=1): #l1과 l2의 모든 쌍을 지어 리턴한다
	print(i)

for i in product(l1,repeat=3): #product(l1,l1,l1,repeat=1)과 동일한 출력
	print(i)
"""