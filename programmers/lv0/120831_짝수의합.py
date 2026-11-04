# 문제: 짝수의 합
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 유형: 반복문
# 결과: 맞음
# 걸린 시간: 약 2분
# 핵심 아이디어: range(n + 1)로 n까지 포함해 돌면서 짝수만 더한다

def solution(n):
    answer = 0

    for i in range(n + 1):
        if i % 2 == 0:
            answer += i

    return answer
