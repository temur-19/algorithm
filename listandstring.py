def secondmax(numbers:list):
    numbers.remove(max(numbers))
    return max(numbers)


def removenumber(numbers:list):
    res = []
    for i in numbers:
        if i not in res:
            res.append(i)
    return res

a = list(map(int, input('Sonlarni kiriting: ').split()))
print(removenumber(a))