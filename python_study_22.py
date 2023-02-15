# 실습 문제4
# 펠린드롬이라는 것은 앞뒤가 같은 문자열을 의미하고, 펠린드롬수 라는 것은
# 앞뒤가 같은 숫자라고 정의합니다.
# 숫자를 입력받고 이것이 펠림드롬수인지 확인하는 프로그램을 작성하시오
# ★★★★★

num = int(input())
tmp = num
lspalindrome = 0
while tmp != 0:
    lspalindrome *= 10
    lspalindrome += tmp % 10
    tmp = tmp // 10
    if num == lspalindrome:
            print('True')
    else:
            print("False")
