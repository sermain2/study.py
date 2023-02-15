# 실습 문제5
# 피보나치수는 다음과 같은 점화식으로 나타내지는 수열이다
# 피보나치 수열은 1,1,2,3,5,8,13...과 같이 현재 수는 이전 두 수의 앞으로
# 표현 할 수 있다.
# 이때 숫자 n을 입력하여 n번째 피보나치 수를 구하는 프로그램을 작성하세요
# (n은 1이상인 자연수)



# string = input("두 정수를 입력하세요: ")
# a, b = string.split()
# a, b = int(a), int(b)

# while a < 10:
#     print(a)
#     a, b = b, a+b
    
    
    
n = int(input())
i = 2
before = 1
now = 1
while i < n:
    tmp = before + now
    before = now
    now = tmp
    i += 1
    
if(n<=2):
    print(i)
else:
    print(now)
