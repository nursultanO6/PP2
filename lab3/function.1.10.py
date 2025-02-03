def unique(nums):
    udict = {}
    for num in nums:  
        udict[num] = udict.get(num, 0) + 1  

    for key, value in udict.items():
        if value == 1:
            print(key)
nums = [1 ,2, 3, 4, 5, 6, 5, 6, 4, 7]
unique(nums)