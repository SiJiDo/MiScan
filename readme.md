### Miscan 开发记录

#### 开发环境
python3.7
##### 依赖库
optparse

requests

lxml

urllib

BeautifulSoup4

#### 2月1 ~ 2月9日
写好启动界面Miscan.py

完善调用模块扫描文件common/start.py

完善对URL进行处理的类common/URL.py

写好爬虫大体框架 lib/utils/webscan/Crawl.py

#### 2月10日
写好根据表单字段填写的方法 lib/utils/webscan/Smart_fill.py

编写静态爬取功能类 lib/utils/webscan/HtmlParser.py

#### 2月11日
编写完善静态爬取功能类 lib/utils/webscan/HtmlParser.py

爬虫框架 lib/utils/webscan/Crawl.py 多线程处理存在bug

#### 2月12日
买菜，洗衣服，换床单 orz

#### 2月13日
研究hash去重 lib/utils/webscan/Urlfilter.py

#### 2月19日
写好去重url类 lib/utils/webscan/crawl/Urlfilter.py


#### 2月24日
完善去重去相似模块代码 lib/utils/webscan/crawl/Urlfilter.py

完善url处理提取模块 lib/utils/webscan/crawl/SpiderThread.py

#### 参考资料
书籍：

《白帽子讲web扫描》

《python绝技:运用python成为顶级黑客》

爬虫开发：

https://www.cnblogs.com/wang-yc/p/5623711.html

https://github.com/w-digital-scanner/w9scan

https://github.com/youmengxuefei/web_vul_scan

https://www.freebuf.com/news/topnews/96821.html


未授权：

https://xz.aliyun.com/t/6103
