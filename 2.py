# Задайте натуральное число N. 
# Напишите программу, которая составит 
# список простых множителей числа N.

N=int(input('Введите число N - '))
quotient=N
resultList=[]
factor=2
while quotient>1:
    if quotient%factor>0:
        factor+=1
        print (factor)
    else:
        resultList.append(factor)
        quotient=quotient/factor
print(resultList)   
