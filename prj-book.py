persons=[]
dic={}

def print_menu():
    print('\n1.create person\n'
          '2.delete person\n'
          '3.query person\n'
          '4.list all persons\n'
          '5.save as file\n'
          '6.input from file\n'
          '7.quit\n')


def create_person():
    name=input('请输入姓名:')
    add=input('请输入地址:')
    tel=input('请输入手机号:')
    dic={'name':name,'address':add,'tel':tel}#在此更改信息种类及数目
    persons.append(dic)
    print(persons)


def delete_person():
    name=input('请输入要删除的联系人的姓名:')
    i=0
    for item in persons:
        i+=1
        if name in item['name']:
            del persons[i-1]
            print(persons)
        else:
            print('查无此人')

def query_person():
    name=input('请输入要查询的联系人的姓名:')
    for item in persons:
        if name in item['name']:
            print('联系人信息如下')
            print('联系人的姓名是%s,地址是%s,手机号是%s' % (item['name'],item['add'],item['tel']))
        else:
            print('查无此人')

def list_all_persons():
    print('姓名 地址 手机号')
    for item in persons:
        print(item['name'],item['add'],item['tel'])

def save_as_file():
    with open('./prj.txt','w',encoding='utf-8') as f:
        for item in persons:
            f.write(str(item['name'])+' '+str(item['add'])+' '+str(item['tel'])+'\n')

def input_from_file():
    with open("./prj.txt", 'r', encoding='utf-8') as infile:#在此更改导入文件名
        data=[]
        for line in infile:
            data_line = line.strip("\n").split()
            for i in data_line:
                data.append(i)
            name=data[0]
            add=data[1]
            tel=data[2]
            dic={'name':name,'address':add,'tel':tel}
            persons.append(dic)
            data=[]
    print("Succeeded!")



while True:
    print_menu()
    choice=int(input('Enter a number(1-7):'))
    if choice==1:
        create_person()
    elif choice==2:
        delete_person()
    elif choice==3:
        query_person()
    elif choice==4:
        list_all_persons()
    elif choice==5:
        save_as_file()
    elif choice==6:
        input_from_file()
    elif choice==7:
        break
    else:
        print('无效选项')