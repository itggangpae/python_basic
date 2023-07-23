# MySQL

"""
#데이터 삽입
import sys, pymysql

try:
    # 데이터베이스 연결
    con = pymysql.connect(host='localhost',
                          port=3306, user='adam', passwd='wnddkd', db='adam', charset='utf8')
    cursor = con.cursor()

    # 데이터 삽입 - 파라미터 없이 직접 값 입력
    cursor.execute("insert into usertbl values('ljy', '이진연', 1970, '서울', '01012345678', '1970-10-31')")
    # 데이터 삽입 - 파라미터를 이용해서 값 대입
    cursor.execute("insert into usertbl values(%s, %s, %s, %s, %s, %s)",
                   ('sohye', '김소혜', 1999, '서울', '01012121212', '1999-7-19'))
    # 작업 종료
    con.commit()
    print("삽입 성공")
except:
    print('exception:', sys.exc_info())
finally:
    con.close()
"""


"""
#데이터 수정 및 삭제
import sys, pymysql
try:
    #데이터베이스 연결
    con = pymysql.connect(host='localhost',
                          port=3306, user='adam', passwd='wnddkd', db='adam', charset='utf8')
    cursor = con.cursor()

    #데이터 수정
    cursor.execute("update usertbl set name='이지연' where name = '이진연'")
    #데이터 삭제
    cursor.execute("delete from usertbl where name = '김소혜'")
    con.commit()
    print("편집 성공")
except:
    print('exception:', sys.exc_info())
finally:
    con.close()
"""



"""
#데이터 1개 조회
import sys, pymysql

try:
    # 데이터베이스 연결
    con = pymysql.connect(host='localhost',
                          port=3306, user='adam', passwd='wnddkd', db='adam', charset='utf8')
    cursor = con.cursor()

    # 데이터 읽어오는 SQL 실행
    cursor.execute("select * from usertbl")
    # 데이터 1개를 튜플로 가져오기
    data = cursor.fetchone()
    # 튜플을 순회하면서 출력
    for imsi in data:
        print(imsi)
except:
    print('exception:', sys.exc_info())
finally:
    con.close()
"""


"""
#데이터 여러 개 조회
import sys, pymysql

try:
    # 데이터베이스 연결
    con = pymysql.connect(host='localhost',
                          port=3306, user='adam', passwd='wnddkd', db='adam', charset='utf8')
    cursor = con.cursor()

    # 데이터 읽어오는 SQL 실행
    cursor.execute("select * from usertbl")
    # 전체 데이터를 가져와서 튜플의 튜플로 생성
    data = cursor.fetchall()
    for imsi in data:
        print(imsi)
except:
    print('exception:', sys.exc_info())
finally:
    con.close()
"""


"""
#프로시저 실행
import sys, pymysql
try:
    con = pymysql.connect(host='localhost',
                           port=3306, user='adam', passwd='wnddkd', db='adam', charset ='utf8')
    cursor = con.cursor()
    cursor.callproc('myproc', args=('momo', '모모', 1996, '교토', '01098765432', '1996-11-9'))
    con.commit()
except:
    print('exception:', sys.exc_info())
finally:
    con.close()
"""


"""
#blob 저장
import sys, pymysql
#자신의 이미지 파일 경로를 사용하세요
# read file
filename = 'data/image1.png'

#파일을 열어서 내용을 읽어서 photo에 저장
f =  open(filename, 'rb')
photo = f.read()
f.close()

#파일이름만 추출
sp = filename.split('/')

query = 'insert into blobtable values(%s, %s, %s)'
args = ('태연', sp[len(sp)-1], photo)
try:
    con = pymysql.connect(host='localhost',
    port=3306, user='adam', passwd='wnddkd', db='adam', charset ='utf8')
    cursor = con.cursor()
    cursor.execute(query, args)
    con.commit()
    print("삽입성공")
except:
    print('exception:', sys.exc_info())
finally:
    cursor.close()
    con.close()
"""


