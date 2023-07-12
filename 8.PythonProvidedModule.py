"""
import time

#현재 시간을 실수로 가져오기
print(time.time())
#현재 시간을 struct_time 형식으로 가져오기
print(time.gmtime())
#년도만 가져오기
print(time.localtime().tm_year)
t1 = time.time()
#10초 대기
time.sleep(10)
t2 = time.time()
#시간에서 시간을 빼서 경과한 시간 만들기
spendtime = t2-t1
print("Wait seconds ", spendtime)
"""

"""
import datetime
#현재 시간을 저장
dt = datetime.datetime.now()
#전체 시간을 출력
print("현재시간:", dt)
#각 속성을 분할해서 출력
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)
print("요일:",dt.weekday())

#문자열을 가지고 datetime 생성
dt1 = datetime.datetime.strptime("2015-12-31 11:32", "%Y-%m-%d %H:%M")
print(dt1)

#datetime을 문자열로 생성
s = dt1.strftime('%Y %m %d %H %M %S')
print(s)
"""

"""
import datetime

#현재 날짜 및 시간을 저장
dt = datetime.datetime.now()
#날짜와 시간을 추출
print(dt.date())
print(dt.time())

#날짜 및 시간을 가지고 datetime을 생성
d = datetime.date(2015, 12, 31)
print(d)
t = datetime.time(11, 31, 29)
print(datetime.datetime.combine(d, t))

#2개의 datetime의 차이
dt1 = datetime.datetime(2016, 2, 19, 14, 11, 9)
dt2 = datetime.datetime(2016, 1, 2, 13, 16, 23)
td = dt1 - dt2
print(td)
print(td.days, td.seconds, td.microseconds)

#문자열을 날짜로 변환
from dateutil.parser import parse
print(parse('2016-04-16'))
"""

"""
#분수 표현
from fractions import Fraction
#분수를 생성해서 더라기
a = Fraction(5,7) + Fraction('2/5')
print(a)
#분수 빼기
a = a - Fraction(5,7)
print(a)
#분수 나누기
a = a * Fraction(5,7)
print(a)
#소수를 이용해서 분수 생성
a = Fraction("1.24")
print(a)
#버림, 올림, 반올림
print(a.__floor__())
print(a.__ceil__())
print(a.__round__())
"""


"""
#경로 추출
import os.path
#현재 경로에 temp를 붙여서 리턴
print(os.path.abspath('temp'))

#마지막 경로만 리턴
print(os.path.basename('c:\\data'))

#문자열 차원에서 추출하므로 이상한 결과가 리턴될 수 있음
print(os.path.commonprefix(['C:\\Python30\\Lib', 'C:\\Python30', 'C:\\Python30\\Tools']))
print(os.path.commonprefix(['C:\\Python26\\Lib', 'C:\\Python25\\Tools']))
"""

"""
import os
import time

#파일의 경로를 변경해서 수행
print("접근시간:",os.path.getatime('./8.PythonProvidedModule.py'))

#타입 변환
print(time.gmtime(os.path.getatime('./8.PythonProvidedModule.py')))
print("수정시간:",os.path.getmtime('./8.PythonProvidedModule.py'))
print("생성시간:",os.path.getctime('./8.PythonProvidedModule.py'))

print(os.path.split('./8.PythonProvidedModule.py'))
print(os.path.splitext('./8.PythonProvidedModule.py'))
"""

"""
import os, glob
file_list = os.listdir("./")
print(file_list)
print(glob.glob('./*.py'))
print(glob.iglob('./*.py'))
"""


"""
import os
print("현재 작업 디렉토리:",os.getcwd())
print("현재 작업 디렉토리에 대한 정보:", os.stat(os.getcwd()))
"""


"""
import os
print("운영체제:", os.name)
print("환경변수 목록:", os.environ)
print("현재 프로세스 id:", os.getpid())
os.system("ls") #windows 에서는 os.system('dir')
"""

"""
import sys
print("파이썬이 설치된 경로:", sys.prefix)
msg = "Hello"
print("msg의 참조 개수:", sys.getrefcount(msg))
s1 = msg
print("msg의 참조 개수:", sys.getrefcount(msg))
s2 = msg
print("msg의 참조 개수:", sys.getrefcount(msg))
print("현재 인코딩 방식:", sys.getdefaultencoding())
print("현재 사용 중인 모듈:", sys.modules)
"""


"""
a = 1
b = 1
print(id(a))
print(id(b))
"""


