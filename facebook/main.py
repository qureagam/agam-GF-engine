from bs4 import BeautifulSoup
import requests

def Nested(d):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    url = f'https://www.google.com/search?q={d}'

    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'lxml')

    link = soup.find('cite',class_='tjvcx GvPZzd cHaqb')
    b = link.get_text() if link else 'false'

    title = soup.find('h3',class_='LC20lb MBeuO DKV0Md')
    c = title.get_text() if title else 'Title not found'

    image = soup.find_all('img',class_='XNo5Ab')
    a = image[0].get('src') if image else 'Image not found'

    about = soup.find_all('div',class_='kno-rdesc')
    for i in about:
        fd = i.find('span')
        if fd:
          d = fd.get_text()
        else:
           pass

    
    gg = soup.find('span',class_='hgKElc')
    more = gg.get_text() if gg else ''


    return a, c, b, d , more

# qLRx3b tjvcx GvPZzd cHaqb
