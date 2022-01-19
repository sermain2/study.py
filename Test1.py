# 문제 1: print()연습
# 아래의 코드를 파이썬 파일에서 실행했을 때 결과를 적어 제출하세요.

print('Python')
# 문자열 'Python'을 출력한다  


print('Python'[-1], 'Python'[4], 'Python'[1:3])
# 문자열 인덱싱에 의해 Python[-1] -> n  Python[4] -> o  Python[1:3] -> yt


print(10+20)
# 정수 10과 정수 20의 합을 출력한다 -> 30.


print('10'+'20')
# 문자열 '10'과 '20'을 합으로 출력한다 -> 1020


print('10+20'*2)
# 문자열 '10+20'을 2번 곱하여 출력한다 -> 10+2010+20 


print('Hello', end='')
print('World!')
# 문자열 'Hello'를 출력한 뒤 그 다음 문장으로 World!를 end를 통해 연달아 출력한다 -> HelloWorld!


print('Hello\n', end='')
print('World!')
# end를 사용한 뒤 \n 줄바꿈을 사용하였기 때문에 Hello
#                                            World! 가 되었다.

print('Hello\n')
print('World!')
# 문자열 Hello을 출력하고 줄바꿈 \n을하여 한 줄을 띈다. 그 다음에 문자열 World!를 출력한다.

# 실행 결과
# Python
# n o yt
# 30    
# 1020  
# 10+2010+20
# HelloWorld!
# Hello
# World!
# Hello

# World!