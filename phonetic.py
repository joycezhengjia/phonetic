import requests
from bs4 import BeautifulSoup
import random
def read( word ):
    # word = input('請輸入中文字:')
    url = f'https://dict.idioms.moe.edu.tw/idiomList.jsp?idiom={word}&qMd=0&qTp=1&qTp=2'
    print(url)
    user_agent = {'User-agent': 'Mozilla/5.0'}
    html = requests.get(url, headers=user_agent)
    bs = BeautifulSoup(html.text, 'html')
    try:
        data = bs.find_all('td', headers='thVal')
        word = random.choice( data )
        return ( word.div.a.text )
    except:
        return ('查無此字')
