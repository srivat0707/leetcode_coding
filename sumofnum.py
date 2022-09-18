def ans(nums,target):
    min1=10000000
    mine1=nums[0]
    for i in nums:
        print(abs(i-target),min1)
        if abs(i-target)<min1:
            min1=abs(i-target)
            mine1=i
    nums.remove(mine1)
    min2=10000000
    mine2=nums[0]
    for j in nums:
        if abs(mine1+j-target)<min2:
            min2=abs(min1+j-target)
            mine2=j
    nums.remove(mine2)
    min3=100000000
    mine3=nums[0]
    for k in nums:
        if abs(mine1+mine2+k-target)<min3:
            min3=abs(mine1+mine2+k-target)
            mine3=k
    print(mine1,mine2,mine3,mine1+mine2+mine3)

ans([-3,-2,-1,0,1,2],3)
    