import requests, os,time

def waifu():
    url = 'https://moe.anosu.top/img'
    pic = requests.get(url)
    with open('waifu.jpg', 'wb') as f:
        f.write(pic.content)
        f.close()

    os.system('waifu.jpg')
    time.sleep(5)
    os.system('taskkill /F /IM PhotosApp.exe')


if __name__ == '__main__':
    while True:
        cho = input('是否继续？(y/n)\n')
        if cho == 'y':
            waifu()
        else:
            break
