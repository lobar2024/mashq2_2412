# 1) 1–15 sonlarning kvadratlari
set1 = {i**2 for i in range(1, 16)}

# 2) nums ichidan juft sonlar
nums = [1, 2, 2, 3, 4, 4, 5]
set2 = {i for i in nums if i % 2 == 0}

# 3) so‘zlarning uzunliklari
words = ["apple", "banana", "cherry", "kiwi"]
set3 = {len(word) for word in words}

# 4) manfiy sonlar
nums2 = [-3, -1, 0, 2, 4]
set4 = {i for i in nums2 if i < 0}

print(set1, set2, set3, set4)
