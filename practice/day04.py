# def add(a, b):
#     return a + b
# print(add(3, 5))

# nums = [3, 1, 2]
# new = sorted(nums)
# nums.sort()
# sorted(nums, reverse=True)

# words = ["banana", "kiwi", "apple"]
# sorted(words)
# sorted(words, key=len)

# pairs = [("kim", 90), ("lee", 80), ("park", 95)]
# sorted(pairs, key=lambda x: x[1])

# 리스트를 받아 가장 큰 값과 가장 작은 값의 차이를 return하는 함수 diff(nums) 만들기.
# max, min 쓰지 말고 정렬로 → diff([3, 9, 1]) = 8
def diff(nums):
    nums.sort()
    return nums[-1] - nums[0]

# ["ccc", "a", "bb"]를 길이가 긴 순서로 정렬해 출력하기 → ['ccc', 'bb', 'a']
def len_word(arr):
    return sorted(arr, reverse=True, key=len)

# pairs = [("kim", 90), ("lee", 80), ("park", 95)]를
# 점수가 높은 순서로 정렬해서 이름만 출력하기 → park kim lee
def good_score (pairs):
    arr = sorted(pairs, reverse=True, key=lambda x: x[1])

    for i in arr:
        print(i[0])
