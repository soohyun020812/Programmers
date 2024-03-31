'''
문제 설명
문자열 my_string, overwrite_string과 정수 s가 주어집니다. 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

제한사항
my_string와 overwrite_string은 숫자와 알파벳으로 이루어져 있습니다.
1 ≤ overwrite_string의 길이 ≤ my_string의 길이 ≤ 1,000
0 ≤ s ≤ my_string의 길이 - overwrite_string의 길이

def solution(my_string, overwrite_string, s):
    answer = ''
    return answer
'''

def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
    return answer

# 1. my_string[:s] : my_string에서 인덱스 s 이전까지의 부분을 선택
# 2. overwrite_string : 대체할 부분인 overwrite_string을 선택
# 3. my_string[s + len(overwrite_string):] : overwrite_string이 끝나는 부분 이후의 문자열을 선택
# 4. + 연산자로 이어붙여서 my_string의 일부를 대체한 새로운 문자열 생성
# 5. 만들어진 문자열을 answer에 할당하고, answer를 반환

# 다른사람 코드 풀이
'''
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
'''

'''
def solution(m, o, s):
    return m[:s]+o+m[len(o)+s:]
'''