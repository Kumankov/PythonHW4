# ДОП Даны два файла, в каждом из которых 
# находится запись многочлена. Задача - сформировать 
# файл, содержащий сумму многочленов.

with open("input1.txt") as inputFile:
    polynomial1 = inputFile.read()
with open("input2.txt") as inputFile:
    polynomial2 = inputFile.read()    
polyList1 = polynomial1.split()
polyList2 = polynomial2.split()
for i in range(len(polyList1)-1,0,-1):
    if polyList1[i]=="=" or polyList1[i]=='0':
        polyList1.pop(i)
for j in range(len(polyList2)-1,0,-1):
    if polyList2[j]=="=" or polyList2[j]=='0':
        polyList2.pop(j)
polyList3=[[]]*len(polyList1)
for k in range(len(polyList1)):
    if '*' not in polyList1[k]:
        polyList3[k]=[polyList1[k],'']
    else:
        polyList3[k]=polyList1[k].split('*')
polyList4=[[]]*len(polyList2)
for l in range(len(polyList2)):
    if '*' not in polyList2[l]:
        polyList4[l]=[polyList2[l],'']
    else:    
        polyList4[l]=polyList2[l].split('*')
resultPolyList=[0]*len(polyList1)
index=[]
for m in range(len(polyList3)):
    resultPolyList[m]=polyList3[m][1]
for n in range(len(polyList4)):
    if polyList4[n][1] not in resultPolyList:
        resultPolyList.append(polyList4[n][1])
        index.append(n)
for o in range(len(polyList3)):
    for p in range(len(polyList4)):
        if polyList3[o][1] == polyList4[p][1]:
            polyList3[o][0]=int(polyList3[o][0])+int(polyList4[p][0])
        else:
            polyList3[o][0]=int(polyList3[o][0])
if len(resultPolyList)!=len(polyList3):
    for q in range(len(polyList4)):
        if q in index:
            polyList5=[int(polyList4[q][0]),polyList4[q][1]]
            polyList3.append(polyList5)    
polynomial=''  
for r in range(len(polyList3)):
    if r==len(polyList3)-1:
        if (polyList3[r][0])>0:
            if polyList3[r][1]=='':
                polynomial+=' +'+str(polyList3[r][0])+" = 0"
            else:
                polynomial+=' +'+str(polyList3[r][0])+"*"+polyList3[r][1]+" = 0"        
        elif polyList3[r][0]<0:          
            if polyList3[r][1]=='':
                polynomial+=' '+str(polyList3[r][0])+" = 0"
            else:
                polynomial+=' '+str(polyList3[r][0])+"*"+polyList3[r][1]+" = 0"
        else:          
            polynomial+=" = 0"
    else:
        if polyList3[r][0]>0:
            if polyList3[r][1]=='':
                polynomial+=' +'+ str(polyList3[r][0])    
            else:    
                polynomial+=' +'+ str(polyList3[r][0])+"*"+polyList3[r][1]
        elif polyList3[r][0]<0:
            if polyList3[r][1]=='':
                polynomial+=' '+str(polyList3[r][0])    
            else:    
                polynomial+=' '+str(polyList3[r][0])+"*"+polyList3[r][1]
        else:
            polynomial+=""
with open("output1.txt", "w") as outputFile:
    outputFile.write(polynomial.lstrip(' +'))

    