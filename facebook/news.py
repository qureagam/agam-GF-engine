import requests
from bs4 import BeautifulSoup

class tribute:

    def __init__(self):
        self.link = 'https://timesofindia.indiatimes.com/home/headlines'

    def basics(self):
        self.response = requests.get(self.link)
        if (self.response.status_code ==200):
            self.parse = BeautifulSoup(self.response.content,'lxml')
        else:
            print("server kick the black ass")

    def fecthing_all(self):
        self.divs_bundle = self.parse.find_all(class_='crd_ttl8')
        a = [i.get_text() for i in self.divs_bundle]
        print(a)


if __name__ == '__main__':
    main = tribute()
    main.basics()
    main.fecthing_all()