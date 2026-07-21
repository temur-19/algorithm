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
a = int(input("Sonni kiriting: "))
print(ispallindromnumber(a))