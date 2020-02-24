#-*- encoding:utf-8 -*-
#获取新的url
from lxml import etree
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import *

import sys
sys.path.append('/Users/mi0/PythonWorkPlace/Miscan/')

from common import URL
from lib.utils.webscan.crawl import Smart_fill
from lib.utils.webscan.crawl import Urlfilter

class SpiderThread:
    URL_HEADERS  = ('location')
    URL_TAGS = ('a', 'img', 'link', 'script', 'iframe', 'frame', 'form', 'object')
    URL_ATTRS = ('href', 'src', 'data', 'action')
    URL_RE = re.compile('(((http|https):/|)/([\w:@\-\./]*?[^ \n\r\t"\'<>]\s)*)', re.U|re.I)
    #不期待的文件后缀
    IGNORE_EXT = ['css','js','jpg','png','gif','pdf','doc','docx']
    
    HEADER = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    }   
    
    def get_url(self, url):
        self.root_url = url
        r = requests.get(url, headers=self.HEADER)
        url_list = []
        if(r.status_code == '404'):
            return "[-]Can't view {} - 404".format(url)
        else:
            print("[+]GET url: {} - response code {}".format(url, r.status_code))
        r.encoding = "utf-8"
        url_list += self.url_from_tags(url, r)
        url_list += self.url_from_header(url, r)
        return url_list
    
    #从header中获取新的url
    def url_from_header(self, url, r):
        text = r.headers
        try:
            location = text[self.URL_HEADERS]
        except:
            location = None
        url_in_header = []
        if(location !=None):
            url_in_header.append(self.check_url(location))
        url_in_header = list(filter(None, url_in_header))
        return url_in_header

    #从标签中获取新的url
    def url_from_tags(self, url, r):
        text = r.text
        url_in_tags = []
        soup =BeautifulSoup(text,'html.parser')
        for tag in self.URL_TAGS:
            for attr in self.URL_ATTRS:
                new_urls = soup.findAll(name=tag,attrs={attr:self.URL_RE})
                for new_url in new_urls:
                    try:
                        url_in_tags.append(self.check_url(new_url[attr]))
                    except:
                        pass
        url_in_tags = list(filter(None, url_in_tags))
        return url_in_tags

    '''
    #将相对路径改为全地址
    def check_url(self, current_url, url):
        full_url = ""
        if(url[url.rfind('.')+1:] in self.IGNORE_EXT):
            return None
        if(current_url.get_domain() not in url):
            if(("http" in url) or ("." in url.split("/")[0])):
                return None
            else:
                full_url = current_url.get_scheme() + "://" + current_url.get_domain() + url
        else:
            full_url = url 
        return full_url
    '''

    #修复url
    def check_url(self, url):
        o = urlparse(url)
        ret = url
        if(o.scheme is "" and o.netloc is ""):
            #print("Fix  Page: " + ret)
            ret = self.root_url.get_scheme() + "://" + self.root_url.get_domain() + o.path + ret
            #保持url的干净,去除拼接后会 出现//的情况
            ret = ret[:8] + ret[8:].replace('//','/')
            o = urlparse(ret)
            #这里不是太完善，但是可以应付一般情况
            if '../' in o.path:
                paths = o.path.split('/')
                for i in range(len(paths)):
                    if paths[i] == '..':
                        paths[i] = ''
                        if paths[i-1]:
                            paths[i-1] = ''
                tmp_path = ''
                for path in paths:
                    if path == '':
                        continue
                    tmp_path = tmp_path + '/' + path
                    ret =ret.replace(o.path,tmp_path)
            #print("FixedPage: " + ret)

        o = URL.URL(ret)       
        #协议处理
        if 'http' not in o.get_scheme():
            #print("Bad  Page：" + ret.encode('ascii'))
            return None
       
        #url合理性检验
        if o.get_scheme() is "" and o.get_domain() is not "":
            #print("Bad  Page: " + ret)
            return None
       
        #域名检验
        if self.root_url.get_domain() not in o.get_domain():
            #print("Bad  Page: " + ret)
            return None
        
        #检查后缀
        if o.get_ext() in self.IGNORE_EXT:
            #print("Bad Page:" + ret)
            return None

        return ret

def test():
   test = SpiderThread()
   for i in test.get_url(URL.URL("http://jwc.ntu.edu.cn/")):
       print(i)

if __name__ == "__main__":
    test()