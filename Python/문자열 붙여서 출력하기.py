'''
문제 설명
두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.

제한사항
1 ≤ str1, str2의 길이 ≤ 10

str1, str2 = input().strip().split(' ')
'''

str1, str2 = input().strip().split(' ') # 입력으로부터 공백을 기준으로 문자열을 나누어 str1과 str2에 할당
result = str1 + str2 # str1과 str2를 이어붙임
print(result)

# 다른사람 코드 풀이
'''
print(input().strip().replace(' ', ''))
1. input() 함수를 사용하여 사용자로부터 입력 받음
2. strip() 메서드를 사용하여 입력된 문자열의 양쪽 끝에 있는 공백을 제거
3. replace(' ', '') 메서드를 사용하여 공백을 빈 문자열로 대체
즉, 입력된 문자열에서 모든 공백을 제거
4. print() 함수를 사용하여 결과 출력
'''

'''
str1, str2 = input().strip().split(' ')
print(str1, str2, sep='')
'''