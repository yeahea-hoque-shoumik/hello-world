def three_sum(nums):
    if len(nums)==0:
        return []
    ans=[]
    nums.sort()
    for i in range(len(nums)-2):
        if nums[i]>0: break
        left,right=i+1,len(nums)-1
        if i>0 and nums[i]==nums[i-1]:
            continue
        while left<right:
            sum=nums[i]+nums[left]+nums[right]
            if sum==0:
                ans.append([nums[i],nums[left],nums[right]])
                left+=1
                while nums[left]==nums[left-1] and left<right:
                    left+=1
            if sum>0 and left<right:
                right-=1
            elif sum<0 and left<right :
                left+=1
    return ans

if __name__ == '__main__':
    nums=[2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
    print(three_sum(nums))