#Time O(n2)
#Space O(1) or O(n) depend on the complexiity
def threesum(nums):
    res = []
    nums.sort()
    
    for i, a in enumerate(nums): 
        # remove duplicate
        if i > 0 and a == nums[i-1]:
            continue
        
        left, right = i+1, len(nums)-1
        while left < right:
            threeSum= a + nums[left] + nums[right]
            if threeSum >0:
                right -=1
            elif threeSum <0:
                left +=1
            else:
                res.append([a ,nums[left] , nums[right]])
                left+=1
                while nums[left] == nums[left-1] and left<right:
                    left+=1
    print(res)
        



threesum([-1,0,1,2,-1,-4])