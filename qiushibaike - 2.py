from lxml import etree
import requests
import os

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

info_lists = []


def info_url(url):
	
	res = requests.get(url,headers=headers)
	selector = etree.HTML(res.text)
	url_infos = selector.xpath('//*[@id="content-left"]/div[@class]')
	for url_info in url_infos:
		id = url_info.xpath('div/a[@target="_blank"]/h2/text()')
		content = url_info.xpath('a[1]/div/span/text()')
		laugh = url_info.xpath('div/span/i[@class="number"]/text()')
		comment = url_info.xpath('div[@class="stats"]/span/a/i/text()')
		info = {
			'id':id,
			'content':content,
			'laugh':laugh,
			'comment':comment
		}
		info_lists.append(info)
			
if __name__ == '__main__':
	urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,30)]
	for url in urls:
		info_url(url)
	for info_list in info_lists:
		f = open(r'C:/Users/win10/Desktop/qiushibaike.txt','a+',errors='ignore')

		#数据结构问题？？？
		try:
			
			f.write(info_list['id'] + '\n')
			f.write(info_list['content'] + '\n')
			f.write(info_list['laugh'] + '\n')
			f.write(info_list['comment'] + '\n\n')
			f.close()
			
		except UnicodeDecodeError:
			pass
			

