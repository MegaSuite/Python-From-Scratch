with open ("./data.txt") as f:
    data=f.readlines()
a=[int(line.strip()) for line in data]
sum=0
for i in a:
    if i%2!=0:
        sum=sum+i
print(sum)