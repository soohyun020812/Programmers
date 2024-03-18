'''
문제 설명
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

제한사항
arr은 길이 1 이상, 100 이하인 배열입니다.
arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

def solution(arr):
    answer = 0
    return answer
'''

def solution(arr):
    # 배열의 모든 원소의 합을 구함
    total_sum = sum(arr)
    # 배열의 길이로 나누어 평균을 구하기
    average = total_sum / len(arr)
    return average

# 다른사람 코드 풀이
'''
def average(list):
    # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
    return sum(list) / len(list)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4] 
print("평균값 : {}".format(average(list)));
'''

'''
def average(list):
    # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
    if len(list) == 0:
        return 0

    else:
        return sum(list) / len(list)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4] 
print("평균값 : {}".format(average(list)));
'''