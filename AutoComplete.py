import urllib2
from redis_completion import RedisEngine
import csv
import redis

engine = RedisEngine()

# UPDATING CACHE

txtfile = open('BestBuy.txt', "r") 
productList = txtfile.read().split("\n")
setProductList = set(productList)
productList = list(setProductList)

map(engine.store, productList)

Options = engine.search('Ultra HD TV Silver')
for item in Options:
	print item




$$$$$$$$$$$$$$$$$$$$$

>>> mystring = "alfa"
>>> myfile = open("/home/gustacaste/FileA", 'w')
>>> myfile.write(mystring)
>>> myfile.close()