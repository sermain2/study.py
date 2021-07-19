from typing import Tuple


print("Hello world")

# 다양한 연산
print(1)
print(-2)
print(3.14)

print(1+2)
print(1-2)
print(1*2)
print(1/2)

print(2**2)
print(2//2)
print(2%2)

# 문자열

print("안녕하세요")

a = "안녕하세요"
b = "반갑습니다"

print(a+b)

print(a*3)

#변수
#변수_이름 = 저장할_값
#변수 이름 설정 문자와 숫자 , _ 사용가능
#대문자와 소문자를 구분하여 사용할 것
#공백은 사용할 수 없음
#숫자로 시작할 수 없음
#미리 예약된 이름은 사용불가

rainbow = '빨주노초파남보'
print(rainbow)

count = 0
print(count)

count = 1
print(count)

count = count + 1
print(count)

#일일 바리스타

coffee = 4100
juice = 4600
tea = 3900

print(coffee * 3 + juice * 2 + tea * 1)

print(coffee * 4 + juice * 3 + tea * 3)

print(coffee * 1 + juice * 1 + tea * 2)


#리스트
#변수 하나하나 귀찮스 = 리스트로 보완

candy0 = '딸기맛'
candy1 = '레몬맛'
candy2 = '수박맛'
candy3 = '박하맛'
candy4 = '우유맛'
print(candy0, candy1, candy2, candy3, candy4)

candies = ['딸기맛', '레몬맛', '수박맛', '박하맛', '우유맛']
print(candies)

my_list1 = []
print(my_list1)

my_list2 = [1, -2, 3.14]
print(my_list2)

mylist3 = ['앨리스', 10, [1.0, 1.2]]
print(mylist3)

#리스트에 값 추가하기
#리스트.append

clovers =[]
clovers.append('클로버1')
print(clovers)

clovers.append('하트2')
print(clovers)

clovers.append('클로버3')
print(clovers)

#리스트 값에 접근하기

print(clovers[1])
print(clovers[2])

#리스트 값 제거하기

del clovers[1]
print(clovers)

candies = ['딸기맛', '레몬맛', '수박맛', '박하맛', '우유맛']
print(candies)

candies.append('콜라맛')
candies.append('포도맛')
print(candies)

del candies[3]
print(candies)

#리스트 [시작:끝:인덱스] 
#2<x<5 느낌

week = ['월', '화', '수', '목', '금', '토', '일']
print(week)
print(week[2:5])

cat_candy = candies[0]
print('체서 고양이에게는',cat_candy,'사탕을 줘요')

duck_candy = candies[1]
print('오리에게는',duck_candy,'사탕을 줘요') 

dodo_candies = candies[3:6]
print('도도새에게는',dodo_candies,'사탕을 줘요')

#리스트를 정렬하기
#리스트.sort()

animals = ['고양이','오리','도도새']
animals.sort()
print(animals)

#리스트에서 특정 값의 개수를 세는 코드
#리스트.count

cards = ['하트', '클로버', '다이아', '스페이드', '클로버']
print(cards.count('하트'))
print(cards.count('클로버'))

#idle 에디터
# for 변수 in 리스트:
    #실행할 명령
#range(끝_값+1)

for num in [0,1,2]:
    print(num)

characters = ['앨리스', '도도새', '3월토끼']
for characters in characters:
    print(characters)

players = ['공작부인', '흰 토끼', '하트잭', '모자장수']
for player in players:
    print(player,'퇴장!')

for num in range(3):
    print(num)

for y in range(1, 10):
    print(2,'x',y, '=' , 2 * y)

roses = ['하얀장미','하얀장미','하얀장미']
for i in range(3):
    roses[i] = '빨간장미'
print(roses)

#참과 거짓

print(True)
print(False)

print(1<2)
print(2<1)

print(1 <= 1)
print(2 <= 1)

print(1 == 1)
print(2 == 1)

print(1 != 2)
print(2 != 2)

#if 조건:
#   실행할_명령

if True:
    print('참입니다')

score = 90
if score > 80:
    print('합격입니다.')
else:
    print('불합격 입니다')

score = 60
if score > 80:
    print('합격입니다')
else:
    print('불합격입니다')

score = 75
if 80 < score <=100:
    print('학점은 A입니다')
elif 60 < score <= 80:
    print('학점은 B입니다')
elif 40 < score <= 60:
    print('학점은 C입니다')
else:
    print("학점은 F입니다")

total_price = 0
ages = [22, 21, 17, 32, 4, 28, 19, 8]
for age in ages:
    if age >= 20:
        total_price = total_price + 8000
    elif age >= 10:
        total_price = total_price + 5000
    else:
        total_price = total_price + 2500
print('총 입장료는',total_price,'원입니다')

games = 12
points = 25
if games >= 10 and points >= 20:
    print('MVP로 선정되었습니다')

#while 조건문

num = 0
while num < 3:
    print('안녕', num)
    num = num + 1

count = 0
while count < 5:
    count = count + 1
    print(count,'번째 바퀴입니다')
print('경주 끝!')

#입력을 받는 법 input()

name = input('이름이 뭔가요?')
print(name, '안녕!')

answer = ''
while answer != '런던':
    answer = input('영국의 수도는 어디인가요?')
print('정답입니다')

#while 과 함께 사용하는 key word continue break

count = 0
while count < 3:
    count = count + 1
    if count == 2:
        continue
    print(count)

count = 0
while count < 3:
    count = count + 1
    if count == 2:
        break
    print(count)

while True:
    answer = input('런던, 파리, 서울 중 영국의 수도는 어디인가요?')
    if answer == '런던':
        print('정답입니다!')
        break

    elif answer == '파리':
        print('틀렸습니다!')
    elif answer == '서울':
        print('틀렸습니다!')
    else:
        print('보기에서 골라주세요')

# 튜플
my_tuplel1 = ()
print(my_tuplel1)

my_tuplel2 = (1, -2, 3.14)
print(my_tuplel2)

my_tuplel3 = '앨리스', 10, 1.0, 1.2
print(my_tuplel3)

#값이 한 개인 튜플을 만드는 코드
my_int = (1)
print(type(my_int))

my_tuple = (1,)
print(type(my_tuple))

#패킹과 언패킹 여러 값을 하나의 변수에 넣음 패킹, 여러 값을 여러 변수에 풀어주는것 언패킹
clovers = '클로버1' , '클로버2', '클로버3'
print(clovers)

alice_blue = (240, 248, 255) # 튜플 rgb에 한꺼번에 저장함
r, g, b = alice_blue
print('R:',r ,'G', g, 'B', b)

#두 개의 값을 바꾸는게 파이썬에서는 다른 언어보다 편하다
dodo = '박하맛'
alice = '딸기맛'
print('도도새:', dodo, '앨리스:', alice)
dodo, alice = alice, dodo
print('도도새:', dodo, '앨리스:', alice)

#딕셔너리 단어 = key 뜻 = value
my_dict1 = {}
print(my_dict1)

my_dict2 = {0:1, 1:-2, 2:3.14}
print(my_dict2)

my_dict3 = {'이름':'앨리스','나이':10, '시력': [1.0, 1.2]}
print(my_dict3)

#list는 append가 있지만 딕셔너리에는 없음 따라서
#딕셔너리[추가할_키] = 추가할_값 이러한 방식으로 저장해야함

clover = {'나이': 27, '직업': '병사'}
print(clover)
clover['번호'] = 9
print(clover)

#딕셔니리에 있는 값에 접근하기
#딕셔너리[접근할_키]

clover = {'나이':27, '직업':'병사', '번호': 9}
print(clover['번호'])

clover['번호'] = 6
print(clover['번호'])

print(clover.get('번호'))

#키-값 제거하기
#del 딕셔너리[제거할_키]
clover = {'나이':27, '직업': '병사', '번호':6}
print(clover)

del clover['나이']
print(clover)

order = {'스페이드1': '비빔라면', '다이아2': '매운라면'}
print(order)

order['클로버3'] = '카레라면'
print(order)

order['다이아2'] = '짜장라면'
print(order)

del order['스페이드1']
print(order)


#함수의 종류
#내장함수 , 모듈의 함수, 사용자 정의 함수

# def 함수_이름(인수):
#    실행할_ 명령
#    return 반환값

def my_func():
    print('토끼야 안녕!')

my_func()

def add(num1, num2):
    return num1 + num2

print(add(2,3))

def add_mul(num1, num2):
    return num1 + num2, num1 * num2

print(add_mul(2,3))

def judge_cards(name):
    print(name, '1 유죄!')
    print(name, '2 유죄!')
    print(name, '3 유죄!')

judge_cards('하트')
judge_cards('클로버')
judge_cards('스페이드')

#랜덤하게 뽑기
#random.choice(리스트)
#random.sample(리스트, 뽑을 개수)
#random.randint(시작 값, 끝 값)

import random
animals = ['고양이', '오리', '도도새']
print(random.choice(animals))

import random
animals = ['고양이', '오리', '도도새']
print(random.sample(animals, 2))

import random
print(random.randint(5, 10))
