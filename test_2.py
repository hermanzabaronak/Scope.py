list = [1,1,2,2,3,4,4,5,5,6,7,7,8]
counter = 0
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
            counter +=1
print(counter)