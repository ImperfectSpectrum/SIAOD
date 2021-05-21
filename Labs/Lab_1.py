from random import randint
import random
import time
import copy

xstr = input("Введите x: ")
ystr = input("Введите y: ")

if xstr == "":
    x = 50
else:
    x = int(xstr)

if ystr == "":
    y = 50
else:
    y = int(ystr)

minstr = input("Введите min: ")
maxstr = input("Введите max: ")

if minstr == "":
    min = -250
else:
    min = int(minstr)

if maxstr == "":
    max = 1021
else:
    max = int(maxstr)

print()
print("Результат: ")

mass = []

for i in range(y):
    mass2 = []
    for j in range(x):
        mass2.append(randint(min, max))
    print(mass2)
    mass.append(mass2)
    
def sel_sort(array):
    for i in range(len(array)):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]
    print(array)


print("Результат сортировки выбором: ")

start_time = time.time()

for j in range(y):
    arr = []
    for i in range(x):
        arr.append(mass[j][i])
    sel_sort(arr)

print("Потраченное время(c): ")
sec1 = float('{:.8f}'.format(time.time() - start_time))
print(sec1)

def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
    print(nums)


print("Результат сортировки вставкой: ")

start_time = time.time()

for j in range(y):
    arr = []
    for i in range(x):
        arr.append(mass[j][i])
    insertion_sort(arr)

print("Потраченное время(c): ")
sec2 = float('{:.6f}'.format(time.time() - start_time))
print(sec2)

def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
    print(nums)


print("Результат сортировки вставкой: ")

start_time = time.time()

for j in range(y):
    arr = []
    for i in range(x):
        arr.append(mass[j][i])
    insertion_sort(arr)

print("Потраченное время(c): ")
sec2 = float('{:.6f}'.format(time.time() - start_time))
print(sec2)

def shell(mass):
    inc = len(mass) // 2
    while inc:
        for i, el in enumerate(mass):
            while i >= inc and mass[i - inc] > el:
                mass[i] = mass[i - inc]
                i -= inc
            mass[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    print(mass)

    
print("Результат сортировки шелла: ")

start_time = time.time()
       
for j in range(y):
    a = []
    for i in range(x):
        a.append(mass[j][i])
    shell(a)

print("Потраченное время(c): ")
sec4 = float('{:.6f}'.format(time.time() - start_time))
print(sec4)

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


print("Результат быстрой сортировки: ")

start_time = time.time()

fast_sort = []    
    
for j in range(y):
    nums = []
    for i in range(x):
        nums.append(mass[j][i])
    quicksort(nums)
    fast_sort.append(quicksort(nums))

for i in range(y):
    print(fast_sort[i])

print("")
print("Потраченное время(c): ")
sec5 = float('{:.6f}'.format(time.time() - start_time))
print(sec5)

def heapSort(li):
    def downHeap(li, k, n):
        new_elem = li[k]
        while 2 * k + 1 < n:
            child = 2 * k + 1
            if child + 1 < n and li[child] < li[child + 1]:
                child += 1
            if new_elem >= li[child]:
                break
            li[k] = li[child]
            k = child
        li[k] = new_elem

    size = len(li)
    for i in range(size // 2 - 1, -1, -1):
        downHeap(li, i, size)
    for i in range(size - 1, 0, -1):
        temp = li[i]
        li[i] = li[0]
        li[0] = temp
        downHeap(li, 0, i)
    print(li)

    
print("Результат пирамидальной сортировки: ")

start_time = time.time()

pir_sort = []
    
for j in range(y):
    li = []
    for i in range(x):
        li.append(mass[j][i])
    heapSort(li)
    pir_sort.append(quicksort(nums))

print("Потраченное время(c): ")
sec6 = float('{:.6f}'.format(time.time() - start_time))
print(sec6)
