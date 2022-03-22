nums =[3,2,4]
target = 6

def twosum( num, target):
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):
            if nums[x] + nums[y] == target:
                return([x, y])

answer = twosum(nums, target)
print(answer)