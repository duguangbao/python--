import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0'}
res = requests.get("http://bj.xiaozhu.com/chaoyang-duanzufang-8/",headers = headers)
soup = BeautifulSoup(res.text,'lxml')
prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')
for p in prices:
    print(p.get_text())


