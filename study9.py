# 튜플: 리스트의 형태와 사용벙이 유사함
# 튜플이 리스트와 다른 점은 
# 튜플렝서는 리시트의 대괄호 대신에 소괄호 사용
# 튜플에서는 리스트와는 달리 요소들의 수정과 추가가 불가
menu = ('짜장면', '우동', '짬뽕', '볶음밥')
print(menu)
print(menu[0])
print(menu[2])
print(menu[0:3])

tup1 = (10, 20, 30)
tup2 = (40, 50, 60)
tup3 = tup1 - tup2
print(tup3)
print(len(tup3))

# 파이썬을 파이썬스럽게 사용하고, 파이썬을 잘한다! 할려면 딕셔너리를 잘 사용해야함.
# 어떻게 메모리를 적게 쓰면서 효율성 있게 연산할 수 있을까.. 키와 값
members ={'name':'황예린', 'age':22, 'email':'zzz@coding.info'}
print(members)
print(members['name'])
print(members['age'])

