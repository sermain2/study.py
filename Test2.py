# 문제 2: 관계연산자 & 논리연산자 연습
# 아래의 코드를 파이썬 파일에서 실행했을 때 결과르 적어 출력하세요.

print(1 <= 1) 
# 1은 1보다 작거나 같다 이므로 참이다.
print('Dog'<'dog')
# 아스키 코드에서 대문자보다 소문자가 더 큰 값을 가지므로 참이다. D = 68 d = 100
print('fun' in 'refunded')
# 'fun'은 "re'fun'ded"안에 포함 되어있으므로 참이다.
a = 2
b = 3
c = 'hello'
print((a+b)<(2*a))
# a+b = 5 < 2*(a) = 4  좌항이 우항보다 크기 때문에 거짓이다.
print((len(c)-b)==(a/2))
#(hello의 길이 == 5 - b = 2)  ==  (a/2 = 1) 이므로 좌항 우항의 값이 달라 거짓이다.

n = 4
answ = 'Y'
print((2<n)and(n<6))
# 2<n  = 참 and n<6 = 참 이므로 and 연산에 의해 참이다.
print((2<n)and(n==6)) 
# 2<n = 참 and n==6 = 거짓 이므로 and 연산에 의해 거짓이다.
print((answ=='Y')and(answ=='y'))
# answ == 'Y' = 참 and answ=='y' = 거짓 이므로 and 연산에 의해 거짓이다.
print(((n==2) and (n==7) or (answ=='Y')))
# n==2 = 거짓 and n==7 = 거짓 이므로 and 연산에 의해 참이고, 참 or answ=='Y' =참 이므로 or 연산에 의해 참이다.
print(((2<n) and (n<6) or (answ=='No')))
# 2<n = 참 and n<6 = 참 이므로 and 연산에 의해 참이고, 참 or (answ=='NO') = 거짓 이므로 or 연산에 의해 참이다.


# 실행 결과
True
True
True
False
False
True
False
False
True
True