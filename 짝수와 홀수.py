'''
문제 설명
정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

제한 조건
num은 int 범위의 정수입니다.
0은 짝수입니다.

def solution(num):
    answer = ''
    return answer
'''

def solution(num):
    return 'Even' if num % 2 == 0 else 'Odd'

# test
print(solution(3))
print(solution(4)) 

# 다른사람 코드 풀이
'''
def solution(num):
    return "Even" if num&1 == 0 else "Odd"
'''

'''
def solution(num): return ["Even", "Odd"].pop(num % 2)
'''
# .pop : 리스트의 맨 마지막 원소를 리턴하고 해당 원소를 삭제
# pop(i) : 리스트의 i번째 원소를 리턴하고 삭제

'''
def evenOrOdd(num):
    return 'Odd' if num & 1 else 'Even'

print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))
'''