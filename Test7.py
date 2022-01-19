# 문제 7: 오전/오후 출력
# 현재 시간이 오전인지 오후인지 판단하는 파이썬 프로그램을 작성하세요.
# (입력은 4자리 양의 정수만 허용합니다.)

time = input("시간을 입력해주세요(00시00분): ")

a = int(time[0:2])
b = int(time[2:5])


if (0 <= a < 12 and 0 <= b < 60):
    print("{0}시 {1}분은 오전 입니다.".format(a,b))
elif(12 <= a < 24 and 0 <= b < 60):
    print("{0}시 {1}분은 오후 입니다.".format(a,b))
else:
    print("잘못 입력하였습니다.")


# str = "hello"
# print(str[:2])
# print(str[2:5])