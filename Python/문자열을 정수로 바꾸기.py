"""
문제 설명
문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

제한 조건
s의 길이는 1 이상 5이하입니다.
s의 맨앞에는 부호(+, -)가 올 수 있습니다.
s는 부호와 숫자로만 이루어져있습니다.
s는 "0"으로 시작하지 않습니다.

def solution(s):
    answer = 0
    return answer
"""


def solution(s):
    answer = int(s)
    return answer


# 다른사람 코드 풀이
# 개편된 문제에 대한 풀이
"""
def strToInt(str): 
    result = 0
    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)
    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));
"""
# enumerate()를 이용하여 인덱스와 값을 동시에 가져오는 방법
# str[::-1]을 이용하여 문자열을 뒤집는 방법
# int(number) * (10 ** idx)를 이용하여 문자열을 숫자로 변환하는 방법
