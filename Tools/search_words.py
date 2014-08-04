#coding:utf-8
import urllib
import urllib2
import re #正则表达式

#采集搜索引擎联想词
#2014-5-23

word = urllib.quote('王自') #关键词变量

# 用urllib.quote()处理汉字编码的问题
# print(word)

search_url = 'http://sug.so.360.cn/suggest?callback=suggest_so&encodei' \
             'n=utf-8&encodeout=utf-8&format=json&fields=word,obdata&word=' + word

#构造头信息
headers = {
            'GET':search_url,
            'Host':'sug.so.360.cn',
            'Referer':'http://www.so.com/',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36'

         }

req = urllib2.Request(search_url)

for key in headers:
    req.add_header(key, headers[key])

# req.add_header('Host', 'sug.so.360.cn')
# req.add_header('Referer', 'http://www.so.com/')

return_html = urllib2.urlopen(req).read()

print '--->', return_html

#用正则表达式解析
ss = re.findall("\"(.*?)\"", return_html)

for item in ss:
    print item








