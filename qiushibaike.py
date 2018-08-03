import re
import requests
import os

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

info_lists = []

def judge_sex(class_name):
	if class_name == 'womanIcon':
		return '女'
	else:
		return '男'

def info_url(url):
        
	res = requests.get(url,headers=headers)
	ids = re.findall(r'<h2>(.*?)</h2>',res.text,re.S)
	levels = re.findall(r'<div class="articleGender \D+Icon">(.*?)</div>',res.text,re.S)
	sexs = re.findall(r'<div class="articleGender (.*?)">',res.text,re.S)
	contents = re.findall(r'<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
	laughs = re.findall(r'<span class="stats-vote"><i class="number">(.*?)</i>',res.text,re.S)
	comments = re.findall(r'<i class="number">(.*?)</i>',res.text,re.S)
	for id,level,sex,content,laugh,comment in zip(ids,levels,sexs,contents,laughs,comments):
		info = {
			'id':id,
			'level':level,
			'sex':judge_sex(sex),
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
		
		try:
			
			f.write(info_list['id'] + '\n')
			f.write(info_list['level'] + '\n')
			f.write(info_list['sex'] + '\n')
			f.write(info_list['content'] + '\n')
			f.write(info_list['laugh'] + '\n')
			f.write(info_list['comment'] + '\n\n')
			f.close()
			
		except UnicodeDecodeError:
			pass
			

