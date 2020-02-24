#-*- encoding:utf-8 -*-
import hashlib
import bsddb3
import os
import simhash
from common import URL

class Urlfilter():
    def filter(self, url_list):
        url_list = self.filter_by_hash(url_list)
        #去相识url，算法和冒泡排序原理类似
        l = len(url_list)
        for after in range(0, l - 1):
            for before in range(after + 1, l - 1):
                if(self.is_similar_url(url_list[before], url_list[after])):
                    del url_list[after]
                    l = l - 1
        return url_list

    #计算hash值，hash去重
    def md5_16(self, str):
        return hashlib.md5(str.encode()).hexdigest()[8:-8]

    #通过Berkeley DB数据库进行hash去重
    def filter_by_hash(self, url_list):
        new_list = []
        if(os.path.exists("lib/utils/webscan/crawl/urlfilter.db")):
	        os.remove("lib/utils/webscan/crawl/urlfilter.db")
        db = bsddb3.hashopen("lib/utils/webscan/crawl/urlfilter.db", 'c')
        #通过键值对存入，如果存在重复，则相当于重新赋值，而不会增多
        for url in url_list:
            #必须转成bytes型
            key = bytes(self.md5_16(url), 'utf-8')
            db[key] = url
        for i in db:
            #转回str型，并返回成list
            new_list.append(str(db[i], encoding='utf-8'))
        db.close()
        return new_list

    #判断2个list是否健相同
    def is_contain_list(self, a_list, b_list):
        if not isinstance(a_list,list) or not isinstance(b_list,list):
            return False

        a_len = len(a_list)
        b_len = len(b_list)

        if a_len != b_len:
            return False

        if a_len >= b_len:
            temp   = a_list
            a_list = b_list
            b_list = temp

        a_len_real = len(a_list)
        b_len_real = len(b_list)        

        #判断两个List是否相同或包含
        count = 0
        for a in a_list:
            if a in b_list:
                count = count + 1
        
        if count == a_len_real and count<=b_len_real:
            return True
        else:
            return False

    #去掉参数值不同的url
    def is_similar_url(self,url1,url2):
        url1 = URL.URL(url1)
        url2 = URL.URL(url2)
        #获取协议
        protocol1 = url1.get_scheme()
        protocol2 = url2.get_scheme()
        #获取host
        host1 = url1.get_host()
        host2 = url2.get_host()
        #获取端口
        port1 = url1.get_port()
        port2 = url2.get_port()
        #获取路径
        path1 = url1.get_path()
        path2 = url2.get_path()
        #获取参数
        key1 = url1.get_key()
        key2 = url2.get_key()
        if(protocol1 == protocol2 and host1 == host2 and port1 == port2 and path1 == path2 and self.is_contain_list(key1,key2)):
            return True
        else:
            return False
'''
    #判断2个页面是否相似
    def is_similar_page(self, res1,res2,radio=0.85):
        if res1 is None or res2 is None:
            return False

        body1 = res1.text
        body2 = res2.text

        simhash1 = simhash.Simhash(body1.split())
        simhash2 = simhash.Simhash(body2.split()) 

        calc_radio = simhash1.similarity(simhash2)
        #print "[%s]与[%s]两个页面的相似度为:%s" % (url1,url2,calc_radio)
        if calc_radio > radio:
            return True
        else:
            return False
'''