# 문제: 배열의 평균값
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 유형: 배열
# 결과: 맞음
# 걸린 시간: 1분 미만
# 핵심 아이디어: for문으로 합을 누적하고 len()으로 나눈다

def solution(numbers):
    nums = 0

    for num in numbers:
        nums += num

    answer = nums / len(numbers)
    return answer
