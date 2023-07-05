"""
#if

var1 = True
if var1:
    print("1 - True 일 때 수행될 문장")
    print(var1)

# 숫자 0은 False 로 간주
var2 = 0
if var2:
    print("2 - True 일 때 수행될 문장")
    print(var2)

var3 = [1]
if var3:
    print("3 - 데이터가 있으면 True")
    print(var3)

var3 = []
if var3:
    print("4 - 데이터가 없으면 False")
    print(var3)

var3 = None
if var3:
    print("3 - None 이어도 False")
    print(var3)

print("프로그램 종료!")
"""

"""
#점수를 입력받아서 60점 이상이면 합격 아니면 불합격이라고 출력
score = int(input("점수를 입력하세요:"))
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")
"""


"""
#변수에 값 할당을 if, else로 축약 – 삼항 연산자 처럼 사용
x = 5
if x == 10:
    y = True
else:
    y = False
print(y)

x = 10
y = True if x == 10 else False
print(y)
"""


"""
#1번을 누르면 아메리카노 2번을 누르면 카페라떼 3번을 누르면 에스프레소를 나머지를 누르면 제공하지 않는 메뉴라고 출력하기
menu = input("메뉴를 입력하세요:")
if menu == '1':
    print('아메리카노')
elif menu == '2':
    print('카페 라떼')
elif menu == '3':
    print('에스프레소')
else:
    print('잘못된 메뉴를 입력')
"""

"""
#switch
switcher = {
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
    }

print(switcher.get(3, 'Unknown Week'))
"""

"""
#while
limit = int(input('몇 번 반복할까요: '))

count = 0
while count < limit:
    count = count + 1
    print('%d회 반복.' % (limit))

print('반복이 종료되었습니다.')
"""

"""
#excel1.xls 부터 excel3.xls 파일을 읽기
print('--반복문을 사용하지 않는 경우')
print('excel1.xls 파일 읽기')
print('excel2.xls 파일 읽기')
print('excel3.xls 파일 읽기')

print('--반복문을 사용하는 경우')
i = 1
while i <= 3:
    print('excel%d.xls 파일 읽기'%(i))
    i = i+1
"""


"""
#구구단 2단 출력
i = 0
while i < 9:
    i = i + 1
    print('2 * %d = %d'%(i, 2*i))
"""

"""
#한겨레 주소 만들기
keyword = input("검색어를 입력하세요 :")
pagenumber = 0
while pagenumber < 3:
    url = "http://search.hani.co.kr/Search?command=query&keyword="+ keyword + "&media=news&submedia=&sort=d&period=all&datefrom=2000.01.01&dateto=2019.06.24&pageseq=" + str(pagenumber)
    print(url)
    pagenumber = pagenumber + 1
"""

"""
#3번 반복 수행한 후 다른 동작 수행
i = 0
while i < 3:
    i = i + 1
    print('2 * {0} = {1}'. format(i, 2*i))
else:
    print("반복문을 정상적으로 종료하였습니다.")
"""

"""
#( ) 안의 내용을 순서대로 가져와서 출력
for i in (1, 2, 3) :
	print(i)
else:
    print("반복문을 정상적으로 수행했습니다.")
"""

"""
#range
print(list(range(10)))#종료 값만 있는 경우
print(list(range(5, 10)))#시작 값과 종료 값만 있는 경우
print(list(range(10, 0, -1)))#3가지 값을 모두 대입한 경우
#10에서 20까지의 짝수를 출력하는 경우
for i in range(10,20,2):
    print(i, end="\t")
"""


"""
#구구단 전체 출력
print("★ 구구단을 출력★\n")
for x in range(1, 10):
    for y in range(2, 10):
        print(y,"X",x,"=",format(x*y,'2d'),end=" ")
    print('')
"""

"""
#*을 5개씩 5개 출력
for x in range(0, 5):
    for y in range(0, 5):
        print('{0}'.format('*'), end='')
    print('')
"""


"""
#삼각형 모양의 별 출력
for x in range(0, 5):
    for y in range(0, x+1):
        print('{0}'.format('*'), end='')
    print('')
"""

"""
#삼각형 모양의 별 출력
for x in range(0, 5):
    for y in range(0, 5 - x):
        print('{0}'.format(' '), end='')

    for y in range(0, 2 * x + 1):
        print('{0}'.format('*'), end='')
    print('')
"""


"""
#continue
for i in range(10):
    if i % 2 == 1:
        continue

    print(i)
"""


"""
#break
i = 0
while(True):
    i = i+1
    if i == 1000:
        print('i가 %d값이 됐습니다. 반복문을 중단합니다.'%(i))
        break
    print(i)
"""


"""
#for - break - else
for i in (1, 2, 3):
    if(i%3 == 0):
        break
    print(i)
else:
    print("반복문을 정상적으로 종료한 경우에만 수행합니다.")
print("무조건 수행합니다.")
"""







