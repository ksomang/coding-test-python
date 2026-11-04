# 문제: 문자열 뒤집기
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120822
# 유형: 문자열
# 결과: 맞음
# 걸린 시간: 약 2분
# 핵심 아이디어: 슬라이싱 [::-1]로 문자열을 뒤집는다

def solution(my_string):
    answer = my_string[::-1]
    return answer
