weater = "비" 

if weater =="비":
  print("우산을 챙기세요")
  
  
## = VS -==
# x = 5 //할당 ->  x에 5를 저장
# == 5 // 비교 -> x가 5와 같은가? 

##비교 연산자들 
age = 20 

# 같다
if age ==20:
  print("같음") 
# 다르다
if age != 25:
  print("나이가 25이 아닙니다.")
# 크다 
if age > 18: 
  print("성인")
# 작다 
if age < 30:
  print("30살 미만")
# 크거나 같다(이상) / age >=
# 작거나 같다(이하) / age <=

#if-else: 둘 중 하나 

if weater == "비": 
  print("우산을 챙기세요")

else:
  print("좋은 날씨네요.")

# if-elif-else: 여러 조건

score = 85

if score >= 90:
  print("A등급")
elif score >= 70:
  print("B")
elif score >= 60:
  print("D")
else: 
  print("F")  
  
  
# if 는 독립적 

#############

# 논리 연산자: 
# and : 둘 다 참이여야 함.
age = 25
height = 180

if age >= 18 and height >= 170:
  print("놀이기구 탑승 가능합니다.")
  
# or : 하나라도 참이면 참 
day = "토요일"

if day == "토요일" or day == "일요일":
  print("주말 입니다~")
  
# not  
is_raining = False
if not is_raining:
  print("비가 안오네요.")

#영화관 입료 계산기
print()
age = int(input("나이를 입력하세요:"))
print("age")

""""
규칙:
  13세 미만: 5,000원
  13세 이상 ~ 18세 미만: 8,000원
  18세 이상 ~ 85세 미만: 12,000원
  65세 이상: 7,000원 
"""

print()
if age < 13: 
   price = 5000
elif age <= 18: 
  price : 8000
elif age >65: 
  price : 12000

else : 
  price: 7000


price(f"입장료: {price}원 입니다.")


