def containsDuplicate(nums) -> bool:
    hashset = set()
        
    for i in range(len(nums)):
        if nums[i] in hashset:
                return True
        hashset.add(nums[i])
    return False

print(containsDuplicate([1,2,3,4]))