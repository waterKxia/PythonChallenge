#coding:utf-8

from bs4 import BeautifulSoup
import requests
import string

str_l = [word for word in string.lowercase]
str_u = [word for word in string.uppercase]
str_sum = str_l + str_u
url = "http://www.pythonchallenge.com/pc/def/map.html"
def spider(url):
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html,'html.parser')
	data = soup.find('font',color='#f000f0').get_text()
	print "miwen:" + data
	return data

def jiemi(data,str_sum):
	text = ''
	for d in data:
		if d in str_sum:
			if d == 'y':
				text += 'a'
			elif d == 'z':
				text += 'b'
			else:
				text += chr(ord(d)+2)
		else:
			text += d
	print text

if __name__ == '__main__':
	data = spider(url)
	jiemi(data,str_sum)
