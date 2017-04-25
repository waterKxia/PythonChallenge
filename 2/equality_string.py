#coding:utf-8

import requests
from bs4 import BeautifulSoup,Comment
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
def spider(url):
	r = requests.get(url,headers=headers)
	html = r.text
	soup = BeautifulSoup(html,'html.parser')
	datas = soup.findAll(text=lambda text:isinstance(text,Comment))[1]
	return datas

if __name__ == '__main__':
	data = spider(url)
	dict1 = {}
	List = []
	for i in data:
		if i in dict1:
			dict1[i]+=1
		else:
			dict1[i]=1

	dict2 = sorted(dict1.iteritems(), key=lambda d:d[1], reverse=True)
	for i in dict2:
		if i[1] == 1:
			List.append(i[0])
	print List
