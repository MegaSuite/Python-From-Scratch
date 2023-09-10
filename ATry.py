import requests

def waifu():
    url = 'https://moe.anosu.top/img'
    pic = requests.get(url)
    print(pic)
    with open('waifu.jpg', 'wb') as f:
        f.write(pic.content)
        f.close()

if __name__ == '__main__':
        waifu()