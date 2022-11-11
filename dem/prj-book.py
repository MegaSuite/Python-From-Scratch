persons=[]
dic={}

def print_menu():
    print('1.create person\n'
          '2.delete person\n'
          '3.query person\n'
          '4.list all persons\n'
          '5.quit\n')


def create_person():
    name=input('请输入姓名:')
    tel=input('请输入手机号:')
    dic={'name':name,'tel':tel}
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
            return '并无此联系人'

def query_person():
    name=input('请输入要查询的联系人的姓名:')
    for item in persons:
        if name in item['name']:
            print('查询到的联系人信息如下')
            print('联系人的姓名是%s,手机号是%s' % (item['name'],item['tel']))
        else:
            print('查无此人')

def list_all_persons():
    print('姓名 手机号')
    for item in persons:
        print(item['name'],item['tel'])


while True:
    print_menu()
    choice=int(input('Enter a number(1-5):'))
    if choice==1:
        create_person()
    elif choice==2:
        delete_person()
    elif choice==3:
        query_person()
    elif choice==4:
        list_all_persons()
    elif choice==5:
        break
    else:
        print('无效选项')