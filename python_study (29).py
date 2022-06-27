# 실습문제4
# 4월달 달력을 다음과 같이 출력하세요 ★

print("            ", end=' ')

for i in range(1 , 31):
    if i % 7 == 4:
        print("\n")
        
    print("%d" %i, end=' ')
    
    if i<10:
        print("", end=' ')