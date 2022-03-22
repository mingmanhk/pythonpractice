def solution(height):
    res= 0
    left, right = 0, len(height)-1

    while left < right:
        # no of block x hight
        area = (right-left) * min(height[left] , height[right])
        res= max(res,area)

        if height[left] < height[right]:
            left+=1
        else:
            right-=1

    return res

print(solution([1,1]))