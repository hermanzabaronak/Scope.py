list = [1,1,1,2,2,3,4,4,5,5,6,7,7,8]
for i in range(len(list)):
    for j in range(len(list)):
        if i !=j and list[i] == list[j]:
            break
    else:
        print(list[i],',', end="")