#-*- encoding:utf-8 -*-
import time
import queue
import sys
sys.path.append('../')

from lib.utils.webscan.crawl import Crawl
from lib.utils.webscan.crawl import Urlfilter 
from common import URL

MAX = 100

def portscan(host, thread_count):
    pass

#传入的url参数是URL对象
def webscan(host, thread_count, cookies = ""):
    target = URL.URL(host)
    url_queue = queue.Queue(MAX)
    seen_queue = queue.Queue()
    url_queue.put(target)
    threads = []
    for i in range(0, thread_count + 1):
        thread = Crawl.Crawl(url_queue, seen_queue)
        time.sleep(2)
        print("[+]Thread-{} start".format(i))
        thread.start()
        threads.append(thread)

    for j in threads:
        threads[j].join()

def url_filter_test():
    url_list = [
        'http://mi0.xyz/4.php?id=1&name=2',
        'http://mi0.xyz/4.php?id=2&name=3',
        'http://mi0.xyz/1.php',
        'http://mi0.xyz/2.php',
        'http://mi0.xyz/3.php',
        'http://mi0.xyz/4.php',
        'http://mi0.xyz/1.php',
        'http://mi0.xyz/2.php',
        'http://mi0.xyz/2.php',
        'http://mi0.xyz/3.php',
        'http://mi0.xyz/4.php?test=2'
    ]
    urlfilter = Urlfilter.Urlfilter()
    result = urlfilter.filter(url_list)
    for i in result:
        print(i)