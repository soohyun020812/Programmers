'''
문제 설명
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

제한사항
N의 범위 : 100,000,000 이하의 자연수

def solution(n):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
'''

def solution(n):
    answer = 0
    # 주어진 자연수 n을 문자열로 변환하여 각 자릿수를 분리
    digits = str(n)
    # 각 자릿수를 순회하면서 합을 구함
    for digit in digits:
        answer += int(digit) # 각 자릿수를 정수로 변환하여 합에 더함
    return answer

# 다른사람 코드 풀이
# 개편된 문제에 대한 풀이
'''
def sum_digit(number):
    # number의 각 자릿수를 더해서 return
    if number < 10:
        return number
    return number%10 + sum_digit(number//10)
print("결과 : {}".format(sum_digit(123)));
'''
# // : 나누기의 몫 연산자
# 재귀함수를 이용한 풀이

'''
def sum_digit(number):
    return sum([int(i) for i in str(number)])
print("결과 : {}".format(sum_digit(123)));
'''