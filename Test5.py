# 문제 5: 부모님의 나이 차이
# 부모님 성함과 연세를 입력 받아 연상/연하 및 나이 차에 따라 각각 아래의 결과값을 출력하는
# 프로그램을 작성하세요.

mom_name = input("Mother's name?: ")
mom_age = int(input("Mother's age?: "))

far_name = input("Father's name?: ")
far_age = int(input("Father's age?: "))

gap1 = (mom_age - far_age)
gap2 = (far_age - mom_age)

if (mom_age == far_age):
    print("{} and {} are the same age".format(mom_name, far_name))

elif(mom_age > far_age):
    print("Older: {}".format(mom_name))
    print("Younger: {}".format(far_name))
    print("Age gap: {}".format(gap1))

else:
    print("Older: {}".format(far_name))
    print("Younger: {}".format(mom_name))
    print("Age gap: {}".format(gap2))
