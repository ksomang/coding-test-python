# 문제: 문자열 내 마음대로 정렬하기
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12915
# 유형: 정렬
# 결과: 맞음 (힌트를 받고 통과)
# 걸린 시간: 약 20분
# 핵심 아이디어: key가 (n번째 글자, 문자열 전체) 묶음을 돌려주면 1순위가 같을 때 사전순으로 정렬된다

def solution(strings, n):
    answer = []
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer
