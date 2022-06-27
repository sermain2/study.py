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
        print("{}은 3의 배수이면서 21의 배수가 아닙니다.".format(num))
else:
    print("{}은 3의 배수가 아닌 수 입니다.".format(num))
                

# result 와 print로 한 번에 출력하기.