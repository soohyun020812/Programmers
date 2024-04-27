"""
문제 설명
임의의 양의 정수 n에 대해, 
n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, 
n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

제한 사항
n은 1이상, 50000000000000 이하인 양의 정수입니다.

def solution(n):
    answer = 0
    return answer
"""


def solution(n):
    # n이 양의 정수 x의 제곱인지 확인
    x = int(n**0.5)  # n의 제곱근을 구함
    if x**2 == n:  # x의 제곱이 n과 같다면
        return (x + 1) ** 2  # (x+1)의 제곱을 반환
    else:
        return -1  # 아니라면 -1 반환


# 다른사람 코드 풀이
# 개편된 문제에 대한 풀이
"""
def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or 'no'

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));
"""
# reverse = True 옵션을 사용하여 내림차순으로 정렬할 수 있다.
# join() 함수를 사용하여 리스트의 요소를 문자열로 결합할 수 있다.
