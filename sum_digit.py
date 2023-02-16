# 리스트 정렬
# 리스트의 요소를 정렬하고 싶은 경우 -> sort()함수를 사용!

a = [12, 2, 33, 4]
a.sort() # 오름차순 정렬
print(a)

b = [22, 34, 49, 51]
b.sort(reverse=True) # 내림차순 정렬
print(b)

# sort()와 sorted()의 차이점
c = [19,34,15,27]
d = sorted(c)
print(c)
print(d)
# sort() 리스트 정렬 후 반환 x
# sorted() 정렬한 리스트를 반환