"""
a = [1,2,3]
b = a
a[0]=100

print("a의 id:", id(a));
print("b의 id:", id(b));

print("a의 첫번째 요소:",a[0])
print("b의 첫번째 요소:",b[0])
"""

"""
a = [1,2,3]
b = a[0:3]

a[0]=300
print("a[0]:", a[0])
print("b[0]:", b[0])
"""


"""
import copy
a = [1,2,3]
x = [a, 100]
y = copy.copy(x)

#copy를 했으므로 2개의 아이디는 다름
print("x의 아이디:", id(x));
print("y의 아이디:", id(y));

#두번째 데이터는 일반적인 데이터이므로 복제가 이루어짐
x[1] = 200
print("x[1]:",x[1])
print("y[1]:",y[1])

#첫번째 데이터는 다시 데이터의 모임이므로 주소의 복제를 수행
x[0][0] = 300
print("x[0][0]:",x[0][0])
print("y[0][0]:",y[0][0])
"""

"""
import copy
a = [1,2,3]
x = [a, 100]
y = copy.deepcopy(x)

#copy를 했으므로 2개의 아이디는 다름
print("x의 아이디:", id(x));
print("y의 아이디:", id(y));

#첫번째 데이터는 다시 데이터의 모임이므로 재귀적으로 복제를 수행
x[0][0] = 300
print("x[0][0]:",x[0][0])
print("y[0][0]:",y[0][0])
"""


"""
#약한 참조
import weakref
class Temp:
  def __init__(self):
    self.value = 1
  def __del__(self):
    print('인스턴스가 파괴됩니다.')

a = Temp()
b = weakref.ref(a)
a = 1
"""


"""
import time

def threadEx(id):
    for i in range(10):
        print('id={0} --> {1}'.format(id, i))
        time.sleep(1)

for i in range(2):
    threadEx("{0}번 스레드".format(i))
"""

"""
import threading, time

def threadEx(id):
    for i in range(10):
        print('id={0} --> {1}'.format(id, i))
        time.sleep(1)

for i in range(2):
    id = ("{0}번 스레드".format(i))
    th = threading.Thread(target=threadEx, args=(id,))  # 쓰레드 함수를 target인수로, 쓰레드로 전달될 인수를 args인수에 전달
    th.start()
print("메인 종료")          # 쓰레드 실행 시작
"""

"""
import threading, time

class ThreadEx(threading.Thread):
    def run(self):
        for i in range(10):
            print('id={0} --> {1}'.format(self.getName(), i))
            time.sleep(1)

for i in range(2):
    th = ThreadEx()
    th.start() 
"""


"""
import threading, time
g_count = 0

class ThreadEx(threading.Thread):
    def run(self):
        global g_count
        for i in range(10):
            print('id={0} 증가하기 전 --> {1}'.format(self.getName(), g_count))
            g_count = g_count + 1
            time.sleep(0.5)
            print('id={0} 증가한 후 --> {1}'.format(self.getName(), g_count))
            time.sleep(0.5)

for i in range(2):
    th = ThreadEx()
    th.start()
"""


"""
import threading, time
g_count = 0
lock = threading.Lock()

class ThreadEx(threading.Thread):
    def run(self):
        global g_count
        global lock
        for i in range(10):
            lock.acquire()
            print('id={0} 증가하기 전 --> {1}'.format(self.getName(), g_count))
            g_count = g_count + 1
            time.sleep(0.5)
            print('id={0} 증가한 후 --> {1}'.format(self.getName(), g_count))
            lock.release()
            time.sleep(0.5)

for i in range(2):
    th = ThreadEx()
    th.start()
"""


"""
import threading, time

shareData = []


class Producer(threading.Thread):
    def run(self):
        global shareData;
        for i in range(10):
            print("공유자원 생성")
            shareData.append(i)
            time.sleep(1)


class Customer(threading.Thread):
    def run(self):
        global shareData;
        for i in range(10):
            print("공유자원 사용")
            print(shareData.pop())
            time.sleep(1)

producer = Producer()
customer = Customer()

producer.start()
customer.start()
"""


