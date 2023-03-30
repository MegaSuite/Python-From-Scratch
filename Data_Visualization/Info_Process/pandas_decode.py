import pandas as pd

url='https://www.maigoo.com/news/657640.html'
a=pd.read_html(url)
for i in a:
    table=pd.DataFrame(i)
    table.to_csv('table.csv',encoding='utf-8-sig',index=False)