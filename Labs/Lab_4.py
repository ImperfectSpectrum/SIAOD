class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def show_elements(self):
        return (self.items)

    def peek(self):
        if self.items == []:
            return "error"
        else:
            return self.items[len(self.items)-1]

class Deque:
    def __init__(self):
        self.deque = []

    def pushFront(self, key):
        self.deque.insert(0, key)

    def pushBack(self, key):
        self.deque.append(key)

    def popFront(self):
        if self.deque == []:
            return "error"
        else:
            return self.deque.pop(0)

    def popBack(self):
        if self.deque == []:
            return "error"
        else:
            return self.deque.pop()

    def peekFront(self):
        if self.deque == []:
            return "error"
        else:
            return self.deque[0]

    def peekBack(self):
        if self.deque == []:
            return "error"
        else:
            return self.deque[len(self.deque)-1]

    def show_elements(self):
        return (self.deque)

    def size(self):
        return len(self.deque)

print("")
print("Задание №1")

def bigger(s1, s2):
    s1.lower()
    s2.lower()
    for i in range (len(s1)):
        if s1[i] >s2[i]:
            return True
        if s1[i] < s2[i]:
            return False

def sort(l):
    l1 = []
    A = Deque()
    B = Deque()
    for i in range(len(l)):
        if A.deque == []:
            A.pushBack(l[i])
            continue
        if bigger(A.peekBack(), l[i]) == False:
            A.pushBack(l[i])
            continue
        if bigger(A.peekFront(), l[i]) == True:
            A.pushFront(l[i])
            continue
        x = A.peekBack()
        while bigger(x, l[i]) == True:
            x = A.popBack()
            B.pushFront(x)
            x = A.peekBack()
        A.pushBack(l[i])
        while B.deque != []:
            x = B.popFront()
            A.pushBack(x)
    while A.deque != []:
        x = A.popFront()
        l1.append(x)
    return l1

book = ["Дикие лебеди", "Дюймовочка", "Огниво", "Русалочка", "Три мушкетера", "Баба-Яга", "Александр"]
bookSorted = sort(book)
print(bookSorted)

print()
print("Задние №2")
N2 = Deque()
str = "офхук нхщъкл дхй"
strN = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
for i in range(len(strN)):
    N2.pushBack(strN[i])


def dehash(str, D):
    str1 = ""
    for i in range(len(str)):
        if str[i] == " ":
            str1+= " "
            continue
        while len(str1)<=i:
            if D.peekBack() == str[i]:
                x = D.popBack()
                D.pushFront(x)
                x = D.popBack()
                D.pushFront(x)
                str1 += D.popBack()
                D.pushBack(str1[i])
            else:
                x = D.popBack()
                D.pushFront(x)
    return str1

print(dehash(str, N2))



list1 = [3, 2, 1, 0]
n = len(list1)
A = Stack()

for i in list1:
    A.push(i)

B = Stack()
C = Stack()


def move_disks(A, B, C, n):
    if n == 0:
        return
    elif n == 1:
        C.push(A.pop)
    elif n == 2:
        x = A.pop()
        B.push(x)

        y = A.pop()
        C.push(y)

        z = B.pop()
        C.push(z)
    else:
        move_disks(A, C, B, n - 1)
        y = A.pop()
        C.push(y)
        move_disks(B, A, C, n - 1)


move_disks(A, B, C, n)

print()
print('Задание №3')
print(A.show_elements(), B.show_elements(), C.show_elements())

print()
print("Задние №4")

str = "()(()))"
def isBalanced(str):
    N4 = Stack()
    for i in range(len(str)):
        if str[i] == "(" or str[i] == ")":
            if N4.isEmpty() == True:
                if str[i] == ")":
                    return False
                N4.push(str[i])
                continue
            if str[i] == ")" and N4.peek() == "(":
                N4.pop()
                continue
            N4.push(str[i])
    if N4.isEmpty() == False:
        return False
    return True
print(isBalanced(str))

print()
print("Задание 5:")
str = "[][][]"
def isBalanced(str):
    N5 = Deque()
    for i in range(len(str)):
        if str[i] == "[" or str[i] == "]":
            if N5.size() == 0:
                if str[i] == "]":
                    return False
                N5.pushBack(str[i])
                continue
            if str[i] == "]" and N5.peekBack() == "[":
                N5.popBack()
                continue
            N5.pushBack(str[i])
    if N5.size() > 0:
        return False
    return True
print(isBalanced(str))

