# coding:utf-8
import requests
import re
header = {
    # 'Host': 'www.mmjpg.com ',
    # 'Connection': 'Keep - Alive',
    #'Referer': 'http://www.mmjpg.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3302.400 QQBrowser/9.6.11768.400'
}

def fan_ye(html,chu_shi=1,pan_duan=None):
	p = re.compile(r'src="(.*?)" alt="(.*?)".*?<span class="view">(.*?)<')
	l = p.findall(html)
	if l!=pan_duan:
		p = re.compile(r'src="(.*?)".*?alt="(.*?)".*?<span class="view">(.*?)<')
		#print(html.text)
		for m in p.finditer(html):
		    biao_ti = m.group(1)
		    URL = m.group(2)
		    liu_lan = m.group(3)
		    print(biao_ti+'\t'+URL+'\t'+liu_lan)
		chu_shi+=1
		pan_duan = l
		url = "http://www.mmjpg.com/home/"+str(chu_shi)
		html = requests.get(url, headers = header)
		html.encoding = 'utf-8'
		fan_ye(html.text,chu_shi,pan_duan)


url = "http://www.mmjpg.com/"
html = requests.get(url, headers = header)
html.encoding = 'utf-8'
fan_ye(html.text)
