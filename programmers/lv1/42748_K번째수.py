# 문제: K번째수
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42748
# 유형: 정렬
# 결과: 맞음 (힌트로 문제를 단계별로 쪼갠 뒤 통과)
# 걸린 시간: 약 30분
# 핵심 아이디어: 명령마다 array[i-1:j]로 자르고 정렬한 뒤 k-1번째를 꺼낸다 (1부터 세는 번호 → 0부터로 변환)
# 다시 풀기: 2026-11-08 힌트 없이 혼자 통과 (10분 미만)

def solution(array, commands):
    answer = []
    tem_array = []

    for c in commands:
        tem_array = array[c[0] - 1:c[1]]
        tem_array.sort()
        answer.append(tem_array[c[2] - 1])

    return answer
