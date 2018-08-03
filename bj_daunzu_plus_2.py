from bs4 import BeautifulSoup
import requests
import time
headers = {'User-Agent':'Mzilla/5.0'}
def judgment_sex(class_name):
	if class_name == ['member_icol']:
		return '女'
	else:
		return '男'
def get_links(url):
	wb_data = requests.get(url,headers=headers)
	soup = BeautifulSoup(wb_data.text,'lxml')
	links = soup.select('#page_list > ul > li > a')
	for link in links:
		href = link.get("herf")
		get_info(herf)

def get_info(url):
	wb_data = requests.get(url,headers = headers)
	soup = BeautifulSoup(wb_data.text,'lxml')
	titles = soup.select('div.pho_info > h4')
	addresses = soup.select('span.pr5')
	prices = soup.select('#pricePart > div.day_1 > span')
	#可替换
	imgs = soup.select('#floatRightBox>div.js_box.clearfix>div.member_pic > a > img')
	names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
	sexs = soup.select('#floatRightBox>div.js_box.clearfix>div.member_pic > div')
	#修改
	for title,address,price,img,name,sex in zip(titles,addresses,prices,imgs,names,sexs):
		date = {
                    'tittle':tittle.get_text().strip(),
                    'address':address.get_text().strip(),
                    'price':price.get_text(),
                    'img':img.get('src'),
                    'name':name.get_text(),
                    'sex':judgement_sex(sex.get('class'))
		}
		print(data)

if __name__ == '__main__':
        urls = ['http://bj.xiaozu.com/search-duanzuwang-p{}-0/'.format(number) for number in range(1,5)]
        for url in urls:
                get_links(url)
                time.sleep(2)
		

		
