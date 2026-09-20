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


def binarysearch(nums:list, target:int):
    i = 0
    j = len(nums)-1
    while i<=j:
        med = (i+j)//2
        if nums[med]==target:
            return med
        elif nums[med]>target:
            j = med-1
        elif nums[med]<target:
            i = med+1
    return -1


def firstandend(numbers:list, target:int):
    result = []
    i = 0
    j = len(numbers)-1
    while numbers[i] != target or numbers[j]!=target:
        if numbers[i] != target:
            i+=1
        if numbers[j] != target:
            j-=1
        if i==j:
            return [-1,-1]
        result.append([i,j])
    return result[-1]


def qavslar(word:str):
    l1 = list(word)
    qavslar = {
               '{':'}',
               '[':']',
               '(':')'
               }
    i = 0
    j = len(l1)-1
    while i<=(j+1)//2-1:
        print(qavslar[l1[i]], l1[j])
        if str(qavslar[l1[i]]) == l1[j]:
            i+=1
            j-=1
        else:
            return False
    return True
            
    
# a = list(map(int,input("sonlarni kirit: ").split()))
# b = int(input("Son kirit: "))
# a = input('Qavslarni kiriting: ')
# print(qavslar(a))

# import pefile
# import yara

# PE fayl tahlil qilish
# pe = pefile.PE('malware.exe')
# print(f"Machine: {pe.FILE_HEADER.Machine}")
# print(f"Sections: {[s.Name.decode() for s in pe.sections]}")

# # YARA rules bilan tekshirish
# rules = yara.compile(filepath='rules.yar')
# matches = rules.match(filename='suspect.exe')
# for match in matches:
#     print(f"[!] Malware topildi: {match.rule}")

import http
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

session = requests.Session()

url = "https://example.com"

login_data = {
    'username':'',
    'password':''
}



response = session.post(url, login_data) 
print(f"Login Status: {response.status_code}")