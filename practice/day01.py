# 워밍업 3문제
# 1. 정수 두 개를 한 줄씩 입력받아 합을 출력하기 (입력 3, 5 -> 8)
n1 = int(input())
n2 = int(input())
print(n1 + n2)

# 2. 정수 하나를 입력받아 짝수면 True, 홀수면 False 출력하기
n3 = int(input())

print(n3 % 2 == 0)

# 3. 분(minute)을 입력받아 "몇 시간 몇 분"으로 출력하기
minute = int(input())
print (f"{minute // 60}시간 {minute % 60}분")
