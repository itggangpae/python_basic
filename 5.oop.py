"""
#Student Class를 생성하고 인스턴스를 만들고 Method를 사용

# Class 선언
class Student:
    # 인스턴스가 있어야만 호출가능한 Method 생성
    def insa(self):
        print('안녕하세요')

    # 인스턴스가 있어야만 호출가능한 Method 생성
    def printName(self, name):
        # Method 내부에서 다른 Method 호출
        self.insa()
        print('이름은', name)


# 인스턴스 생성
stu = Student()
# 바운드 호출
stu.printName("사이버가수 아담")
# 언바운드 호출
Student.printName(stu, "군계")
"""

"""
import time
class Student:
    # 생성자
    def __init__(self, name="사이버가수"):
        print(time.ctime(), "에 인스턴스가 생성되었습니다.")
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

student = Student()

student.setName('아담')
"""


"""
class Student:
    schoolName = "Korea"

stu1 = Student()
stu2 = Student()

print("stu1의 참조:",id(stu1))
print("stu2의 참조:",id(stu2))
print("===========================")

#schoolName은 Method 외부에 만들어진 것이므로 class 변수가 되고
#Class 변수는 1개만 만들어서
#Class와 Class로부터 만들어진 인스턴스 모두가 공유해서 사용
#따라서 아래 3개의 출력문은 모두 동일한 값을 출력

print("Student의 학교:",Student.schoolName)
print("stu1의 학교:",stu1.schoolName)
print("stu2의 학교:",stu2.schoolName)
print("===========================")

#Class를 이용해서 Attribute을 변경하면 Class Attribute이 변경됨
Student.schoolName="Seoul"
print("Student의 학교:",Student.schoolName)
print("stu1의 학교:",stu1.schoolName)
print("stu2의 학교:",stu2.schoolName)
print("===========================")

#인스턴스를 이용해서 Attribute의 값을 수정하면 Class Attribute을 수정하는 것이 아니고
#자신에게 없는 Attribute이면 생성하고 없는 Attribute이면 수정
stu1.schoolName = "KAIST"
print("Student의 학교:",Student.schoolName)
print("stu1의 학교:",stu1.schoolName)
print("stu2의 학교:",stu2.schoolName)
"""

"""
#Accessor 생성과 호출
class Student:
    #Method를 만들 때 첫번째 매개변수는 인스턴스의 참조를 기억하는 self
    def getName(self):
        #인스턴스가 각각 소유하는 name의 값을 리턴
        return self.name

    #매개변수가 2개인 함수
    def setName(self, name):
        #매개변수로 받은 내용을 인스턴스가 각각 소유하는 name에 대입
        self.name = name

#객체 자신의 name에 값을 설정
student1 = Student()
student1.setName('아담')

student2 = Student()
student2.setName('류시아')

#객체 자신의 값을 가져오기 때문에 내용이 다름
print(student1.getName())
print(student2.getName())
"""


"""
#매개변수가 없는 초기화 Method를 이용해서 인스턴스를 생성하고 Method 호출
class Student:
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

student1 = Student()
student1.setName('아담')
print(student1.getName())

student2 = Student()
print(student2.getName())
"""


"""
import time
class Student:
    # 생성자
    def __init__(self, name="사이버가수"):
        print(time.ctime(), "에 인스턴스가 생성되었습니다.")
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    # 소멸자
    def __del__(self):
        print(time.ctime(), "에 인스턴스가 소멸되었습니다.")


student1 = Student()
student1.setName('아담')
print(student1.getName())

student2 = Student()
print(student2.getName())

#객체의 소멸은 None을 대입해서 retain count를 1감소 시켜서 0을 만들어서 삭제
student1 = None
student2 = None
"""


"""
#참조 횟수 확인
import sys
import time
class Student:
    # 생성자
    def __init__(self, name="사이버가수"):
        print(time.ctime(), "에 인스턴스가 생성되었습니다.")
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    # 소멸자
    def __del__(self):
        print(time.ctime(), "에 인스턴스가 소멸되었습니다.")

student1 = Student()
print(sys.getrefcount(student1))
student1 = None
#아래 문장은 에러
#print(student1.getName())

student2 = Student()
print(sys.getrefcount(student2))
student3 = student2
print(sys.getrefcount(student2))
student2 = None
print(student3.getName())
"""

"""
class Student:
    @classmethod
    def cmethod(cls):
        print("Class Method")
        print(cls)

    @staticmethod
    def smethod():
        print("정적 Method")

#클래스를 이용한 method
Student.cmethod()
Student.smethod()

#인스턴스를 이용한 method
student = Student()
student.cmethod()
student.smethod()
"""

"""
class Student:
    name = ""
    score = 0


student = Student()
student.name = "제시카"
student.score = 90
student.tel = "01031391997"
print(student.tel)
"""