"""
import sys, pymysql
try:
    con = pymysql.connect(host='localhost',
                           port=3306, user='adam', passwd='wnddkd', db='adam', charset ='utf8')
    cursor = con.cursor()
    cursor.execute("select * from blobtable")
    data = cursor.fetchall()
    for imsi in data:
        print(imsi[0])
        print(imsi[1])
        #파일을 기록
        f = open('data/' + imsi[1], 'wb')
        f.write(imsi[2])
        f.close()
except:
    print('exception:', sys.exc_info())
finally:
    con.close()
"""


"""
#Oracle
# 모듈을 불러옵니다.
import cx_Oracle
import sys

try:
    # 데이터베이스에 연결합니다.
    dsnStr = cx_Oracle.makedsn("localhost", "1521", "xe")
    con = cx_Oracle.connect(user="system", password="wnddkd", dsn=dsnStr)
    print(con)
except:
    print('exception:', sys.exc_info())
finally:
    con.close()
"""


"""
import cx_Oracle

try:
    # 데이터베이스에 연결합니다.
    dsnStr = cx_Oracle.makedsn("localhost", "1521", "xe")
    con = cx_Oracle.connect(user="system", password="wnddkd", dsn=dsnStr)

    cursor = con.cursor()
    # cursor.execute("insert into dept(deptno, dname, loc) values(50, '총무', '목포')")
    cursor.execute('insert into dept values(:1, :2, :3)', (60, '영업', '서울'))

    con.commit()
    print("삽입 성공")
except Exception as e:
    print('exception:', e)
finally:
    con.close()
"""


"""
import cx_Oracle

try:
    # 데이터베이스에 연결합니다.
    dsnStr = cx_Oracle.makedsn("localhost", "1521", "xe")
    con = cx_Oracle.connect(user="system", password="wnddkd", dsn=dsnStr)

    cursor = con.cursor()
    cursor.execute('update dept set dname = :1 where deptno = :2', ('회계', 60))

    con.commit()
    print("수정 성공")
except Exception as e:
    print('exception:', e)
finally:
    con.close()
"""


"""
import cx_Oracle

try:
    # 데이터베이스에 연결합니다.
    dsnStr = cx_Oracle.makedsn("localhost", "1521", "xe")
    con = cx_Oracle.connect(user="system", password="wnddkd", dsn=dsnStr)

    cursor = con.cursor()
    cursor.execute('delete from dept where deptno = :1', (60,))

    con.commit()
    print("삭제 성공")
except Exception as e:
    print('exception:', e)
finally:
    con.close()
"""


"""
import cx_Oracle

try:
    # 데이터베이스에 연결합니다.
    dsnStr = cx_Oracle.makedsn("localhost", "1521", "xe")
    con = cx_Oracle.connect(user="system", password="wnddkd", dsn=dsnStr)

    cursor = con.cursor()

    cursor.execute("select * from dept")
    data = cursor.fetchone()
    print(data)
except Exception as e:
    print('exception:', e)
finally:
    con.close()
"""


"""
import cx_Oracle

try:
    # 데이터베이스에 연결합니다.
    dsnStr = cx_Oracle.makedsn("localhost", "1521", "xe")
    con = cx_Oracle.connect(user="system", password="wnddkd", dsn=dsnStr)

    cursor = con.cursor()

    cursor.execute("select * from dept")
    data = cursor.fetchall()
    for imsi in data:
        print(imsi)
except Exception as e:
    print('exception:', e)
finally:
    con.close()
"""


"""
import cx_Oracle

try:
    # 데이터베이스에 연결합니다.
    dsnStr = cx_Oracle.makedsn("localhost", "1521", "xe")
    con = cx_Oracle.connect(user="system", password="wnddkd", dsn=dsnStr)

    cursor = con.cursor()
    cursor.callproc('INSERT_DEPT', (95, '재무', '홍대'))
    con.commit()
    print('프로시저 수행 성공')

except Exception as e:
    print('exception:', e)
finally:
    con.close()
"""


