"""
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.

def solution(n):
    answer = []
    return answer
"""


def solution(n):
    answer = []
    # 숫자를 문자열로 변환하여 뒤집기
    reversed_str = str(n)[::-1]
    # 뒤집은 문자열을 순회하면서 각 자리 숫자를 배열에 추가
    for digit in reversed_str:
        answer.append(int(digit))
    return answer


# 다른사람 코드 풀이
# 개편된 문제에 대한 풀이
"""
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
"""
# str(n): 숫자를 문자열로 변환
# reversed(str(n)): 문자열을 역순으로 뒤집음
# map(int, reversed(str(n))): 각 문자를 정수로 변환하는 함수(map)를 적용하여 리스트로 변환
# list(map(int, reversed(str(n)))): 정수로 변환된 문자열을 리스트로 변환
