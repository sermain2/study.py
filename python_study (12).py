# 실습 문제3: 사분면 구하기
# 주어진 xy 좌표가 속하는 사분면 (1,2,3,4 중 하나) 번호를 출력하세요.
# 단, x좌표와 y좌표는 모두 양수나 음수라고 가정합니다.

x = int(input("x 좌표를 입력하세요: "))
y = int(input("y 좌표를 입력하세요: "))

if (x > 0) and (y > 0):
    print("1 사분면입니다.")
elif (x < 0) and (y > 0):
    print("2 사분면입니다")
elif (x < 0) and (y < 0):
    print("3 사분면입니다.")
else:
    print("4 사분면입니다.")
