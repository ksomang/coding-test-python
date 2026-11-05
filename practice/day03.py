# 1. fruits = {"apple": 3, "banana": 5}에 "cherry": 2를 추가하고,
# 모든 과일 개수의 합을 출력하기 → 10
fruits = {"apple": 3, "banana": 5}
fruits["cherry"] = 2
cnt = 0
for i in fruits:
    cnt += fruits[i]
print(cnt)

# 2. "hello world"에서 "l"이 몇 번 나오는지 딕셔너리로 세서 출력하기 → 3
world = {}
for i in "hello world":
    if i in world:
        world[i] += 1
    else:
        world[i] = 1

print(world["l"])

# 3. nums = [1, 3, 3, 5, 1, 7]에서 서로 다른 숫자가 몇 개인지 출력하기 → 4
nums = [1, 3, 3, 5, 1, 7]
ss = set(nums)
print(len(ss))