"""
class Student:
    __slots__ = ["name", "score"]

student = Student()
student.name = "제시카"
student.score = 90
student.tel = "01031391997"
print(student.tel)
"""


"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

maria = Student('마리아', 20)
maria.name = "Maria"
maria.__age -= 1  # Class 외부에서 비공개 Attribute에 접근하면 에러가 발생함
"""


"""
#Property
class Student:
    def __init__(self, name="noname"):
        self.__name = name

    def setName(self, name):
        print("setter 호출")
        self.__name = name

    def getName(self):
        print("getter 호출")
        return self.__name

    name = property(getName, setName)


stu = Student()
# 아래 문장은 변수를 호출한 것이 아니고 Accessor를 호출한 것
stu.name = "adam"
print(stu.name)
"""


"""
#Decorator를 이용한 Property
class Student:

    def __init__(self, name="noname"):
        self.__name = name

    @property
    def name(self):
        print("getter 호출")
        return self.__name

    @name.setter
    def name(self, name):
        print("setter 호출")
        self.__name = name

stu = Student()
stu.name = "아담"
print(stu.name)
"""


"""
#Operator Overloading
class Student:
    def __init__(self, name="noname"):
        self.__name = name

    def setName(self, name):
        print("setter 호출")
        self.__name = name

    def getName(self):
        print("getter 호출")
        return self.__name

    def __add__(self, other):
        return self.name + "," +  other.name


stu1 = Student()
stu1.name = "아담"

stu2 = Student()
stu2.name = "류시아"

print(stu1 + stu2)
"""

"""
class Student:
    def __init__(self, name="noname"):
        self.__name = name

    def setName(self, name):
        print("setter 호출")
        self.__name = name

    def getName(self):
        print("getter 호출")
        return self.__name

    def __str__(self):
        return self.name

stu = Student()
stu.name = "아담"
print(stu)
"""


"""
class Square:
    def __init__(self, end):
        self.end = end

    def __len__(self):
        return self.end

    def __getitem__(self, k):
        if type(k) != int:
            raise TypeError('...')
        if k < 0 or self.end <= k:
            raise IndexError('index {} out of range'.format(k))
        return k * k


s1 = Square(10)
print(len(s1))
print(s1.__getitem__(4))
print(s1[4])
print(s1[20])
"""


"""
class MyDict:
    def __init__(self):
        self.d = {}

    def __getitem__(self, k):  # key
        return self.d[k]

    def __setitem__(self, k, v):
        self.d[k] = v

    def __len__(self):
        return len(self.d)


m = MyDict()
m.__setitem__('night', 'darkness')
m['day'] = 'light'

print(m['day'])
print(m['night'])
print(len(m))
"""


"""
#Singleton Pattern
class Singleton:
    __instance = None  # 유일한 객체를 저장하기 위한 클래스 변수

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # 새로운 객체를 생성한다.
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance


class Sub(Singleton):  # 싱글톤으로부터 상속받는다.
    pass


s1 = Sub()
s2 = Sub()
print(s1 is s2)
"""


#단일 상속
class Person:
    def greeting(self):
        print('안녕하세요.')

"""
class Student(Person):
    def study(self):
        print('공부하기')


student = Student()
student.greeting()  # 기반 Class Person의 Method 호출
student.study()  # 파생 Class Student에 추가한 study Method
"""


"""
#상위 클래스의 메서드 호출
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'


class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 학교'


student = Student()
print(student.school)
print(student.hello)  # 기반 Class의 Attribute을 출력하려고 하면 에러가 발생함
"""


"""
#상위 클래스의 프로퍼티 호출
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'


class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()  # super()로 기반 Class의 Method 호출
        self.school = '파이썬 학교'


student = Student()
print(student.school)
print(student.hello)
"""


"""
#Method Overriding
class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def greeting(self):
        super().greeting()
        print('반갑습니다.')

student = Student()
student.greeting()
"""


"""
#다중 상속
class Base1:
    def __init__(self):
        print('첫번째 상위 클래스의 초기화 method')

    def method(self):
        print('첫번째 상위 클래스의 method')


class Base2:
    def __init__(self):
        print('두번째 상위 클래스의 초기화 method')

    def method(self):
        print('두번째 상위 클래스의 method')


class Derived(Base1, Base2):
    def __init__(self):
        # 첫번째 상위 클래스의 초기화 method
        super().__init__()
        # 두번째 상위 클래스의 초기화 method
        super(Base1, self).__init__()
        print('하위 클래스의 초기화 method')

    def method(self):
        # 첫번째 상위 클래스의 method() 호출
        super().method()
        # 두번째 상위 클래스의 method() 호출
        super(Base1, self).method()
        print('하위 클래스의 method')


