##задача№ 1
##print("введите размер списка")
##n=int(input())
##lst=[]
##for i in range(n):
##    print("введите число", end=" ")
##    x=int(input())
##    lst.append(x)
##for i in range(n):
##    if lst[i]%2==0:
##        print(lst[i], end=" ")
##Задача № 2
##print("введите размер списка")
##n=int(input())
##lst=[]
##for i in range(n):
##    print("введите число", end=" ")
##    x=int(input())
##    lst.append(x)
##for i in range(n):
##    if i%2==0:
##        print(lst[i], end=" ")
##Задача№ 1
##print("введите размер списка")
##n=int(input())
##lst=[]
##S=0
##for i in range (n):
##    print("введите число", end=" ")
##    x=int(input())
##    lst.append(x)
##    S+=lst[i]   
##print(S)
##Задача№ 2
##print("введите размер списка")
##n=int(input())
##lst=[]
##P=1
##for i in range (n):
##    print("введите число", end=" ")
##    x=int(input())
##    lst.append(x)
##    P*=lst[i]   
##print(P)    
####Задача№ 3
##print("введите размер списка")
##n=int(input())
##lst=[]
##S=0
##ar=0
##for i in range (n):
##    print("введите число", end=" ")
##    x=int(input())
##    lst.append(x)
##    S+=lst[i]
##    ar=S/n
##print(ar)
##Задача№ 4
##import math
##print("введите размер списка")
##n=int(input())
##lst=[]
##P=1
##geo=0
##for i in range (n):
##    print("введите число", end=" ")
##    x=int(input())
##    lst.append(x)
##    P*=lst[i]
##    geo=math.sqrt(P)
##print(geo)
###Задача № 5
##print("введите размер списка")
##n=int(input())
##lst=[]
##p=0
##for i in range(n):
##    print("введите число", end=" ")
##    x=int(input())
##    lst.append(x)
##for i in range(n):
##    if lst[i]%3==0 and lst[i]%5!=0:
##        p+=1
##print(p)
##Array 1.Дано целое число N (> 0). Сформировать и вывести целочисленный
##массив размера N, содержащий N первых положительных нечетных чисел:
##1, 3, 5, . . . .
##print("введите размер списка")
##n=int(input())
##lst=[1]
##x=1
##for i in range(n):
##    x+=2
##    lst.append(x)
##print(lst)
##Array2. Дано целое число N (> 0). Сформировать и вывести целочисленный
##массив размера N, содержащий степени двойки от первой до N-й: 2, 4,
##8, 16, . . . .
##print("введите размер списка")
##n=int(input())
##lst=[2]
##x=2
##for i in range(n):
##    x*=2
##    lst.append(x)
##print(lst)
##Array3. Дано целое число N (> 1), а также первый член A и разность D арифметической прогрессии. Сформировать и вывести массив размера N, содержащий N первых членов данной прогрессии:
##A, A + D, A + 2·D, A + 3·D, . . . .
##print("введите размер списка")
##n=int(input())
##lst=[]
##print("ввведите две переменные")
##A=int(input())
##D=int(input())
##for i in range(n):
##     lst.append(A+i*D)
##print(lst)
##Array4. Дано целое число N (> 1), а также первый член A и знаменатель D
##геометрической прогрессии. Сформировать и вывести массив размера N,
##содержащий N первых членов данной прогрессии:
##A, A·D, A·D2, A·D3
print("введите размер списка")
n=int(input())
print("ввведите две переменные")
A=int(input())
D=int(input())
lst=[]
for i in range(n):
    lst.append(A*D**i)
print(lst)
    
    
