#!coding=utf-8

import re
import requests
import json


#相对url转绝对url，假定将从网页中提取的不是http开头的，全部替换成从Index_Url中的第一个/前面部分+网页中提取到的部分					
#将穿进来的url统一转换成list返回
def Relative_to_Absolute(index_url,url_tail,site_name):
	if site_name == "letv_show":
		res_urls = []
		for i in url_tail:
			res_urls.append("http://www.le.com/zongyi/{aid}.html".format(aid=i))
		return res_urls
	elif site_name == "letv_sp":
		res_urls = []
		for i in url_tail:
			res_urls.append("http://www.le.com/zongyi/{aid}.html".format(aid=i))
		return res_urls
	else:
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

def Relative_to_Absolute2(index_url,url_tail,site_name):
	if site_name == "mangguo_sp":
		res_urls = []
		target_url = "http://pcweb.api.mgtv.com/variety/showlist?collection_id={data_id}&month={time_id}"
		data_id = re.search('(?<=/b/)\d+',index_url).group()
		for i in url_tail:
				res_urls.append(target_url.format(data_id=data_id,time_id=i))
		return res_urls
	elif site_name == "souhu_sp":
		res_urls = []
		target_url = "http://tv.sohu.com/item/VideoServlet?source=sohu&id={id}&year=2016&month=0"
		for i in url_tail:
				res_urls.append(target_url.format(id=i))
		return res_urls
	else:
		return url_tail
	#乐视综艺不再使用这个接口 (按照月份和综艺id) 传递数据，将其注释掉
	"""
	elif site_name == "letv_sp":
		res_urls = []
		target_url = "http://api.le.com/mms/out/albumInfo/getVideoListByIdAndDate?&year=2016&type=1&month={month}&id={data_id}"
		data_id = re.search('\d+',index_url).group()
		for i in url_tail:
				res_urls.append(target_url.format(month=i,data_id=data_id))
		return res_urls
	"""


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
	if spider_name == "youku_show":
			return re.sub(r"\d.html","{page}.html",index_url)
	if spider_name == "mangguo_show":
			return re.sub(r"\d-0--.html","{page}-0--.html",index_url)
	if spider_name == "mangguo_sp":
			return re.sub(r"\d-0--.html","{page}-0--.html",index_url)
	if spider_name == "souhu_show":
			return re.sub(r"\d_p11_p12_p13.html","{page}_p11_p12_p13.html",index_url)
	else:
			return re.sub("(\d+)$","{page}",index_url)
	












