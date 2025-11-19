# 새파일: number_game.py

import random

number = random.randint(1, 100)
print(f"랜덤 숫자: {number}")

# 게임 로직 
# 1. 컴퓨터가 1~100 사이 숫자를 하나 정함 
# 2. 사용자가 숫자를 입력
# 3. 컴퓨터가 힌트 제공: 높음, 낮음, 정답
# 4. 몇 번 만에 맞추는지 카운트 

# 1단계. 랜덤 숫자 생성 
answer = random.randint(1,100)
tries = 0 

print("= = = 숫자 맞추기 게임 = = =")
print("1부터 100 사이의 숫자를 맞춰보세요~!")

# 2단계: 게임 루프
while True:
  # 사용자 입력
  user = int(input("\n 숫자를 입력하세요: "))
  tries += 1 
    
  # 3단계 정답 확인 (if문)
  if user == answer: 
    print(f"정답! {tries}번 만에 맞추셨습니다.")
  elif user < answer:
    print("더 높습니다.")
  else:
    print("더 낮습니다.")
    
    


    