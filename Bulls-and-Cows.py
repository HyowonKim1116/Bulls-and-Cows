# 1. 필요한 라이브러리 import
from random import randrange #난수 생성을 위한 라이브러리

# 2. 난수 3개를 생성한 후 리스트로 저장
answer_set = set()                #집합 생성
while len(answer_set) < 3:        #집합 answer의 원소 개수가 3이 될 때까지
    answer_set.add(randrange(10)) #answer에 난수를 추가
                                  #집합의 성질에 의해 중복을 허용하지 않음
answer = list(answer_set)         #집합을 리스트로 변환

# 3. 반복문을 이용한 참가 인원수 입력
player_num = 0 #참가 인원수 변수 선언
while player_num < 1: #참가 인원수로 양수가 입력될 때까지 반복 실행
    try:
        player_num = int(input(">>> 게임 참가 인원수: ")) #참가 인원수 입력
        if player_num < 1: #입력값이 0 또는 음수일 경우
            print("Error: 1 이상의 정수를 입력해주세요.")
    except:                #입력값이 정수가 아닐 경우
        print("Error: 1 이상의 정수를 입력해주세요.")

# 4. 각종 변수 선언
try_cnt = 0   #기회 변수 선언
result = True #반복문 종료를 위한 변수 선언

print("게임을 시작합니다. 기회는 인당 10번입니다.")

# 5. 삼중 반복문을 이용한 게임 실행
# 5-1) 첫 번째 반복문: 3 strike 또는 기회 10번을 채울 때까지 게임 반복 실행
while True:
    try_cnt += 1
    print(f"\n[{try_cnt}번째 기회]")
    
    # 5-2) 두 번째 반복문: 참가 인원수만큼 숫자 입력 및 자리수 분리
    for i in range(player_num):
        number = int(input(f"player{i+1} 입력: "))

        num1 = number // 100        #입력한 값의 백의 자리수
        num2 = (number % 100) // 10 #입력한 값의 십의 자리수
        num3 = number % 10          #입력한 값의 일의 자리수
        nums = [num1, num2, num3]   #입력한 값의 백, 십, 일의 자리수를 리스트로 저장

        strike_cnt, ball_cnt = 0, 0 #strike수, ball수 선언 및 초기화

        # 5-3) 세 번째 반복문: 입력한 값을 answer와 비교하며 strike수, ball수 결정
        for j in range(3):
            if nums[j] in answer:        #answer에 포함되는 값 중에서
                if nums[j] == answer[j]: #숫자 위치가 같을 경우
                    strike_cnt += 1      #strike수 1 증가
                else:                    #숫자 위치가 다를 경우
                    ball_cnt += 1        #ball수 1 증가
        
        print(f"{strike_cnt} strike, {ball_cnt} ball") #결과 출력

        #두 번째 반복문 종료 조건
        if strike_cnt == 3: #숫자 3개 모두 값과 위치가 같을 경우
            result = False  #result 변수에 False 대입
            print(f"\n정답입니다. player{i+1} 우승!")
            break
    
    #첫 번째 반복문 종료 조건
    if result == False: #result 변수가 False일 경우 (3 strike일 경우)
        break
    if try_cnt == 10:   #기회 10번을 모두 소진했을 경우
        print("\n기회 10번을 초과하였습니다.")
        if player_num > 1:
            print("무승부입니다!")
        break

# 6. 게임 종료 후 메시지 출력
print("게임을 종료합니다.")