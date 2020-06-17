import requests
from bs4 import BeautifulSoup

class Ciyu:
    cookie = {
        'Cookie': 'BAIDUID=0E3093F274C1C37254EE37DBE72BCCDB:FG=1; BIDUPSID=0E3093F274C1C37254EE37DBE72BCCDB; PSTM=1566719896; __cfduid=de5cd75c77d552abb70f17c6dfa883cab1574397488; BAIDU_WISE_UID=wapp_1585362557088_970; BDUSS=VFpbnV2RUptMzRZaTVpYzNWZjktLW1icnA0TVpsRkV3amhFOXRHU3JpTldzflJlSVFBQUFBJCQAAAAAAAAAAAEAAABvkC1BtcLC6s730ceyu9f3y8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFYmzV5WJs1eV; cflag=13%3A3; Hm_lvt_010e9ef9290225e88b64ebf20166c8c4=1592362681; Hm_lpvt_010e9ef9290225e88b64ebf20166c8c4=1592362745'
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }

    def __init__(self,ci):
        self.ci = ci

    def get_url(self):
        url = 'https://dict.baidu.com/s?wd='+self.ci+'&device=pc&from=home#basicmean'
        return url

    def url_parser(self):
        response = requests.get(self.get_url(),headers=self.header,cookies = self.cookie)
        soup = BeautifulSoup(response.content,'html.parser')
        print(soup)
        try:
            means = soup.find('div',{'class','tab-content'}).find_all('dd')
            self.flag = 0
        except Exception as e:
            means = soup.find('div',{'class','poem-list-item-body check-red'})
            self.flag = 1
        self.means = means

    def data_wash(self):
        data = []
        if self.flag == 1:
            data.append(self.means.text.strip())
        else:
            for mean in self.means:
                me = mean.find_all('p')
                for m in me:
                    data.append(m.text.strip())
        self.data = data
        #print(data)

    def work(self):
        self.url_parser()
        self.data_wash()

if __name__ == '__main__':
    cc = Ciyu('地')
    cc.work()
