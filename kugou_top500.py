import requests
from bs4 import BeautifulSoup
import time
headers = {'User-Agent':'Mozilla/5.0'}
def get_info(url):
	wb_data = requests.get(url,headers=headers)
	soup = BeautifulSoup(wb_data.text,'lxml')
	ranks = soup.select('span.pc_temp_num')
	titles = soup.select('div.pc_temp_songlist > ul > li > a')
	times = soup.select('span.pc_temp_tips_r > span')
	for rank, title, time in zip(ranks, titles, times):
		data = {
			'rank': rank.get_text().strip(),
			'title': title.get_text().strip(),
			'time': time.get_text().strip()
		}
		print(data)

#get_info('http://www.kugou.com/yy/rank/home/1-8888.html')
if __name__ == '__main__':
    
    for i in range(1,5):
        urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(i)]
        for url in urls:
            get_info(url)
            time.sleep(1)
