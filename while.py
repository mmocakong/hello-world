#while 조건:
# 반복한 코드 


count = 1

while count <= 5: 
    print(f"{count}번째 안녕하세요.")
    count = count + 1 
    
print("END")


#break : 반복 즉시 탈출 
count = 1
while count <= 10:
    if count ==5:
        print("5가 되었으니 종료")
    print(count)
    count += 1 
    
# continue : 이번만 건너뛰기 
count = 0 
while count < 5:
    count += 1
    
    if count ==3:
        continue    # 3일 대는 아래 print를 건너뜀 

    
print(count)

        
