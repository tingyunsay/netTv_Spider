#!coding=utf-8

#这个文件：分离出所有需要计算站点实际page页面的木块，一个可扩展的if elif语句来实现

def Total_page_circulate(site_name,max_pages):
	if site_name == "xiami_music":
			return (max_pages/24)+1
	if site_name == "xiami_album":
			return (max_pages/24)+1
	if site_name == "xiami_mv":
			return (max_pages/24)+1
	if site_name == "letv":
			return (max_pages/30)+1
	if site_name == "tudou":
			return (max_pages/40)+1
	else:
			return max_pages


def Turn_True_Page(i,site_name):
	if site_name == "tencent_show":
			return (i - 1)*30
	else:
			return i



def Total_page_circulate2(site_name,max_pages):
	if site_name == "letv":
			return (max_pages/14)+1
	else:
			return max_pages