drived = Derived()
print()
drived.method()
"""



"""
import abc
#추상 클래스
class ChineseRestaurant(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def jajangmyeon(self):
        pass


class Magnoliaceae(ChineseRestaurant):
    pass


magnoliaceae = Magnoliaceae()
"""


"""
import abc
class ChineseRestaurant(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def jajangmyeon(self):
        pass


class Magnoliaceae(ChineseRestaurant):
    def jajangmyeon(self):
        print('이연복이 만든 짜장면')


magnoliaceae = Magnoliaceae()
magnoliaceae.jajangmyeon()
"""


"""
#Delegation
class Delegation:
    def __init__(self, data):
        self.data = data

    def __getattr__(self, name):
        print(name + "호출")
        #self.data 의 count Method 호출
        return getattr(self.data, name)

instance = Delegation([100,200,300,200,200])
print(instance.count(200))
"""


"""
#iterator
li = [1, 2, 3]
it = li.__iter__()
#iterator 출력하기
print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
"""

"""
#iterator 구현
class IteratorImpl:
    def __init__(self, stop):
        self.current = 0  # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop  # 반복을 끝낼 숫자

    def __iter__(self):
        return self  # 현재 인스턴스를 반환

    def __next__(self):
        if self.current < self.stop:  # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current  # 반환할 숫자를 변수에 저장
            self.current += 1  # 현재 숫자를 1 증가시킴
            return r  # 숫자를 반환
        else:  # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration  # 예외 발생


for i in IteratorImpl(3):
    print(i, end=' ')
"""

"""
#enumerator
study = ['파이썬', '자료구조', '알고리즘', '웹 프로그래밍', '데이터 분석']
for idx, subject in enumerate(study):
    print(idx, ':', subject)
"""


"""
#Generator
def gen():
    yield 1
    yield 2
    yield 3

# Generator 인스턴스
g = gen()
print(type(g))  # <class 'generator'>

# for 루프 사용 가능
for x in g:
    print(x)
"""


"""
def reverse(data):
    for idx in range(len(data)-1, -1, -1):
        yield data[idx]

for ch in reverse('Teacher'):
    print(ch)
"""



"""
def upper_generator(x):
    for i in x:
        yield i.upper() # 함수의 반환값을 바깥으로 전달

study = ['Python', 'DataStructure', 'Algorithm', 'Web_Programming', 'Data_Analysis']

for i in upper_generator(study):
    print(i)
"""


"""
def tot_coroutine():
    tot = 0
    while True:  # coroutine을 계속 유지하기 위해 무한 루프 사용
        x = (yield)  # coroutine 바깥에서 값을 받아옴
        tot = tot + x
        print('현재까지의 합:', tot)


co = tot_coroutine()
next(co)  # coroutine 안의 yield까지 코드 실행(최초 실행)

co.send(1)  # coroutine에 숫자 1을 보냄
co.send(2)  # coroutine에 숫자 2을 보냄
co.send(3)  # coroutine에 숫자 3을 보냄
"""


"""
#coroutine
def tot_coroutine():
    total = 0
    while True:
        x = (yield total)  # coroutine 바깥에서 값을 받아오면서 바깥으로 값을 전달
        total += x


co = tot_coroutine()
print(next(co))  # 0: coroutine 안의 yield까지 코드를 실행하고 coroutine에서 나온 값 출력

print(co.send(1))  # 1: coroutine에 숫자 1을 보내고 coroutine에서 나온 값 출력
print(co.send(2))  # 3: coroutine에 숫자 2를 보내고 coroutine에서 나온 값 출력
print(co.send(3))  # 6: coroutine에 숫자 3을 보내고 coroutine에서 나온 값 출력
"""


"""
def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    except GeneratorExit:  # coroutine이 종료 될 때 GeneratorExit 예외 발생
        print()
        print('coroutine 종료')


co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()
"""


"""
#Decorator
def is_multiple(x):  # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func):  # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):  # 호출할 함수의 매개변수와 똑같이 지정
            r = func(a, b)  # func을 호출하고 반환값을 변수에 저장
            if r % x == 0:  # func의 반환값이 x의 배수인지 확인
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r  # func의 반환값을 반환

        return wrapper  # wrapper 함수 반환

    return real_decorator  # real_decorator 함수 반환


@is_multiple(3)  # @데코레이터(인수)
def add(a, b):
    return a + b


print(add(10, 20))
print(add(2, 5))
"""


"""
# 적재된 모듈 이름 확인
import sys
from math import sin

print(type(sys.modules))
print()
#print('\n'.join(sys.modules.keys()))

print()
print(sin.__module__)

print()
a = 1
current_module = sys.modules[__name__] # 현재 모듈 얻어내기
print(getattr (current_module, 'a')) # 현재 모듈에서 a의 값 얻어내기
"""


