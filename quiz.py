import random
serial_num = 0
user_num = 0

# 여기에 코드를 작성하세요
random_num = random.randint(1,20)
print(random_num)

for serial_num in range(0,4):
  user_num = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: " .format(4-(int(serial_num)))))

  if random_num > user_num:
    print("Up")
  elif random_num < user_num:
    print("Down")
    
if random_num == user_num:
  print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(4-serial_num))
else:
  print("아쉽습니다. 정답은 {}입니다.".format(random_num))