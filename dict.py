# 새 파일: dict.py

name = "Kim"
age = 20
email = "kim@example.com"

# 리스트 

User = ["Kim", 20, "kim@example.com"]
#         ^0번째 , 1번째,  2번째 

#Dictionary = Key(이름표) 와 Value(값)
# 단어(key) : apple / 뜻(Value) : 사과 


user = {
    "name": "Kim",
    "age" : 20,
    "eamil" : "kim@example.com"
}


user2 = dict(name="Lee", age=25, email="asdf@asdf.com")

empty_dict = {}


#값 가져오기.
print(user["name"])
print(user["age"])

print()
print(user.get("name"))
print(user.get("phone")) #없음

# print(user["phone"])  #KeyError 발생
print(user.get("phone","없음"))

#모든 키 출력
print()
print(user.keys()) 

#모든 값 출력
print()
print(user.values())

#모든 키-값 출력
print()
print(user.items())


###########################################################
# 값 추가/수정 
print()
user["city"] = "seoul"
print(user)

# 값 수정 
print()
user["age"] = 99
print(user)

#값 삭제
print()
del user["city"]
print(user)

# 값 꺼내기(삭제+리턴)
print()
age = user.pop("age")
print(age)
print(user)

# 전체 삭제
print()
user.clear()
print(user)

#중첩 딕셔너리(딕셔너리 안의 딕셔너리)

users = {
    "user1": {
        "name": "Kim",
        "age": 20 
    },
    "user2": {
       "name" : "Lee"
       "age" : = 22
             
        
    }
    
}

print()
print(users["user1"]["name"])
print(users["user2"]["age"])

###############################
print()
user = {}

# 2. 정보 추가 
user["name"] = "Kim"
user["age"] = "22"
user["city"] = "seoul"

print(user)
print("이름:" + user["name"])
#print("나이"): + user["age"] + "세")  # 오류 
print("나이:" + str(user["age"]) + "세")
#문자열끼리 붙이는건 허용, 문자열과 숫자를 직접적으로 이어 붙이는건 허용하지 않음 


#f-staring
print()
print(f"이름: {user['name`']}")
print(f"나이: {user['age']}세")


##########딕셔너리 만들기
book = {
    "title": "점프 투파이썬",
    "price": 10000,
    "pages": 100
    }


#print()
#print(f"제목: {book}") #ㅠㅠ
      
      
      
#집합(set) = 중복 없는 데이터 모음 

fruits = {"사과","바나나","포도"}
numbers = {1,2,2,3,3,3}

empty_set = set()  #빈 집합 만들기 
 
 
print(numbers)  #중복 제거 
print(fruits)   #순서 없음 
#print(fruits[0])

print( 3 in numbers)

#중복된 값값이  잉잉ㅆㅆ는 리리스스트트
numbers = [1,2,3,3,4,4,5,5,5,5,6,7,6,7,6]

#집합으로 변환 -> 중복 제거 

unique_numbers = list(set(numbers))
print(unique_numbers)

