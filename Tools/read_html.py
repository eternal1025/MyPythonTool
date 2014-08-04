#coding:utf-8
import urllib2

html = urllib2.urlopen('http://www.so.com').read()

print html