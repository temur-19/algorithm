def sumnumber(number):
    result = 0
    while number:
        result+=number%10
        number = number//10
    return result


 

def teskarison(number):
    result = 0
    while number:
        result *= 10
        result += number%10
        number = number//10
    return result 

def ispallindromnumber(number):
    if teskarison(number) == number:
        return True
    else:
        return False
    
def maxdigit(number):
    result = 0
    while number:
        i = number%10
        number //=10
        if i>result:
            result = i
    return result

def unliharflar(matn):
    result = 0
    for i in matn:
        if i in ['a','u','i','o','e',"o'"]:
            result+=1
    return result
# a = input("So'zni kiriting: ")
# print(f"Unli harflar: {unliharflar(a)}")


def number(number):
    for i in range(0, number):
        if i%3 == 0:
            print(f'{i} Fizz')
        elif i%5 == 0:
            print(f'{i} Buzz')
        elif i%3 == 0 and i%5 == 0:
            print(f'{i} Fizzbuzz')
        else:
            print(i)

a = int(input("Son kirit: "))
print(number(a))