list = ['1','2','3',"s","u",'7',"q","&",'7',"%"]

A = Stack()
B = Stack()
C = Stack()
D = Stack()

for i in range(len(list)):
    x = list[i]
    A.push(x)
    if ord(list[i]) >= 33 and ord(list[i]) <= 47:
        D.push(x)
    if ord(list[i]) >= 48 and ord(list[i]) <= 57:
        B.push(x)
    if ord(list[i]) >= 65 and ord(list[i]) <= 90:
        A.push(x)
    if ord(list[i]) >= 97 and ord(list[i]) <= 122:
        A.push(x)
    if ord(list[i]) >= 58 and ord(list[i]) <= 64:
        D.push(x)
    if ord(list[i]) >= 91 and ord(list[i]) <= 96:
        D.push(x)
    if ord(list[i]) >= 123 and ord(list[i]) <= 127:
        D.push(x)
    if ord(list[i]) >= 65 and ord(list[i]) <= 90:
        C.push(x)
    if ord(list[i]) >= 97 and ord(list[i]) <= 122:
        C.push(x)

print('')
print("Задние №6")
print(B.items + C.items + D.items)


print('')
print('Задание №7')

numbers = [1,4,23,-1,-7,52,-7,-1,2, 3]
l = []
Zad_7 = Deque()
for i in numbers:
    if i>0:
        Zad_7.pushFront(i)
        continue
    l.append(i)

x = Zad_7.peekBack()
while Zad_7.size() != 0:
    l.append(Zad_7.popBack())
    x = Zad_7.peekBack()
print(l)

print()
print("Задание №8")
A = Stack()
B = Stack()
C = Stack()

del list

str1 = "pog loki"
list = list(str1)

z = 0

for i in range(len(list)):
    A.push(list[i])

while z == 0:
    for i in range(len(A.items)):
        x = A.pop()
        if x == " ":
            break
        B.push(x)

    for i in range(len(B.items)):
        x = B.pop()
        C.push(x)

    if A.items == []:
        z = 1
        continue

    C.push(" ")

print(C.show_elements())

print()
print("Задание №9")
# задание 9
def computeLogic (str):
    str1=""
    stk= Stack()
    for i in range (len(str)):
        stk.push(str[i])
    for i in range (len(str)):
        if(stk.peek()=="T"):
            str1 +="True "
        if(stk.peek()=="F"):
            str1+="False "
        if(stk.peek()=="N"):
            str1 += "Not is "
        if(stk.peek()=="A" or stk.peek()=="*"):
            str1+="and "
        if(stk.peek()=="X"):
            str1="!= " +str1
        if(stk.peek()=="O" or stk.peek()=="+"):
            str1+="or "
        if(stk.peek()=="("):
            str1+="( "
        if(stk.peek()==")"):
            str1+=")"
        stk.pop()
    print(eval(str1))
computeLogic("TAF")

print()
print("Задание №10")
# задание 10
def computeMinMax(str):
    str1=""
    stk= Stack()
    for i in range (len(str)-1, -1, -1):
        stk.push(str[i])
    for i in range(len(str)):
        if(stk.peek()=="0"):
            str1+="0"
        if(stk.peek()=="1"):
            str1+="1"
        if(stk.peek()=="2"):
            str1+="2"
        if(stk.peek()=="3"):
            str1+="3"
        if(stk.peek()=="4"):
            str1+="4"
        if(stk.peek()=="5"):
            str1+="5"
        if(stk.peek()=="6"):
            str1+="6"
        if(stk.peek()=="7"):
            str1+="7"
        if(stk.peek()=="8"):
            str1+="8"
        if(stk.peek()=="9"):
            str1+="9"
        if(stk.peek()=="M"):
            str1+="max"
        if(stk.peek()=="N"):
            str1+="min"
        if(stk.peek()==","or stk.peek()=="."):
            str1+=","
        if(stk.peek()=="("):
            str1+="("
        if(stk.peek()==")"):
            str1+=")"
        stk.pop()
    print(eval(str1))
computeMinMax("N(3,5)")


print()
print("Задание №11")
# задание 11
def computeForm(str):
    x=1
    y=1
    z=1
    stk= Stack()
    str1=""
    for i in range(len(str) - 1, -1, -1):
        stk.push(str[i])
    for i in range(len(str)):
        str1+=stk.pop()
    try:
        eval(str1)
    except:
        print("False")
        return
    print("True")
computeForm("2 +(3+)")

