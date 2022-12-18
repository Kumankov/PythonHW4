# Задайте последовательность чисел. 
# Напишите программу, которая выведет 
# список неповторяющихся элементов 
# исходной последовательности.

# map(int, input("Введите числа через пробел: ").split("\n")))
print('Введите числа для задачи разделённые пробелом')
inputList=input().split()
outputList =[]
for i in range(len(inputList)):
    if inputList[i] not in outputList:
        outputList.append(inputList[i])
print(outputList)
