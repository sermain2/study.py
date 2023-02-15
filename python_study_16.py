year = int(input("현재년을 입력해주세요: "))
month = int(input("현재월을 입력해주세요: "))
day = int(input("현재일을 입력해주세요: "))
b_y = int(input("출생년을 입력해주세요: "))
b_m = int(input("출생월을 입력해주세요: "))
b_d = int(input("출생일을 입력해주세요: "))

if(b_m < month):
    age = year - b_y
elif(b_m == month):
    if(b_d <= day):
        age = year - b_y
    else:
        age = year - b_y - 1
else:
    age = year - b_y - 1

print("오늘 날짜: {}년 {}월 {}일".format(year, month, day))
print("생년 월일: {}년 {}월 {}일".format(b_y, b_m, b_d))

print("만나이 : %d" %age)

if (age >= 19):
    print("성인입니다.")
