import requests
from bs4 import BeautifulSoup as bs

URL_AM  = 'https://www.apkmirror.com/?post_type=app_release&searchtype=apk&s='

def create_link(Link_from_store):
    pack = Link_from_store.partition('id=')[2]
    am_search = URL_AM + pack

    HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.4.3.257 Yowser/2.5 Yptp/1.23 Safari/537.36'
    #'Cache-Control': 'no-cache'
    }

    try:
        r = requests.get(am_search, headers = HEADERS)
        s = bs(r.content, 'html.parser')
        l ='https://www.apkmirror.com' + s.find('a', class_='fontBlack').get('href')

        r = requests.get(l, headers = HEADERS)
        s = bs(r.content, 'html.parser')
        l = 'https://www.apkmirror.com' + s.find('a', class_='btn btn-flat downloadButton').get('href')

        r = requests.get(l, headers = HEADERS)
        s = bs(r.content, 'html.parser')
        l = 'https://www.apkmirror.com' + s.find('a', text='here').get('href')

    except:
        try:
            r = requests.get(am_search, headers = HEADERS)
            s = bs(r.content, 'html.parser')
            l ='https://www.apkmirror.com' + s.find('a', class_='fontBlack').get('href')

            r = requests.get(l, headers = HEADERS)
            s = bs(r.content, 'html.parser')
            l = 'https://www.apkmirror.com' + s.find('div', class_='table-cell rowheight addseparator expand pad dowrap').find('a').get('href')

            r = requests.get(l, headers = HEADERS)
            s = bs(r.content, 'html.parser')
            l = 'https://www.apkmirror.com' + s.find('a', class_='btn btn-flat downloadButton').get('href')

            r = requests.get(l, headers = HEADERS)
            s = bs(r.content, 'html.parser')
            l = 'https://www.apkmirror.com' + s.find('a', text='here').get('href')
        except:
            l = 'Я не смогла найти это приложение'
    return(l)
