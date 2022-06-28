from unittest import result


def computeMaxGong(x,y):
    if x > y:
        small = y
    else:
        small = x
        
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            result = i
    return result

num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))

max_gong = computeMaxGong(num1, num2)

print("%d와 %d의 최대공약수: %d" % (num1, num2, max_gong))

def matchWord(in_word, answer):
    if in_word == answer:
        msg = "참 잘했어요."
    else:
        msg = "단어 공부 좀 하세요~"
    return msg

eng_dict = {'apple':'사과', 'lion':'사자', 'love':'사랑', 'friend':'친구'}
for i in eng_dict:
    string = input(eng_dict[i] + '에 맞는 영어 단어는?')
    result = matchWord(string, i)
    print(result)
