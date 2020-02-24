#-*- encoding:utf-8 -*-
#author:Mi0
#用于解析url连接
from urllib.parse import *
DEFUALT_ENCODING = "utf-8"

class URL:
    def __init__(self, url, encoding = DEFUALT_ENCODING):
        self.__unicode_url  = None
        self.__changed      = False
        self.__encoding     = encoding
        if(not url.startswith("https://") and not url.startswith("http://")):
            url = "http://" + url
        urlres = urlparse(url)
        #确定协议
        self.scheme = urlres.scheme
        #确定端口
        if(urlres.port == None):
            self.port = 80
        else:
            self.port = urlres.port
        #确定地址
        if(urlres.netloc.find(":") > -1):
            self.netloc = urlres.netloc
        else:
            self.netloc = urlres.netloc + ":" + str(self.port)
        #确定目录
        self.path = urlres.path
        #确定参数
        self.params = urlres.params
        #确定get参数
        self.query = urlres.query
        #确定信息片段
        self.fragment = urlres.fragment


    #获得协议
    def get_scheme(self):
        return self.scheme
    #获得域名
    def get_domain(self):
        return self.netloc.split(":")[0]
    #获得主机名
    def get_host(self):
        return self.netloc.split(":")[0]
    #获得url中的端口
    def get_port(self):
        return self.port
    #获得url中的路径
    def get_path(self):
        return self.path
    #获得url中的信息片段
    def get_fragment(self):
        return self.fragment
    #获得url中的文件名
    def get_filename(self):
        return self.path[self.path.rfind('/')+1:]
    #获得url中的文件扩展名
    def get_ext(self):
        fname = self.get_filename()
        ext = fname[fname.rfind('.')+1:]
        if(ext ==fname):
            return ''
        else:
            return ext
    #获取url中的参数
    def get_query(self):
        return self.query
    #获取url中参数并返回list
    def get_key(self):
        result = parse_qs(self.query)
        return list(result.keys())

    #获取url所对应的完整字符串
    @property
    def url_string(self):
        u_url = self.__unicode_url
        if(not self.__changed or u_url == None):
            data = (self.scheme, self.netloc, self.path, self.params, self.query, self.fragment)
            dataurl = urlunparse(data)
            try:
                u_url = str(dataurl)
            except UnicodeDecodeError:
                u_url = str(dataurl, self.__encoding, 'replace')
            self.__unicode_url = u_url
            self.__changed = True
        return u_url
    #设置直接输出
    def __str__(self):
        return str(self.url_string)
    def __repr__(self):
        return str(self.url_string)

def test():
    url = "http://www.baidu.com/test/index.php?id=2&name=hcx#top"
    u = URL(url)
    print(u.get_key()) 

if __name__ == '__main__':
    test()