"""
import threading, time
shareData = []
cv = threading.Condition()
class Producer(threading.Thread):
    def run(self):
        global shareData;
        for i in range(10):
            cv.acquire()
            print("공유자원 생성")
            shareData.append(i)
            time.sleep(1)
            cv.notify()
            cv.release()

class Customer(threading.Thread):
    def run(self):
        global shareData;
        for i in range(10):
            cv.acquire()
            if len(shareData) < 1:
                cv.wait(0)
            print("공유자원 사용")
            print(shareData.pop())
            time.sleep(1)
            cv.release()

producer = Producer()
customer = Customer()

producer.start()
customer.start()
"""


"""
import threading, time
sema = threading.Semaphore(3)
class ThreadEx(threading.Thread):
    def run(self):
        sema.acquire()
        time.sleep(5)
        print(self.getName())
        sema.release()

for i in range(10):
    th = ThreadEx()
    th.start()
"""

"""
import socket
print(socket.getservbyname('http', 'tcp'))
print(socket.getservbyname('ftp', 'tcp'))
"""

"""
#서버 코드
from socket import *
try:
    svrsock = socket(AF_INET, SOCK_STREAM)
    svrsock.bind(('localhost', 8000))
    svrsock.listen(1)
    print("서버 대기 중")
    conn, addr = svrsock.accept()
    print(addr)
    b = conn.recv(1024)
    conn.send('Hello Client'.encode())
    print(b.decode())
except Exception as e:
    print("예외가 발생했습니다.", e)
finally:
    conn.close()
"""

"""
from socket import *
try:
    svrsock = socket(AF_INET, SOCK_DGRAM)
    svrsock.bind(('localhost', 8001))
    while True:
        print("서버 대기 중...")
        s, addr = svrsock.recvfrom(1024)
        print("접속한 곳:{0}".format(addr))
        print("메시지:" + s.decode())
        svrsock.sendto(s, addr)
except Exception as e:
    print("예외 발생:", e)
finally:
    svrsock.close()
"""


"""
#서버 - 나중에 실행 - 자신의 아이피를 확인해서 아이피는 수정하세요
from socket import *
try:
    svrsock = socket(AF_INET, SOCK_DGRAM)
    #브로드 캐스팅 옵션 설정
    svrsock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    svrsock.sendto('Broadcasting Message'.encode(), ('192.168.0.115', 8000))
    print("전송 성공")
except Exception as e:
    print("접속 에러:", e)
finally:
    svrsock.close()
"""



"""
#채팅 서버
import socketserver
import threading

HOST = ''
PORT = 9009
lock = threading.Lock()


class UserManager:
    def __init__(self):
        self.users = {}

    def addUser(self, username, conn, addr):
        if username in self.users:
            conn.send('이미 등록된 사용자입니다.\n'.encode())
            return None

        # 새로운 사용자를 등록함
        lock.acquire()
        self.users[username] = (conn, addr)
        lock.release()

        self.sendMessageToAll('[%s]님이 입장했습니다.' % username)
        print('+++ 대화 참여자 수 [%d]' % len(self.users))

        return username

    def removeUser(self, username):
        if username not in self.users:
            return

        lock.acquire()
        del self.users[username]
        lock.release()

        self.sendMessageToAll('[%s]님이 퇴장했습니다.' % username)
        print('--- 대화 참여자 수 [%d]' % len(self.users))


    def messageHandler(self, username, msg):
        if msg[0] != '/':
            self.sendMessageToAll('[%s] %s' % (username, msg))
            return

        if msg.strip() == '/quit':
            self.removeUser(username)
            return -1

    def sendMessageToAll(self, msg):
        for conn, addr in self.users.values():
            conn.send(msg.encode())

class MyTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()

    def handle(self):
        print('[%s] 연결됨' % self.client_address[0])

        try:
            username = self.registerUsername()
            msg = self.request.recv(1024)
            while msg:
                print(msg.decode())
                if self.userman.messageHandler(username, msg.decode()) == -1:
                    self.request.close()
                    break
                msg = self.request.recv(1024)
        except Exception as e:
            print(e)

        print('[%s] 접속종료' % self.client_address[0])
        self.userman.removeUser(username)

    def registerUsername(self):
        while True:
            self.request.send('로그인ID:'.encode())
            username = self.request.recv(1024)
            username = username.decode().strip()
            if self.userman.addUser(username, self.request, self.client_address):
                return username

class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def runServer():
    print('+++ 채팅 서버를 시작합니다.')
    print('+++ 채텅 서버를 끝내려면 Ctrl-C를 누르세요.')

    try:
        server = ChatingServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('--- 채팅 서버를 종료합니다.')
        server.shutdown()
        server.server_close()

runServer()
"""