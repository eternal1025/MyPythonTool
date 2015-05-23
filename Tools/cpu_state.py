#coding:utf-8

import psutil
import os

def getCPUstate(interval=1):
    cpu = (" CPU: " + str(psutil.cpu_percent(interval)) + "%")
    os.system("clear")
    return cpu

def getMemorystate():    
    phymem = psutil.phymem_usage()    
    buffers = getattr(psutil, 'phymem_buffers', lambda: 0)()    
    cached = getattr(psutil, 'cached_phymem', lambda: 0)()    
    used = phymem.total - (phymem.free + buffers + cached)    
    line = " Memory: %5s%% %6s/%s" % (    
        phymem.percent,    
        str(int(used / 1024 / 1024)) + "M",    
        str(int(phymem.total / 1024 / 1024)) + "M"    
    )       
    return line   

while True:
    print getCPUstate()

