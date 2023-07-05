import re
num=0
with open('source.txt','r+') as f:
    source=f.read()

lista=re.split('[0-9]{1,2}\.',source)
# print(lista)
# len(lista)
with open('out.txt','w+') as f:
    for item in lista:
        # item=item.replace('\n','')
        f.write('```\n'+str(num)+'.'+item+'\n```\n\n')
        num+=1
