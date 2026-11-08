# 문제: 폰켓몬
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 유형: 해시 (set)
# 결과: 맞음 (두 번 틀린 뒤 통과)
# 걸린 시간: 약 20분
# 핵심 아이디어: 서로 다른 종류 수(len(set))와 가져갈 수(N // 2) 중 작은 쪽이 답
# 다시 풀기: 2026-11-08 힌트 없이 혼자 통과 (5분 미만)

def solution(nums):
    set_nums = set(nums)
    dev_nums = len(nums) // 2     # 가져갈 수
    answer = len(set_nums)    # 종류 수

    if dev_nums > answer:
        return answer
    else:
        return dev_nums
