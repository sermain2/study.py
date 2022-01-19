# 문제 8: 미성년자 판단

# 주민등록번호(13자리)를 입력 받고 성인인지 미성년자인지와 여자인지 남자인지를 판단하는 파이썬 프로그램을 작성하세요

# 만 19세 이상이면 성인  그렇지 않다면 미성년자 입니다.   

# Hint1: elif 문을 사용하세요
# Hint2: 주민등록번호 뒷자리에서 1,3의 경우 남자, 2,4의 경우 여자입니다.

# 1. 만 나이의 구분은 년(year) 과 월(month) 단위로만 계산합니다. 일(day) 단위는 고려하지 않습니다.
# (예:  현재 2021년 11월 기준으로 1982년 5월 생은 만 38년 6개월,
# 1997년 3월생은 만 24년 8개월, 2001년 12월생은 만 19년 11개월,  2009년 8월생 만 12년 3개월)
# 2. 1921년 이전 출생자에 대해서는 고려하지 않습니다. (즉, 1921년생과 2021년생은 구분하지 않습니다.)
# 3. 2000년대 이전 출생자의 경우 주민번호 뒷자리는 1,2 그리고 2000년대 이후 출생자의 경우 주민번호 뒷자리는 3,4 로 표기합니다.
# 4. 잘못 된 생일을 입력받았을 경우에 대해서는 별도의 처리를 고려하지 않습니다. (예: 911341-3451667  => 생일이 13월41일 처럼 잘못 입력된 경우는 고려하지 않습니다.)

num = input("주민등록번호를 입력하세요: ")

age_year = int(num[:2])
if(age_year > 22):
     age_year = 1900+age_year
elif(age_year <22):
     age_year = 2000+age_year

age_month = int(num[2:4])

sex = int(num[6])

now_year = 2021
now_month = 11

only_month = 0
only_year = 0

if(age_month < now_month) :
    only_month = now_month - age_month
    count = 0;

else:
    only_month = (now_month - age_month) + 12
    count = 1;

only_year = (now_year - age_year) - count;

if(sex == 1 or sex == 3):
     if(only_year >= 19):
          print("성인 남자입니다.")
     else:     
          print("미성년 남자입니다.")

elif(sex == 2 or sex == 4):
     if(only_year >= 19):
          print("성인 여성입니다.")
     else:     
          print("미성년 여성입니다.")
