# -*- encoding:utf8 -*-
import re
import requests
import time
# 爬取斗破苍穹全文小说，保存到txt文档中
 
# 请求头
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
# 新建txt文档，a+表示追加的方式
f = open(r"C:/Users/win10/Desktop/doupocangqing.txt","a+")
 
# 定义获取信息的函数
def get_info(url):
    res = requests.get(url,headers=headers)
    # 判断请求码是否为200
    if res.status_code == 200:
        # re.S多行匹配，包含换行在内的所有字符,这里获取的是一章的所有段落,返回的是一个列表
        contents = re.findall("<p>(.*?)</p>",res.content.decode('utf-8'),re.S)
        for content in contents:
            f.write(content+"\n")
    else:
        # 若请求码不为200，则表示没有获取到数据，不做处理
        pass
 
# 程序的入口
if __name__ == "__main__":
    # 创建url
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2,1665)]
    for url in urls:
        get_info(url)
        # 休眠1秒，这里无所谓，小网址没有防爬
        time.sleep(1)
    # 关闭txt文件
    f.close()
    pass
