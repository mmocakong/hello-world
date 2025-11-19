student1 = "일철수"
student2 = "이철수"
student3 = "삼철수"

#리스트(목록) : 여러 개의 값을 하나로 묶은 것 

# 학생 이름 목록 
students = ["일철수","이철수","삼철수"]

#숫자 목록 
scores = [11,22,33,]
scores1 = ["문자열",22, 33,44 ]   #관리하기 어려워 별로 추천하지않음.... 
print(scores1)


print("= = = = = = = =")
fruits = ["사과","바나나","메론"] 

fruits.append("귤")
print("fruits")

print("= = = Len = = = =")

print(len(fruits))

#첫 번째 과일 (0번째)
print(fruits[0]) #사과
print(fruits[1]) #바나나
print(fruits[2]) # 메론 
print(fruits[-1]) # 마지막 과일(귤)
print(fruits[-2]) # 마지막 과일(귤)


#사과만 필요할 경우 어떻게 꺼낼 수 있을까? 
print(fruits) 

#리스트 길이(몇 개 들어있어?)
#print(len(fruits))
    1. print()
    2. len()
    2.1 len(fruits)
    2.2 print()  -> print(len(fruits))


print("= = = 슬라이싱 = = = =")
# 슬라이싱: 여러개 잘라내기 
# [시작:끝] -> 시작 위치부터(끝-1) 위치까지
#           ['사과','바나나','메론','귤']

print(fruits[1:3]) 
print(fruits[0:3])  # 사과 부터 멜론까지 출력이 되었다! 


print("= = = 리스트 수정 = = =")
print = ["사과","바나나"."포도"]
print(fruits)

# 값 변경 
fruits[1] = "딸기"
print(fruits)

# 값 추가(끝에)
print()
fruits.append("키위")
print(fruits)

# 값 추가(중간에)
print()
fruits.insert(1, "망고")
print(fruits)


# 값 삭제 
print()         #현재 : [사과,망고,딸기,포드,키위]
del fruits[2]
print(fruits)  #결과 : [사과,망고,포도,키위]

#마지막 값 꺼내서(삭제 +리턴(사용하기))
print()         # 현재 : ['사과'.'망고'.'포도','키위']
last = fruits.pop()
print(last)     #키위
print(fruits)   #결과 : ['사과','망고','포도']





#2차원 리스트 

scores = [ 
          [90, 80 , 70], # 학생1
          [55, 50, 10],  # 학생2
          [12, 32, 44]   # 학생3
          ]

#학생 1의 모든 정수 
print(scores[0]) # [90,80, 70] ,

#학생 1의 첫번째 과목 점수 
print(scores[0][0]) # 90

# 학생 2 두번째 과목 점수 
print(scores[1][1])


