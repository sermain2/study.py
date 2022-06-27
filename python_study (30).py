# 실습문제 5
# 숫자 n을 입력받아, 첫째 줄에는 별 한 개, 둘째 줄에는 별 두 개
# N번째 줄에는 별N개를 오른쪽을 기준으로 정렬해서 찍는 
# 작업을 반복하세요
# print(' ', end=' ')

a = int(input("숫자 입력: "))

for i in range(1, a+1):
    for j in range(a-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()