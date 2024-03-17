'''
문제 설명
자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

제한사항
3 ≤ n ≤ 1,000,000

def solution(n):
    answer = 0
    return answer
'''

def solution(n):
    for x in range(2, n): # 1은 모든 자연수에 대해 나머지가 0이 되므로 2부터 시작
        if n % x == 1:
            return x # 조건을 만족하는 가장 작은 x 반환

# test
print(solution(10))
print(solution(12))

# 다른사람 코드 풀이
'''
def solution(n):
    answer = min([x for x in range(1, n+1) if n % x == 1])
    return answer
'''

'''
def solution(n):
    answer = 0
    for i in range(2, n):
        if n % i == 1:
            return i
    return answer
'''
# 1. i를 2로 초기화, 이는 x를 찾기 위한 시작점 역할 : x가 1인 경우는 모든 자연수 n에 대해 나머지가 0
# 2. while 루프를 사용하여 (n-1) % i의 결과가 0이 아닐 때까지 i의 값을 1씩 증가,
# (n-1) % i가 0이 되는 순간 n-1은 i로 나누어떨어진다는 의미로 n % i == 1과 동일한 조건
# 3. 조건을 만족하는 첫 번째 i 값을 찾으면 while 루프가 종료
# i 값이 문제에서 요구하는 n을 x로 나누었을 때 나머지가 1이 되도록 하는 가장 작은 자연수 x
# = i=2일 때 : (10-1) % 2 = 1이므로 조건을 만족하지 않음
# = i=3일 때 : (10-1) % 3 = 0이므로 조건을 만족

'''
solution = lambda n: min(list(filter(lambda x:n%x==1,range(1,n+1))))
'''
# 1. range(1, n+1) : n을 포함하기 위해 n+1을 사용 (n을 나눌 후보)
# 2. lambda x: n % x == 1 : 람다 함수를 사용해 주어진 숫자 x가 n을 나누었을 때 나머지가 1이 되는지를 확인
# 3. filter(lambda x: n % x == 1, range(1, n+1)) : 필터 함수를 사용하여 1부터 n까지의 숫자 중에서 n을 나누었을 때 나머지가 1이 되는 숫자만을 골라냄
# 4. list(filter(lambda x: n % x == 1, range(1, n+1))) : 필터링 된 결과를 리스트로 반환하고 숫자들이 리스트 형식으로 저장됨
# 5. min(list(filter(lambda x: n % x == 1, range(1, n+1)))) : 조건을 만족하는 숫자 중 가장 작은 수를 찾음, main 함수를 사용하여 리스트에서 가장 작은 값을 선택
# 6. solution = lambda n : 최종적으로 전체 과정을 n을 입력받는 람다 함수로 정의