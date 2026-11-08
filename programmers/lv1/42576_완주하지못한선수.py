# 문제: 완주하지 못한 선수
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 유형: 해시
# 결과: 맞음 (set으로 동명이인을 없애는 방법에서 개수 세기로 바꾼 뒤 통과)
# 걸린 시간: 약 27분
# 핵심 아이디어: 참가자 이름별 인원수를 딕셔너리로 세고, 완주자마다 1씩 빼면 값이 남은 한 명이 답
# 다시 풀기: 2026-11-08 힌트 없이 혼자 통과 (10분 미만)

def solution(participant, completion):
    dic_participant = {}

    for i in participant:
        if i in dic_participant:
            dic_participant[i] += 1
        else:
            dic_participant[i] = 1

    for i in completion:
        if i in dic_participant:
            dic_participant[i] -= 1

    for i in dic_participant:
        if dic_participant[i] > 0:
            return i
