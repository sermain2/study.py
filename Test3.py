# 문제 3: 리스트 함수 사용
# 5개의 정수를 입력 받아 리스트를 만든 후 출력하고 리스트 함수를 이용하여 그 중에서 가장 큰 수와 가장 작은 수,
# 리스트의 평균을 출력하는 프로그램을 작성하세요

num_list = []

num_list.append(int(input("정수를 입력하세요: ")))
num_list.append(int(input("정수를 입력하세요: ")))
num_list.append(int(input("정수를 입력하세요: ")))
num_list.append(int(input("정수를 입력하세요: ")))
num_list.append(int(input("정수를 입력하세요: ")))

result = (sum(num_list))

avg = float(result/len(num_list))

print("Maxnum:{0}  Minimum:{1}  Average:{2}" .format(max(num_list), min(num_list), avg))