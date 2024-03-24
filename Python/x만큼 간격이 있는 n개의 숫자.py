'''
문제 설명
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

제한 조건
x는 -10000000 이상, 10000000 이하인 정수입니다.
n은 1000 이하인 자연수입니다.

def solution(x, n):
    answer = []
    return answer
'''

def solution(x, n):
    answer = []
    for i in range(1, n + 1): # 1부터 n까지 반복
        answer.append(x * i) # x에 i를 곱한 값을 리스트에 추가
    return answer

# 다른사람 코드 풀이
# 개편된 문제에 대한 풀이
'''
def number_generator(x, n):
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))
'''

'''
def number_generator(x, n):
    return [i for i in range(x, x*n+1, x)]
print(number_generator(2,5))
'''

'''
def number_generator(x, n):
    if x <= 0:
        return [0] * n # x가 음수이거나 0인 경우 0으로만 이루어진 리스트 반환
    else:
        total = list(range(x, n * x + 1, x))
        return total
print(number_generator(3, 5))
'''
# 기존의 total = list(range(x, n * x + 1, x)) 코드에 if문 추가하여 x가 음수일 때와 0일 때를 걸러주는 코드 추가