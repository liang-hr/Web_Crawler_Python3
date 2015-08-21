import re
# import sys
import requests
from bs4 import BeautifulSoup

# url = 'http://movie.douban.com/'
# request = requests.get(url)
# data = request.text
# soup = BeautifulSoup(data, 'html.parser')


# count = 0
# def get_info_single(tag_name, attrs):
# 	soup = BeautifulSoup(data, 'html.parser')
# 	global count
# 	count += 1
# 	r = soup.find_all(tag_name, attrs)
# 	s = set()
# 	for i in r:
# 		print(str(count),i.text)
# 		s.add(i.text)
# 	return s

def get_info(data):
	def get_info_single(tag_name, attrs):
		# soup = BeautifulSoup(data, 'html.parser')
		# global count
		# count += 1
		r = soup.find_all(tag_name, attrs)
		s = set()
		for i in r:
			# print(str(count),i.text)
			s.add(i.text)
		return s
		
	# 创建存储影片信息的dict
	info = {}

	soup = BeautifulSoup(data, 'html.parser')

	# 如果不是电影页面，返回null
	r = soup.find_all('span', {'property': 'v:itemreviewed'})
	if len(r) is 0:
		return info

	# 抓取电影分数
	info['score'] = get_info_single('strong', {'property': 'v:average'})
	
	# 抓取电影名称
	info['name'] = get_info_single('span', {'property': 'v:itemreviewed'})
	
	# 抓取主演
	info['starring'] = get_info_single('a', {'rel': 'v:starring'})
	
	# 抓取上映日期
	info['release_date'] = get_info_single('span', {'property': 'v:initialReleaseDate'})
	
	# 抓取导演
	info['director'] = get_info_single('a', {'rel': 'v:directedBy'})
	
	# 抓取电影年份
	r = soup.find('span', {'class': 'year'})
	i = r.text[1:-1]
	# print('6',i)
	info['release_year'] = i
	
	# 抓取制片国家/地区
	link_regex = re.compile('制片国家\/地区:<\/span>\s*(.+?)\s*<br')
	r = link_regex.findall(data)[0]
	r_list = r.split('/')
	s = set()
	for i in r_list:
		i = i.strip()
		# print('7',i)
		s.add(i)
	info['producing_countries'] = s

	# print(info)
	return info

# get_info(data)