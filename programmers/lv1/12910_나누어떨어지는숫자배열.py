# 문제: 나누어 떨어지는 숫자 배열
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12910
# 유형: 구현 (조건 + 정렬)
# 결과: 맞음 (힌트 없이 혼자 통과)
# 걸린 시간: 5분 미만
# 핵심 아이디어: divisor로 나누어 떨어지는 원소만 append → 정렬, 하나도 없으면 [-1]

def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer
