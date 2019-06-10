from collections import OrderedDict
from bs4 import BeautifulSoup
import requests


class Horoscope:
    def __init__(self):
        self.d = OrderedDict(
                    {(1,19):10,
                    (2,18):11,
                    (3,20):12,
                    (4,19):1,
                    (5,20):2,
                    (6,20):3,
                    (7,22):4,
                    (8,22):5,
                    (9,22):6,
                    (10,22):7,
                    (11,21):8,
                    (12,21):9})
    
    def get_date(self):
        month = int(input('What month were you born? Please put the number of the month, for example, if you were born in April, you would input 4. '))
        day = int(input('What day were you born? '))
        return (month,day)
    
    def get_sign(self, date):
        for k in self.d.keys():
            if date <= k:
                return self.d[k]
        return self.d[(1,19)]
    
    def get_horoscope(self):
        date = self.get_date()
        sign = str(self.get_sign(date))
        url = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={}'.format(sign)
        response = requests.get(url)
        html = response.content

        soup = BeautifulSoup(html, 'lxml')
        return soup.body.p.text


h = Horoscope()
h.get_horoscope()