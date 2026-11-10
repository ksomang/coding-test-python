# 문제: 모의고사
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 유형: 완전탐색
# 결과: 맞음 (힌트 받아 통과: 패턴 반복, 리스트 안의 리스트 꺼내기)
# 걸린 시간: 이틀에 걸쳐 (11/9~11/10)
# 핵심 아이디어: j번 문제의 찍은 답은 p[j % len(p)] → 수포자별 점수 세기 → 최고 점수와 같은 사람을 1부터 번호로 모으기
# 다시 풀기: 2026-11-13 예정

def solution(answers):
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    answer = {}
    for i in range(0, 3):
        cnt = 0
        p = patterns[i]
        for j in range(0, len(answers)):
            if answers[j] == p[j % len(p)]:
                cnt += 1
        answer[i] = cnt

    best = float('-inf')
    for i in range(0, 3):
        if answer[i] > best:
            best = answer[i]

    tem = []
    for i in range(0, 3):
        if best == answer[i]:
            tem.append(i + 1)

    return tem
