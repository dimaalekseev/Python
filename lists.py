import copy

# arr = [1, 42, 30, 7]
# print(arr)

# arr.append(28)  # додати в кінець
# print(arr)

# arr.insert(1, 100500)  # Вставити на місце заданого індекса
# print(arr)

# arr.remove(100500)
# print(arr)

# arr.clear()  # Видалити все
# print(arr)

# arr.append(4)
# arr.append(8)
# arr.append(12)
# arr.append(8)
# arr.append(20)
# print(arr)
# print(arr.index(12))  # дізнаємось індекс елемента

# arr.pop(2)
# print(arr)

# print(arr.count(8))

# arr.append(6)
# print(arr)

# arr.sort()
# print(arr)

# arr.reverse()
# print(arr)

# print(len(arr))

# print("Мінімальне значення масиву:", min(arr))
# print("Максимальне значення масиву:", max(arr))
# print("------------------------")
# for item in arr:
#     print(item)


# print("------------------------")
# names = ["Jane", "Alice", "Mark", "Bob", "Marta"]
# names.sort()
# for item in names:
#     print(item)

# print("------------------------")
# names1 = ["Jane", "Alice", "Mark", "Bob", "Marta"]
# # names2=names1
# names2 = copy.deepcopy(names1)
# print("names1", names1)
# print("names2", names2)
# names3 = names1[3:5]
# print("names3", names3)


#---------------------------------------Домашня робота---------------------------------------------#

# 1 Дано одновимірний масив. Знайти найбільший та найменший елементи масиву та поміняти їх у масиві місцями.
# arr = [10, 12, 8, 18, 15, 9, 36]
# print(arr)
# min_value = min(arr)
# max_value = max(arr)

# print("Мінімальне значення:", min_value)
# print("Максимальне значення:", max_value)

# min_index = arr.index(min_value)
# print("Індекс мінімального елемента:", min_index)
# max_index = arr.index(max_value)
# print("Індекс максимального елемента:", max_index)

# # міняємо місцями
# temp = arr[min_index]
# arr[min_index] = arr[max_index]
# arr[max_index] = temp

# print("New Array:", arr)


# 2 Дано одновимірний масив. Знайти суму елементів з непарними індексами.
# arr = [10, 12, 8, 18, 15, 9, 36]
# sum = 0

# for item in range(1, len(arr), 2):
#     sum += arr[item]
#     #print(arr[item])
# print("Сума непарних елементів списку:", sum)

# 2-й спосіб
# sum(arr[1::2])
# print("Сума елементів:", sum(arr[1::2]))


# 3 Дано список. Поміняти місцями перший елемент з другим, третій з четвертим, і т.д. Вивести змінений масив на екран
# arr = [10, 12, 8, 18, 15, 9, 36]
# print(arr)
# for item in range(1, len(arr), 2):
#     temp=arr[item-1]
#     arr[item-1]=arr[item]
#     arr[item]=temp


# #або
# for item in range(0, len(arr), 2):
#     temp=arr[item]
#     arr[item]=arr[item+1]
#     arr[item+1]=temp

# #або
# arr[item-1], arr[item] = arr[item], arr[item-1]
# print(arr)


# 4 Дано список(А) із К елементів (К- парне число). Утворити 2 списки(В і С), переписуючи у списку В першу половину масиву А, у список С – другу половину масиву А
a = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
b=[]
c=[]

for x in a[:int(len(a)/2)]:
    b.append(x)

for y in a[int(len(a)/2):]:
    c.append(y)

print('B=', b)
print('C=', c)

#2й спосiб
# b=copy.deepcopy(a[:int(len(a)/2)])
# c=copy.deepcopy(a[int(len(a)/2):])
# print('B=', b)
# print('C=', c)



