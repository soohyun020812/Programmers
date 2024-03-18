'''
문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.

def solution(n):
    answer = 0
    return answer
'''

def solution(n):
    answer = 0 # 약수를 더한 값을 저장할 변수를 초기화
    
    # 1부터 n까지의 숫자를 반복하면서 n의 약수인지 확인
    for i in range(1, n + 1):
        if n % i == 0: # n을 현재 숫자로 나누어 떨어지면 약수
            answer += i # 약수이므로 answer에 더함
    
    return answer # 모든 약수를 더한 값을 반환

# 다른사람 코드 풀이
'''
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
'''

'''
def sumDivisor(num):
    return sum([i for i in range(1,num+1) if num%i==0])

print(sumDivisor(12))
'''