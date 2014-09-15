# coding=utf8
from lxml import etree


bus=int(raw_input('请输入公交站路线:'))
bus_zd=raw_input('请输入公交车:')
url="http://119.146.222.248:8091/BusTransfer/brewMobile/queryArrivalForetell?lineName=%s路&stationName=%s" % (bus,bus_zd)
tree=etree.parse(url)
root=tree.getroot()
if(root.__len__() > 3):
    start_bus = root[3][4].text
    end_bus = root[3][5].text
    now_bus = root[3][6].text
    you_bus =  root[3][9].text
    print ''
    print '<<<<<<<<<<<<<<<<<<<<<<<<<<<'
    print u'%s  到  %s 路线' % (start_bus,end_bus)
    print u'公交车已经到%s站' % now_bus
    print u'距离您还有%s站' % you_bus
    print ''
    print '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    h_start_bus = root[4][4].text
    h_end_bus = root[4][5].text
    h_now_bus = root[4][6].text
    h_you_bus =  root[4][9].text
    print u'%s  到  %s 路线' % (h_start_bus,h_end_bus)
    print u'公交车已经到%s站' % h_now_bus
    print u'距离您还有%s站' % h_you_bus
else:
    print u'您输入的有误'