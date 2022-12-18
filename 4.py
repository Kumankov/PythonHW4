# Задана натуральная степень k. 
# Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Так как в условии не обозначено количество переменных, 
# а в примере только одна, будет формироваться многочлен с одной переменной
from random import randint
k=int(input('Введите степень многочлена - '))
constantsList=[0]*(k+1)
for i in range(k+1):
    constantsList[i]=randint(-100, 100)
print(constantsList)
polynomial=''  
for i in range(k+1):
    if i==(k-1):
        if constantsList[i]>0:
            polynomial+=('+' + str(constantsList[i]) + '*x ')
        elif constantsList[i]<0:
            polynomial+=(str(constantsList[i]) + '*x ')
        elif constantsList[i]==0:
            polynomial+=('=0')   
    elif i==k:
        if constantsList[i]>0:
            polynomial+=('+' + str(constantsList[i]) + ' = 0')
        elif constantsList[i]<0:
            polynomial+=(str(constantsList[i]) + ' = 0')
        elif constantsList[i]==0:
            polynomial+=('=0')          
    else:            
        if constantsList[i]>0:
            polynomial+=('+' + str(constantsList[i]) + '*x^'+str(k-i) + ' ')
        elif constantsList[i]<0:
            polynomial+=(str(constantsList[i]) + f'*x^'+str(k-i) + ' ')
        elif constantsList[i]==0:
            polynomial+=('')
with open("output.txt", "w") as outputFile:
    outputFile.write(polynomial.lstrip('+'))
