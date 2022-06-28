scores = [[75, 83, 90], [86, 86, 86], [75, 95, 95], [89,77, 83], [100, 98, 100]]

for i in range(len(scores)):
    sum = 0
    for j in range(len(scores[i])):
        sum = sum + scores[i][j]
        
    avg  = sum/len(scores[i])
    print("%d번째 학생의 합계:%d, 평균:%.2f" % (i+1, sum, avg))
    

strings = [['잠자리', '풍뎅이', ['여치']], ['짜장면', '파스타', '피자']]
for i in range(len(strings)):
    for j in range(strings[i]):
        print(strings[i][j])
    print()
        