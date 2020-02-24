#-*- encoding:utf-8 -*-
import sys
import optparse
from socket import *
from common import Start

#root_url = "http://jwc.ntu.edu.cn/"

def main():
    parser = optparse.OptionParser('usage%porg -m <model> -u <url> -p <port> -c <cookies>')
    parser.add_option('-m', dest = 'model', type = 'string', help = 'specify target model portscan or webscan')
    parser.add_option('-u', dest = 'url', type = 'string', help = 'specify target url')
    parser.add_option('-p', dest = 'port', type = 'string', help = 'specify target port')
    parser.add_option('-c', dest = 'cookies', type = 'string', help = 'specify target cookies')
    parser.add_option('-t', dest = 'thread_count', type = 'int', help = 'specify scan thread')
    (option, args) = parser.parse_args()
    '''
    model = option.model
    host = option.url
    port = option.port
    cookies = option.cookies
    thread_count = option.thread_count
    '''
    model = 'webscan'
    host = "http://jwc.ntu.edu.cn/"
    port = 80
    cookies = ""
    thread_count = None

    #对model参数进行判定
    if(model == None):
        print(parser.usage)
        exit()
    if(model != 'portscan' and model != 'webscan'):
        print("-m 'portscan' or -m 'webscan'")
        exit()
        
    #对线程数进行设置
    if(thread_count == None):
        thread_count = 8

    #对url参数进行拆分
    if(host.startswith("https://")):
        host = host.split("https://")[1].split('/')[0]
    if(host.startswith("http://")):
        host = host.split("http://")[1].split('/')[0]

    #启用端口扫描模块
    if(model == 'portscan'):
        pass
        #portscan(host, thread_count)

    #启用web扫描模块
    if(model == 'webscan'):
        print("[+]webscan model running .....")
        Start.webscan(host, thread_count, cookies)

if __name__ == '__main__':
    main()