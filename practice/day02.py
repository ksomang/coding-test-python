# 1. nums = [3, 7, 2, 9, 4]의 합을 for문으로 구해 출력하기 (sum() 쓰지 않기) → 25
nums = [3, 7, 2, 9, 4]
result = 0

for num in nums:
    result += num

print(result)

# 2. 문자열 "hello"의 첫 글자와 마지막 글자를 출력하기 → h o
s = "hello"
print(f"{s[0]} {s[-1]}")

# 3. nums = [3, 7, 2, 9, 4]에서 짝수만 새 리스트에 담아 출력하기 → [2, 4]
answer = []

for x in nums:
    if x % 2 == 0:
        answer.append(x)

print(answer)
