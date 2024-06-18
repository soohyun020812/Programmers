'''
문제 설명
직각삼각형이 주어졌을 때 빗변의 제곱은 다른 두 변을 각각 제곱한 것의 합과 같습니다.

피타고라스.jpg

직각삼각형의 한 변의 길이를 나타내는 정수 a와 빗변의 길이를 나타내는 정수 c가 주어질 때, 다른 한 변의 길이의 제곱, b_square 을 출력하도록 한 줄을 수정해 코드를 완성해 주세요.

제한사항
1 ≤ a < c ≤ 100

a = int(input())
c = int(input())

b_square = c - a
print(b_square)
'''

a = int(input())
c = int(input())

b_square = c**2 - a**2
print(b_square)

# 다른사람 코드 풀이
'''
a = int(input())
c = int(input())

b_square = pow(c,2) - pow(a,2)
print(b_square)
'''
# pow(x, y) : x의 y제곱을 계산하는 함수