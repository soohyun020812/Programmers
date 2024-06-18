'''
문제 설명
주어진 초기 코드는 변수에 데이터를 저장하고 출력하는 코드입니다. 아래와 같이 출력되도록 빈칸을 채워 코드를 완성해 주세요.

출력 예시
Spring is beginning
13
310

빈칸 채우기 문제 안내
빈칸 채우기는 이미 완성된 코드 중 빈칸에 알맞은 코드를 입력하는 문제 타입입니다.
빈칸을 제외한 기본 코드는 수정할 수 없습니다.
빈칸을 채우지 않을 경우, 실행 결과에 에러 메시지가 표시됩니다.

string_msg = 
int_val = 
string_val = 

print(string_msg)
print(int_val + 10)
print(string_val + "10")
'''

string_msg = "Spring is beginning"
int_val = 3
string_val = "3"

print(string_msg)
print(int_val + 10)
print(string_val + "10")

# 다른사람 코드 풀이
'''
string_msg = "Spring is beginning"
int_val = len(string_msg.split())
string_val = str(int_val)

print(string_msg)
print(int_val + 10)
print(string_val + "10")
'''