# 실습 문제3
# 두 정수를 입력 받고, 그 최대공약수를 출력하는 프로그램을 작성하세요
# 두 수는 공백으로 구분하며, 다른 자료형이 입력되는 경우는 생략하니 않습니다.
# split() 함수 사용 -> input().split()



string = input("두 정수를 입력하세요: ")
a, b = string.split()
a, b = int(a), int(b)

i = 1
gcd = 1 

while i <= min(a,b):
    if(a % i == 0 and b % i == 0):
        gcd = i
    i += 1
print("최대공약수: ", gcd)