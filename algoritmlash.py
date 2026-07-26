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
    for i in range(0, len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(i))
    return nums
a = list(map(int,input("sonlarni kirit: ").split()))
# b = int(input("Son kirit: "))
print(zero(a))