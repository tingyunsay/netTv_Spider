#!coding=utf-8

import re

#相对url转绝对url，假定将从网页中提取的不是http开头的，全部替换成从Index_Url中的第一个/前面部分+网页中提取到的部分					
#将穿进来的url统一转换成list返回
def Relative_to_Absolute(index_url,url_tail):
	head_url = re.search(r'(.+//).+?/',index_url).group()
	if type(url_tail) is list and len(url_tail) > 0:
		res_urls = []
		if re.search(r'^//',url_tail[0]):
			for url in url_tail:
				res_urls.append(re.sub(r'^//',"http://",url))
			return res_urls
		elif (not re.search(r'^http://',url_tail[0])) and (not re.search(r'^https://',url_tail[0])):
			if re.search(r'^/',url_tail[0]):
				for url in url_tail:
					url = re.sub(r'^/',"",url)
					res_urls.append(head_url + url)
			else:
				for url in url_tail:
					res_urls.append(head_url + url)
			return res_urls
		else:
			return url_tail
	else:
		if (not re.search(r'^http://',''.join(url_tail))) and (not re.search(r'^https://',''.join(url_tail))):
			if re.search(r'^/',''.join(url_tail)):
				return [head_url + re.sub(r'^/',"",''.join(url_tail))]
			else:
				return [head_url + ''.join(url_tail)]
		else:
			return [''.join(url_tail)]

def Get_Valid_Url(urls):
	if type(urls) is list and len(urls) > 1:
		res_urls = []
		if re.search(r'^//',urls[0]):
			for url in urls:
				res_urls.append("https://"+re.sub(r'^//',"",url))
		else:
			res_urls = urls
		return res_urls
	else:
		if re.search(r'^//',''.join(urls)):
			return re.sub(r'^//',"",''.join(urls))
		else:
			return ''.join(urls)
			

def get_HeadUrl(index_url,spider_name):
	if spider_name == "aiqiyi_mv":
			return re.sub(r"30","{page}",index_url)
	if spider_name == "tudou":
			index_url = "http://www.tudou.com/list/albumData.action?tagType=3&firstTagId=12&sort=1&page=1"
			return re.sub("(\d+)$","{page}",index_url)
	else:
			return re.sub("(\d+)$","{page}",index_url)
	











