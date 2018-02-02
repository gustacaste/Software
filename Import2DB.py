import csv
import redis


# UPDATING CACHE

txtfile = open('CleanNames.txt', "r") 
productList = txtfile.read().split("\n")
setProductList = set(productList)
productList = list(setProductList)
productList.sort(key=str.lower)

r = redis.StrictRedis(host='localhost', port=6379, db=0)

i = 0
for product in productList:	
	a = r.set(i, product.lower() )
	i+=1




-------------------------

import csv
txtfile = open('CleanNames.txt', "r") 
productList = txtfile.read().split("\n")
setProductList = set(productList)
productList = list(setProductList)
productList.sort(key=str.lower)
for product in productList: 
    a = {}
    a['value']=product
    a['label']=product
    results.append(a)