"""
import cx_Oracle

try:
    # 데이터베이스에 연결합니다.
    dsnStr = cx_Oracle.makedsn("localhost", "1521", "xe")
    con = cx_Oracle.connect(user="system", password="wnddkd", dsn=dsnStr)

    cursor = con.cursor()

    # 자신의 이미지 파일 경로를 사용하세요
    # read file
    filename = 'data/image1.png'
    f = open(filename, 'rb')
    photo = f.read()
    f.close()

    sp = filename.split('/')
    query = 'insert into BLOBTABLE values(:1, :2, :3)'
    args = ('태연', sp[len(sp) - 1], photo)

    cursor.execute(query, args)
    con.commit()
    print('BLOB 삽입 성공')

except Exception as e:
    print('exception:', e)
finally:
    con.close()
"""


"""
import cx_Oracle
import sys
try:
    # 데이터베이스에 연결합니다.
    dsnStr = cx_Oracle.makedsn("localhost", "1521", "xe")
    con = cx_Oracle.connect(user="system", password="wnddkd", dsn=dsnStr)
    cursor = con.cursor()
    cursor.execute("select * from blobtable")
    data = cursor.fetchall()
    for imsi in data:
        print(imsi[0])
        print(imsi[1])
        f = open('./data/' + imsi[1], 'wb')
        blob = imsi[2]
        offset = 1
        while True:
            data = blob.read(offset, 65536)
            if data:
                f.write(data)
            if len(data) < 65536:
                break
            offset += len(data)
        f.close()
except:
    print('exception:', sys.exc_info())
finally:
    con.close()
"""


#Mongo DB

"""
from pymongo import MongoClient
#데이터베이스 연결
conn = MongoClient('127.0.0.1')

#데이터베이스 설정
db = conn.adam

#컬렉션 설정
collect = db.users

#document 생성 : {'key':'value'}
doc1 = {'empno':'10001', 'name':'kim', 'phone':'010-111-111', 'age':35}
doc2 = {'empno':'10002', 'name':'lee', 'age':45}
doc3 = {'empno':'10003', 'name':'park', 'phone':'010-222-222', 'age':25}

doc4 = {'empno':'10004', 'name':'choi', 'age':42}
doc5 = {'empno':'10005', 'name':'yun', 'phone':'010-222-222', 'age':37}

collect.insert_one(doc1)
collect.insert_one(doc2)
collect.insert_one(doc3)

collect.insert_many([doc4, doc5])

print(collect.count_documents({}))

collect.insert_many(
    [
        {'num': i} for i in range(10)
    ]
)
"""

"""
from pymongo import MongoClient
#데이터베이스 연결
conn = MongoClient('127.0.0.1')

#데이터베이스 설정
db = conn.adam

#컬렉션 설정
collect = db.users

# 전체 문서 조회
result = collect.find()

#print(result)
# 조회 문서 출력
for r in result :
    print(r)

# 조건 검색
print('조건 검색')
result2 = collect.find({ 'age':{'$gte':30} }) #크거나 같다
for r in result2 :
    print(r)
print()

result2 = collect.find({ 'age':{'$gte':30} }).sort("age")
for r in result2 :
    print(r)
"""

"""
from pymongo import MongoClient
#데이터베이스 연결
conn = MongoClient('127.0.0.1')

#데이터베이스 설정
db = conn.adam

#컬렉션 설정
collect = db.users

collect.update_one(
    { "empno" : "10001" },
    { "$set" :
        { "name" : "kkk" }
    }
)
collect.update_many(
    { 'age':{'$gte':30} },
    { "$set" :
        { "name" : "park" }
    }
)

result = collect.find()
# 조회 문서 출력
for r in result :
    print(r)
"""

"""
from pymongo import MongoClient
#데이터베이스 연결
conn = MongoClient('127.0.0.1')

#데이터베이스 설정
db = conn.adam

#컬렉션 설정
collect = db.users

collect.delete_many( {"age": { "$gte": 30 } } )

# 전체 문서 조회
result = collect.find()

# 조회 문서 출력
for r in result :
    print(r)
"""



#redis

"""
#데이터베이스 접속
import redis

# 호스트와 포트 설정, 데이터베이스 설정하여 connection 취득
with redis.StrictRedis(host='localhost', port=6379) as conn:
    print(conn)
"""

