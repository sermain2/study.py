
# for i in range(5): # 5번 반복 바깥 쪽 루프는 세로 방향
#         for j in range(5): # 5번 반복 안쪽 루프는 가로 방향
#                 print('j:', j, sep=' ', end = ' ') # j값 출력 end에 ' '를 지정하여 줄바꿈 대신 한칸 띄움 
#         print('i:', i, "\\n", sep='') # i 값 출력, 개행 문자 모양도 출력
#                                       # 가로 방향으로 숫자를 모두 출력한 뒤 다음 줄로 넘어감
#                                       # print 기본적으로 출력 후 다음 줄로 넘어감 
                                      
# for i in range(5):
#         for j in range(5):
#                 print("*", sep = " ", end = " ")
#         print()
        
# for i in range(3):
#         for j in range(7):
#                 print("*", sep = " ", end = " ")
#         print()
        
# 계단식
# for i in range(5): # 0 부터 4까지 5번 반복. 세로 방향
#         for j in range(5): # 0부터 4까지 5번 반복. 가로 방향
#                 if j <= i: # 세로 방향 변수 i 만큼
#                         print("*", end = ' ') # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
#         print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감 

# 대각선
# for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
#     for j in range(5):    # 0부터 4까지 5번 반복. 가로 방향
#         if j == i:                # 세로 방향 변수와 같을 때
#             print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
#         else:                     # 세로 방향 변수와 다를 때
#             print(' ', end='')    # 공백 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
#     print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
#                # (print는 출력 후 기본적으로 다음 줄로 넘어감)

# for i in range(5):
#         for j in range(5):
#                 if i > j:
#                         print(" ", end = '')
#                 else:
#                         print("*", end = '')
                        
#         print()