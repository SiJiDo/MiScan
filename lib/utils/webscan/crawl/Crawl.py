import threading
from lib.utils.webscan.crawl import SpiderThread
from common import URL

class Crawl(threading.Thread):
    def __init__(self, url_queue, seen_queue):
        threading.Thread.__init__(self)
        #初始化队列和参数
        self.url_queue = url_queue
        self.seen = seen_queue
        self.spiderThread = SpiderThread.SpiderThread()

    def run(self):
        url_queue = self.url_queue
        #判断是否爬取完毕
        while not url_queue.empty():
            #获取当前url对象
            current_url = url_queue.get()
            #获取当前url中的新的url
            new_urls = self.get_new_url(current_url)
            #去重
            try:
                for next_url in new_urls:
                    #if(self.is_similar_url(new_urls)):
                    next_url = URL.URL(next_url)
                    url_queue.put(next_url)
            except:
                pass

    #获取页面中心的url
    def get_new_url(self,url):
        return self.spiderThread.get_url(url)
    #url去重
    def is_similar_url(self, url):
        pass

    