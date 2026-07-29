"""
start algortm

"""

def returnindex(nums:list, target:int):
    seen = {}
    for i , number in enumerate(nums):
        needed = target-number
        if needed in seen:

            return [seen[needed],i]
        seen[number]=i
        

def zero(nums:list):
    position = 0
    for number in nums:
        if number!=0:
            nums[position] = number
            position +=1
    while position<len(nums):
        nums[position] = 0
        position+=1
    return nums


def sumtagret(nums:list, target:int):
    i = 0
    result = []
    while i<len(nums)-1:
        j = i+1
        while j<len(nums):
            if nums[j]+nums[i] == target:
                result.append([nums[i],nums[j]])
            j+=1
        i+=1
    return result

a = list(map(int,input("sonlarni kirit: ").split()))
b = int(input("Son kirit: "))
print(sumtagret(a,b))