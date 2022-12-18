# Формат вывода
# Выведите список всех людей и их «друзей 
# 2-го уровня» в формате «Человек: Друг1, Друг2, ...».
# Список людей и друзей в каждой строке требуется 
# вывести в алфавитном порядке без повторений.


with open("input3.txt", encoding="utf-8") as inputFile:
    inputList = [row.strip() for row in inputFile]
connectionList=[[]]*len(inputList)
for i in range(len(connectionList)):
    connectionList[i]=inputList[i].split()
peopleList=[]
for j in range(len(connectionList)):
    if connectionList[j][0] not in peopleList:    
        peopleList.append(connectionList[j][0])
for k in range(len(connectionList)):
    if connectionList[k][1] not in peopleList:    
        peopleList.append(connectionList[k][1])
# print(peopleList)
peopConList=[]
tempPeopConList=[]
for l in range(len(peopleList)):
    tempPeopConList.append(peopleList[l])
    for m in range(len(connectionList)):       
        if peopleList[l]==connectionList[m][0] and connectionList[m][1] not in tempPeopConList:
            tempPeopConList.append(connectionList[m][1])
        elif peopleList[l]==connectionList[m][1] and connectionList[m][0] not in tempPeopConList:
            tempPeopConList.append(connectionList[m][0])
    peopConList.append(tempPeopConList)
    tempPeopConList=[]
print(peopConList)    
peopSecConList=[]
for n in range(len(peopleList)):
    for o in range(1,len(peopConList[n])):
        for p in range(len(peopConList)):
            if peopConList[n][o] == peopConList[p][0]:
                for q in range(1,len(peopConList[p])):
                    if peopConList[p][q] not in tempPeopConList and peopConList[p][q] != peopleList[n]:
                        tempPeopConList.append(peopConList[p][q])                
    peopSecConList.append(tempPeopConList)
    tempPeopConList=[] 
for r in range(len(peopSecConList)):
    peopSecConList[r].sort()
result =[]
tempstr =''
for s in range(len(peopleList)):
    tempstr+=str(peopleList[s])+': '
    for t in range(len(peopSecConList[s])):
        if t == len(peopSecConList[s])-1:
            tempstr+=str(peopSecConList[s][t])
        else: 
            tempstr+=str(peopSecConList[s][t])+', '      
    result.append(tempstr)
    tempstr =''    
result.sort()
with open("output2.txt", "w") as outputFile:
    for u in range(len(result)):
        outputFile.write(result[u]+'\n')