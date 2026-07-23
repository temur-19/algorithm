def secondmax(numbers:list):
    numbers.remove(max(numbers))
    return max(numbers)


def removenumber(numbers:list):
    res = []
    for i in numbers:
        if i not in res:
            res.append(i)
    return res


def countwords(string:str):
    words = string.split()
    res = []
    for i in words:
        res.append(f"{i}: {words.count(i)}")
    return set(res)

def isanagramwords(words1:str, words2:str):
    for i in words1.lower():
        if i not in words2.lower():
            return False
    return True


def longwords(string:str):
    words = string.split()
    res = 0
    for i in words:
        if len(i)>res:
            res = len(i)
            word = i
    return {word:res}

def indexright(array:list, k:int):
    for i in range(0,len(array)):
        array[i] = array[i-k]
        # if i+k>len(array)-1:
        #     array[i] = 
    return array
a = list(map(int,input('Sonlarni kiriting: ').split()))
b = int(input("k ni kiriting: "))
print(indexright(a,b))