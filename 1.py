# Пользователь вводит число, нужно 
# вывести чило pi с заданной точностью
# (БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)

N=int(input('Введите точность вычисления числа Пи (число знаков после запятой) - '))
if N in [0,1,2]:
    print (round(3.14,N))
else:
    sum =0
    for i in range(10**(N+1)):  
        sum = sum+((-1)**i)/(2*i+1)
    Pi = 4*(sum)    
    print (round(Pi,N))