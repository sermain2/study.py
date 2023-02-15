# 실습 문제 1
# 100부터 입력 받은 수 만큼 빼서 0 이하로 만드는 프로그램을 만드세요.
# 이때, 모든 단계 별로 얼마나 남았는지 출력하고, 0 이하가 되면 프로그램을 종료하세요


    
num = 100
while True:
    tmp = int(input())
    num -= tmp
    if num <= 0:
        break
    print("{}은 0보다 큰 숫자입니다.".format(num))
