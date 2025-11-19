# 새 파일 : for.py

fruits = ["사과","바나나","포도"]
index = 0 

while index < len(fruits):
    print(fruits[index])
    index += 1 
    
    
# for문 사용
print()   # 리스트에 있는 요소를 여기에 담아라!
for fruit in fruits:
    print(fruit)
    
# range(): 숫자 범위 만들기 
print()
for i in range(5):      #0부터 -1까지  
    print(i)


print("----")
for i in range(1,6):   #시작부터 끝 -1 까지 
    print(i)
    
print("----")
for i in range(0, 10, 2):     #시작, 끝, 증가값: 증가값 만큼 건너뛰기
    print(i)
    
    
#딕셔너리 
user = {"name":"kim","age":30}
for key, value in user.items():
    print(f"{key}:{value}")
    

for key in user:
    print(key)
    
print("-- 값만 필요함--")
for value in user.values():
    print(value)
    

# 구구단 만들기 
dan =int(input("몇 단을 출력할까요?[9단까지]"))

for i in range(1,10):
    result = dan * i
    print(f"{dan} x {i} ={result}")
    
# 2단부터 9단가지 전부 출력
## 힌트: for 문에 for문을 넣을 수 있음 


    
    
