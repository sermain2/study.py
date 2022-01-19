# 문제 6: 윤년 확인
# 연도를 입력 받아서 윤년인지 확인하는 프로그램을 작성하세요.
# 4의 배수이면 윤년, 100의 배수이면 평년, 400의 배수이면 윤년으로 취급합니다.

year = int(input("연도를 입력하세요: "))

if (year % 400 == 0):
    print("{}은 윤년입니다.".format(year))

elif (year % 100 == 0):
    print("{}은 평년입니다.".format(year))

elif (year % 4 == 0):
    print("{}은 윤년입니다.".format(year))