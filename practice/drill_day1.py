# ──────────────────────────────────────────────
# 1. for문의 i는 "원소 자체"다  (헷갈린 곳: 완주하지 못한 선수, good_score)
# ──────────────────────────────────────────────
# [따라 쓰기]
fruits = ["apple", "banana", "kiwi"]

for f in fruits:
    print(f[0])
    print(f)

for i in range(len(fruits)):
    print(i, fruits[i])


# ──────────────────────────────────────────────
# 2. 빈 리스트에는 번호로 넣을 수 없다 → append  (헷갈린 곳: K번째수)
# ──────────────────────────────────────────────
# [따라 쓰기]
result = []
result.append(10)
result.append(20)
print(result)

result_ = []

for r in range(1, 6):
    result_.append(r)

print(result_)


# ──────────────────────────────────────────────
# 3. 묶음(튜플)에서 칸 꺼내기  (헷갈린 곳: good_score)
# ──────────────────────────────────────────────
# [따라 쓰기]
p = ("kim", 90)
print(p[0])
print(p[1])

pairs = [("kim", 90), ("lee", 80)]
for p in pairs:
    print(p[0], "의 점수는", p[1])

for p in pairs:
    print(p[1])


# ──────────────────────────────────────────────
# 4. sorted()는 새 리스트를 "돌려준다", 담지 않으면 사라진다
#    (헷갈린 곳: nums = nums.sort(), 문자열 내 마음대로 정렬하기)
# ──────────────────────────────────────────────
# [따라 쓰기]
nums = [3, 1, 2]

sorted(nums)
print(nums)

new = sorted(nums)
print(new, nums)

nums.sort()
print(nums)

print(nums.sort())

new = sorted(nums, reverse=True)
print(new)


# ──────────────────────────────────────────────
# 5. key= 는 sorted / sort 안에만 쓴다. x에는 원소 하나가 들어온다
#    (헷갈린 곳: print 안에 key를 넣은 것, x[0]/x[1] 고르기)
# ──────────────────────────────────────────────
# [따라 쓰기]
words = ["banana", "kiwi", "apple"]

print(sorted(words, key=len))

print(sorted(words, key=lambda x: x[1]))

pairs = [("kim", 90), ("lee", 80), ("park", 95)]
print(sorted(pairs, key=lambda x: x[1]))

for p in sorted(pairs, key=lambda x: x[1], reverse=True):
    print(p[0])

for p in sorted(pairs, key=lambda x: x[0]):
    print(p[0])


# ──────────────────────────────────────────────
# 6. 기준이 두 개면 key가 묶음을 돌려준다  (헷갈린 곳: 문자열 내 마음대로 정렬하기)
# ──────────────────────────────────────────────
# [따라 쓰기]
words = ["abce", "abcd", "cdx"]
print(sorted(words, key=lambda x: (x[2], x)))

people = [("kim", 90), ("lee", 90), ("ahn", 80)]
print(sorted(people, key=lambda x: (x[1], x[0])))

print(sorted(people, key=lambda x: (x[0], x[1])))


# ──────────────────────────────────────────────
# 7. "i번째"(1부터) → 파이썬 번호(0부터), 슬라이싱 끝은 포함 안 함
#    (헷갈린 곳: K번째수, 짝수의 합)
# ──────────────────────────────────────────────
# [따라 쓰기]
array = [1, 5, 2, 6, 3, 7, 4]

print(array [2 - 1 : 5])

print(array[3 - 1])

print(list(range(1, 5 + 1)))

print(array[4 - 1: 7])


# ──────────────────────────────────────────────
# 8. 딕셔너리를 for로 돌면 "키"가 나온다  (헷갈린 곳: 워밍업 과일 합, 완주하지 못한 선수)
# ──────────────────────────────────────────────
# [따라 쓰기]
stock = {"apple": 3, "banana": 5}

for name in stock:
    print(name, stock[name])

count = {}
for ch in "banana":
    count[ch] = count.get(ch, 0) + 1

for c in count:
    if count[c] >= 2:
        print(c)
