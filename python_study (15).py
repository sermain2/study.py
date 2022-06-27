

 
# J = int(input("J를 입력하세요: "))
# K = int(input("K를 입력하세요: "))

# if(J > K):
#     print("J가 k보다 큽니다.")

# elif(K > J):
#     print("K가 J보다 큽니다.")

# elif(K == J):
#     print("K와 J가 같습니다.")

# num = int(input("정수를 입력하세요: "))

# if (num >= 0):
#     if(num == 0):
#         print("0 입니다.")
#     else:
#         print("양수입니다.")
# else:
#     print("음수입니다.")           


# num = int(input("숫자를 입력해주세요: "))

# if (num % 2 == 0):
#     if (num % 3 == 0):
#         print("짝수이면서 3의 배수입니다.")
#     else:
#         print("짝수인데 3의 배수는 아닙니다.")
# else:
#     if(num % 3 == 0):
#         print("홀수이면서 3의 배수입니다.")
#     else:
#         print("홀수이고 3의 배수가 아닙니다.")

num = int(input("숫자를 입력해주세요: "))

if(num % 3 == 0):
    print("{}은 3의 배수입니다." .format(num))
    if (num % 5 == 0):
        print("3의 배수이면서 15의 배수입니다." .format(num))
    else:
         print("{}은 3의 배수인데 15의 배수는 아닙니다." .format(num))

    if(num % 7 == 0):
        print("{}은 3의 배수이면서 21의 배수입니다.".format(num))
    else:
        print("{}은 3의 배수인데 21의 배수가 아닙니다.".format(num))
else:
    print("{}은 3의 배수가 아닌 수 입니다.".format(num))