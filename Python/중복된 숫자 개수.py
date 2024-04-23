"""
문제 설명
정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

제한사항
1 ≤ array의 길이 ≤ 100
0 ≤ array의 원소 ≤ 1,000
0 ≤ n ≤ 1,000

def solution(array, n):
    answer = 0
    return answer
"""


def solution(array, n):
    answer = 0
    for num in array:
        if num == n:
            answer += 1
    return answer


# 다른사람 코드 풀이
# count() 함수를 이용한 풀이
"""
def solution(array, n):
    return array.count(n)
"""
