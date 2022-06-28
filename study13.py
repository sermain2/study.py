class Animal:
    name = '고양이'
    def sound(sel):
        print('냐아옹~~~')

cat = Animal()

print(cat.name)
cat.sound()

class Student:
    name = '황제호'
    kor = 80
    eng = 90
    math = 100
    def getSum(self):
        sum = self.kor + self.eng + self.math
        return sum
    
hwang = Student()
print('이름: %s' % hwang.name)
print('국어: %d' % hwang.kor)
print('수학: %d' % hwang.math)
print('영어: %d' % hwang.eng)
print("합계: %d" % hwang.getSum())
print('평균: %.1f' %  (hwang.getSum()/3))
