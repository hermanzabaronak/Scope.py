f = open('123.txt', 'r')
content = f.read()
f.close()
content = content.split("\n")
pupils =[]
for line in content:
    line = line.split("")
    pupils.append([line[0],line[1],int(line[2])])
    avg = 0
    print('Less than 3 points')
for p in pupils:
    avg +=int(p[2])
    if p[2]<3:
        print(f'{p[0]}{p[1]}:{p[2]}')
        avg /=len(pupils)
print(f'Average class point is:{avg}')