# 문제4: 공약수 판단
# 양의 정수인 두 수를 입력 받고 공약수에 3이 있는지 없는지를 판단하는 파이썬 프로그램을 작성하세요

num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))


if (num1 % 3 == 0 and num2 % 3 == 0):
    print("3 in the commin divisor")   
else:
    print("No 3 in the common divisor")