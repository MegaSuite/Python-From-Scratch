list0 = [1,3,2,4]
list1 = [11,33,22]

def select_min(a,b,c):
    temp=a[b:c]
    return min(temp)

def sort(list):
    templist=list[:]
    for i in range(len(list)):
        list[i]=select_min(templist,0,3)
        templist.remove(select_min(templist,0,3))
    return list

sort(list0)
print(list0)
sort(list1)
print(list1)

# for i in range(len(list0)):
#     print(list0[i])
# for i in range(len(list1)):
#     print(list1[i])