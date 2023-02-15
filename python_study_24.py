# 실습문제1 
# 5명의 이름을 입력 받아 리스트에 저장하고 차례대로 출력하세요

user = [] 

for i in range(0,5):
    a= input("%d번째 이름을 입력하세요: " %(i+1))
    user.append(a)
print(user)
