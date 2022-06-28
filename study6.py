sum = 0

for i in range(1,11):
    sum = sum + i
    print("i의 값: %2d => 합계: %d" % (i, sum))
    
    
for i in range(10):
    print(i, end ="")
print()

for i in range(1, 11):
    print(i, end = '')
print('\n')

for i in range(1, 10, 2):
    print(i, end='')
print()
#()
for i in range(20, 0, -2):
   print(i, end = '') 



for i in range(100, 301, 5):
    sum = sum + i

print('100~300의 정수 중에서 5의 배수의 합계: %d' % sum)

print('-'*50)

for a in range(2,10):
    for b in range(1, 10):
        c = a*b
        print("%d x %d = %d" % (a,b,c))