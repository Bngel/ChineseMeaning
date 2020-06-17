import requests
from bs4 import BeautifulSoup

class Handn:
    cookie = {
        'Cookie': 'BAIDUID=0E3093F274C1C37254EE37DBE72BCCDB:FG=1; BIDUPSID=0E3093F274C1C37254EE37DBE72BCCDB; PSTM=1566719896; __cfduid=de5cd75c77d552abb70f17c6dfa883cab1574397488; BAIDU_WISE_UID=wapp_1585362557088_970; BDUSS=VFpbnV2RUptMzRZaTVpYzNWZjktLW1icnA0TVpsRkV3amhFOXRHU3JpTldzflJlSVFBQUFBJCQAAAAAAAAAAAEAAABvkC1BtcLC6s730ceyu9f3y8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFYmzV5WJs1eV; cflag=13%3A3; Hm_lvt_010e9ef9290225e88b64ebf20166c8c4=1592362681; Hm_lpvt_010e9ef9290225e88b64ebf20166c8c4=1592362745'
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }

    def __init__(self,ciyu):
        self.url = 'https://www.zdic.net/hans/'+ciyu

    def get_info(self):
        response = requests.get(self.url,cookies=self.cookie,headers=self.header)
        soup = BeautifulSoup(response.text,'html.parser')
        data = []
        try:
            tmp = soup.find('div', {'class', 'content definitions jnr'}).find_all('p')
            pinyin = []
            for pin in tmp:
                pi = pin.find('span', {'class', 'dicpy'})
                if pi is not None:
                    pinyin.append(pi.text)
            exp = soup.find('div', {'class', 'content definitions jnr'}).find_all('ol')
            for i in range(len(pinyin)):
                data.append(pinyin[i])
                dt = exp[i].find_all('li')
                cnt = 1
                for d in dt:
                    data.append('('+str(cnt)+')'+d.text)
                    cnt += 1
        except Exception as ex:
            exp = soup.find('div', {'class', 'jnr'}).find_all('p')
            for e in exp:
                data.append(e.text)
        #print(data)
        self.data = data

if __name__ == '__main__':
    hd = Handn('好')
    hd.get_info()