# 실습예제3: 50보다 작은 소수찾기
# 50 이하의 숫자n을 입력 받고, n보다 작은 모든 소수를 찾으세요
# 소수는 2부터 시작합니다 범의를 주의할것


n = int(input("50 이하의 숫자를 입력하세요: "))
for i in range(2, n+1):
    is_prime = True
    for j in range (2,i):
        if i % j == 0:
            is_prime = False
    if is_prime == True:
        print(i)        