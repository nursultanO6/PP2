def has_007(nums):
    seq = [0, 0 ,7]
    for i in nums:
        if i == seq[0]:
            seq.pop(0)
        if not seq:
            return True
    return False
nums = [1, 2, 3, 0, 0, 7, 1, 4]
print(has_007(nums))