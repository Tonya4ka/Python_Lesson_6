# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# lst = [int(i) for i in input("Enter the numbers of the list separated by space: ").split()]
# for i in lst:
#    if lst.count(i) == 1:
#        print(i, end=" ")

list1 = [2, 3, 4, 5, 6, 7, 9, 2, 4, 7, 11]
print(list(filter(lambda x: list1.count(x) == 1, list1)))