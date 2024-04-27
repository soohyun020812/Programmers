"""
문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.

def solution(n):
    answer = 0
    return answer
"""


def solution(n):
    # 주어진 정수를 문자열로 변환하여 각 자릿수를 리스트에 저장
    digits = list(str(n))
    # 각 자릿수를 내림차순으로 정렬
    digits.sort(reverse=True)
    # 정렬된 자릿수를 문자열로 결합하여 정수로 반환
    answer = int("".join(digits))
    return answer


# 다른사람 코드 풀이
"""
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
"""
# reverse = True 옵션을 사용하여 내림차순으로 정렬할 수 있다.
# join() 함수를 사용하여 리스트의 요소를 문자열로 결합할 수 있다.
