import re


def hello():
    print("안녕하세요!.")

hello()

def say_hello(name):
    print("%s님 안녕하세요!: " % name)

say_hello('김세민')
say_hello('최태준')
say_hello('이승빈')

def even_odd(n):
    if n % 2 == 0:
        print("%d -> 짝수" % n)
    else:
        print("%d -> 홀수" % n)
        
even_odd(15)
even_odd(26)

def inch_to_cm(inch):
    cm = inch * 2.54
    return cm
num = int(input('인치를 입력하세요: '))
result  = inch_to_cm(num)
print("%d inch => %.2fcm" % (num, result))



def besu5(n):
    if n % 5 == 0:
        rel = True
    else:
        rel = False
    
    return rel

num = (input('양의 정수를 입력하세요: '))
result  = besu5(num)

if result == True:
    print("%d -> 5의 배수이다." % num)
else:
    print("%d -> 5의 배수가 아니다." % num)
    

