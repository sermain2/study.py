# 실습 예제4: 소문자만 출력하기
# 다음과 같은 예제 코드가 주어졌다.
# example = "abcdefghijklmnopqrSTUVWXYZ"
# 문자열 슬라이싱과 문자열 연산을 이용하여 다음의 출력결과와 같이
# 알파벳들을 모두 소문자로 출력하시오

# 출력결과: lower case alphabets are abcdefghijklmnopqrstuwxyz

al = "abcdefghijklmnopqrSTUVWXYZ"

print("lowercase alphabets are " + al[:18:] + al[19::].lower())