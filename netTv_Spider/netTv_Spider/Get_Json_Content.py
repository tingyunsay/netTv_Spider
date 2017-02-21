#!coding=utf-8

import json
import requests

def Get_Json_Content(urls , spider_name):
		if spider_name == "mangguo_sp":
				res_urls = []
				for url in urls:
						json_content = requests.get(url).json()
						for i in json_content['data']['list']:
								res_urls.append(i['url'])
				return res_urls
		elif spider_name == "souhu_sp":
				res_urls = []
				for url in urls:
						json_content = requests.get(url).json()
						for i in json_content['videos']:
								res_urls.append(i['url'])
				return res_urls
		else:
				return urls
		"""
		#乐视网已经废弃这个 （json接口 + js动作) 去获取单期综艺的detail页面，而是直接给出在了网页上，算是简化了难度。这里我们将其注释掉
		elif spider_name == "letv_sp":
				res_urls = []
				target_url = "http://www.le.com/ptv/vplay/{video_id}.html"
				for url in urls:
						json_content = requests.get(url).json()
						try:
								for key in json_content['data']['2016'].keys():
										if json_content['data']['2016'][key]:
												for i in json_content['data']['2016'][key]:
														res_urls.append(target_url.format(video_id=i['id']))
						except Exception,e:
								print Exception,":",e
				return res_urls
		"""

