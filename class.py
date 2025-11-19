# 새 파일: class.py 
# 붕어빵 틀(클래스):설계도, 같은 몽야의 붕어빵을 계속 만들 수 있음
# 실제 붕어빵(객체): 틀로 찍어낸 결과물, 각각은 개별의 붕어빵

class Dog:                              #대문자 사용해야함 
    def __init__(self, name, age):     #init 생성자라고 이해하자 
        self.name = name 
        self.age = age
    
    def bark(self):
        print(f"{self.name}: 멍멍~")
        
    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}세")
        
# 객체 생성(붕어빵 찍어내기)
dog1 = Dog("바둑이",3)
dog2 = Dog("초코",5)            #dog2.name 초코, dog2

# 메서드 호출                   #클래스 안의 함수를 메서드 라고 함 
dog1.bark()
dog1.info()
print()
dog2.bark()
dog2.info()
 
 #강아지 클래스 실습
class Dog:
     def __init__(self, name):
         self.name = name
         self.energy = 100
         
     def brak(self): # 10씩 감소
        print("f {self.name}: 멍멍~~")
        self.energy -= 10
     def eat(self):
        print(f"{self.name}이(가) 밥을 먹었습니다.")
        self.energy = 100 
     def status(self):
         print("f{self.name}의 에너지: {self.energy}")

my_dog = Dog("흰둥이")      #객체 = 실제로 만든 것 

####
print("내사랑 흰둥이")
my_dog.status()
my_dog.brak()
my_dog.brak()
my_dog.status()
my_dog.eat()
my_dog.status()
my_dog.brak()
my_dog.brak()
my_dog.brak()
my_dog.brak()
my_dog.status()
