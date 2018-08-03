import requests,time,re
import pymongo
from lxml import etree

client = pymongo.MongoClient('localhost',27017)
mydb = client['mydb']
musictop = mydb['musictop']

headers = {'User-Agent':'Mozilla/5.0'}

def get_url_music(url):
    html = requests.get(url,headers)
	selector = etree.HTML(html.text)
	music_herfs = selector.xpath('//a[@class="nbg"]/@href')
	for music_herf in music_herfs:
		get_music_info(music_herf)
		
def get_music_info(url):
	html = requests.get(url,headers = headers)
	