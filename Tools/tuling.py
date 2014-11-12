#coding:utf-8
import urllib2

"""
调用图灵API
"""


api_key = "bd294469d3dce4f0f4db0c05923a6e11"

info = "唉，工作压力山大啊，头发一直掉"

apiURL = "http://www.tuling123.com/openapi/api?key=" + api_key + "&info=" + info

json_str = urllib2.urlopen(apiURL).read()

fruit = eval(json_str)

print fruit["text"]