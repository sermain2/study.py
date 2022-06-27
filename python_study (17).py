one = int(input("정수를 입력하세요: "))
two = int(input("정수를 입력하세요: "))
three = int(input("정수를 입력하세요: "))

one = int(one)
two = int(two)
three = int(three)

if (one > two):
    if (one > three):
        max = one
    else:
        max = three
else:
    if (two > three):
        max = two
    else:
        max = three

print('가장 큰 정수는 ', max,'입니다')