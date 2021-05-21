from itertools import permutations

def palindrome(x):
    rev = x[::-1]
    a = False
    if (rev==x):
        a = True
    return a


def longest_palindrome(s):

    last = len(s)
    lst = []
    for i in range(last):
        for j in range(i+1, last):
            b = s[i:j+1]
            a = palindrome(b)
            if a:
                lst.append(b)
    return lst

a = input("Введите строку: ")
print(longest_palindrome(a))

print()

def compareStr(s1, s2):
    for i in range(len(s1)):
        if s1[i] > s2[i]:
            return 0
    return 1

s1 = "abc"
s2 = "xya"
correct = False
for str1 in permutations(s1):
    for str2 in permutations(s2):
        if compareStr(str1, str2) == 1:
            correct = True
            break
print(correct)
