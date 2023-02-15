# 실습문제 3
# 입력받은 숫자 a,b에 대하여 a부터 b까지 숫자의 합을 출력하세요
# 단 (a<=b 로 압력한다고 가정)

first = int(input("처음 숫자를 입력하세요: "))
last = int(input("마지막 숫자를 입력하세요: "))
s = 0

for i in range(first, last+1):
    s += i
print(s)
