"""
문제 설명
String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, 
"김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. 
seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

제한 사항
seoul은 길이 1 이상, 1000 이하인 배열입니다.
seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
"Kim"은 반드시 seoul 안에 포함되어 있습니다.

def solution(seoul):
    answer = ''
    return answer
"""


def solution(seoul):
    idx = seoul.index("Kim")  # "Kim"의 인덱스를 찾아서 idx에 저장
    answer = "김서방은 {}에 있다".format(
        idx
    )  # 인덱스를 포함한 결과 문자열을 answer에 저장
    return answer


# 다른사람 코드 풀이
# 개편된 문제에 대한 풀이
"""
def findKim(seoul):
    # 함수를 완성하세요

    return "김서방은 {}에 있다".format(seoul.index('Kim'))


# 실행을 위한 테스트코드입니다.
print(findKim(["Queen", "Tod", "Kim"]))
"""
# seoul.index('Kim')을 이용하여 "Kim"의 인덱스를 찾아서 바로 반환하는 방법