#데이터베이스 접속 및 데이터 저장
"""
import redis

# 호스트와 포트 설정, 데이터베이스 설정하여 connection 취득
with redis.StrictRedis(host='localhost', port=6379) as conn:
    # name 키로 adam 값을 입력
    conn.set('name', 'adam')
    # name 키로 데이터를 조회
    data = conn.get('name')
    # 콘솔 출력
    print(data)

# 호스트와 포트 설정, 데이터베이스 설정하여 pool를 설정
redis_pool = redis.ConnectionPool(host='localhost', port=6379, max_connections=4)
# pool로 connection을 취득
with redis.StrictRedis(connection_pool=redis_pool) as conn:
    # album 키로 list를 입력
    conn.set('album', '제네시스')
    # album 키로 데이터를 조회
    data = conn.get('album')
    # 콘솔 출력
    print(data)
    print(data.decode('utf-8'))
"""


"""
#데이터 만료 시간 설정
# redis 라이브러리 선언
import redis
import time
# 호스트와 포트 설정, 데이터베이스 설정하여 connection 취득
with redis.StrictRedis(host='localhost', port=6379) as conn:
    # name 키로 adam 값을 입력, 10초의 만료시간
    conn.set('name', 'adam', 10)
    # name 키의 만료시간을 출력
    print(conn.ttl('name'))
    # 만료시간 설정 100초
    conn.expire('name', 30)
    # test 키의 만료시간을 출력
    print(conn.ttl('name'))
    # test를 키로 데이터를 출력
    data = conn.get('name')
    # 콘솔 출력
    print(data)

    time.sleep(60)
    # test를 키로 데이터를 출력
    data = conn.get('name')
    # 콘솔 출력
    print(data)
    # 모든 키 지우기
    # conn.flushall()
"""


"""
#다른 자료형의 데이터 저장
import redis

with redis.StrictRedis(host='localhost', port=6379) as conn:
    # 리스트에서 오른쪽 입력
    conn.rpush("list", "1");
    # 리스트에서 왼쪽 입력
    conn.lpush("list", "2");
    # 리스트 데이터 출력 - 2, 1
    for i in conn.lrange('list', 0, 10):
        # 콘솔 출력
        print(i)
    # 콘솔 출력
    print('lpop list')
    # 리스트 왼쪽 pop - 2
    print(conn.lpop('list'))
    # 콘솔 출력
    print('list')
    # 리스트 데이터 출력 - 1
    for i in conn.lrange('list', 0, 10):
        # 콘솔 출력
        print(i)
    # 개행
    print()
    # Hash 형식의 key-value 값 입력
    conn.hset("map", "a", "1")
    conn.hset("map", "b", "2")
    conn.hset("map", "c", "3")
    # Hash 형식의 모든 데이터 출력
    print(conn.hgetall('map'))
    # Hash 형식의 a key의 데이터 출력
    print(conn.hget('map', 'a'))
    # 개행
    print()
    # Set 형식의 값 입력
    conn.sadd('set', 'C')
    conn.sadd('set', 'B')
    conn.sadd('set', 'A')
    # 중복은 입력 안된다.
    conn.sadd('set', 'A')
    conn.sadd('set', 'A')
    # Set 형식 출력
    print(conn.smembers('set'))
    # Set 형식의 값 입력 - 변수 명 set1
    conn.sadd('set1', 'A')
    conn.sadd('set1', 'D')
    # set과 set1의 교집합
    print(conn.sinter('set', 'set1'))
    # set과 set1의 합집합
    print(conn.sunion('set', 'set1'))
    # 개행
    print()
    # SortedSet 형식의 값 입력
    conn.zadd('sortedset', {'B': 1})
    conn.zadd('sortedset', {'A': 3})
    conn.zadd('sortedset', {'C': 0})
    # 10개의 데이터 출력
    print(conn.zrange('sortedset', 0, 9))
    # 10개의 데이터 출력 - 내림차순
    print(conn.zrange('sortedset', 0, 9, desc=True))
    # 2개의 데이터 출력 - 내림차순
    print(conn.zrange('sortedset', 0, 1, desc=True))
    # 모든 키 지우기
    # conn.flushall()
"""