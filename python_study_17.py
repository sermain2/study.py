group = input("단체 모임을 자주 합니까?: ")
washhand = input("손을 자주 씻나요?: ")
mask  = input("마스크를 끼고 다니시나요: ")
risk = 0

if washhand == "네":
    if group == "네":
        risk = 30
    else:
        if mask == "네":
            risk = 0
        else:
            risk = 20
else:
    risk = 40

print("당신의 감영 확률은 {}% 입니다." .format(risk)
