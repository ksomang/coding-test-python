# 문제: 두 개 뽑아서 더하기
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 유형: 완전탐색 (이중 for문)
# 결과: 맞음
# 걸린 시간: 약 10분
# 핵심 아이디어: j를 i + 1부터 돌려서 자기 자신·중복 쌍을 피하고, 합이 없을 때만 append 후 정렬

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer
