import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import matplotlib as mpl
import pandas as pd
import pymongo
import pprint
from pymongo import MongoClient
from collections import defaultdict
import xlrd
import xlwt
from xlwt import Workbook
import collections

'''India--------------------------------------------------------------------------'''
client = MongoClient()
db = client.solarsystem
collection = db.sun
query={
	"authors":{"$exists": True},
	"year":{"$exists": True}

}
projection={
	
	"authors":[],
	"year":1,
	
}
rm =list(collection.find(query,projection))
authIn=[y['authors'] for y in rm]
yearIn=[y['year'] for y in rm]
di=defaultdict(list)
p=0
for i in authIn:
	y=yearIn[p]
	for k in i:
		di[k].append(y)
	p=p+1

loc = ("/Users/apoorvasingh/Downloads/indiaFilter.xlsx")
	 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
	 
authorNameIn=[]
sheet.cell_value(0, 0)


for i in range(sheet.nrows):
	  authorNameIn.append(sheet.cell_value(i,0))

wb = xlwt.Workbook()
sheet1 = wb.add_sheet('sheet 1')

sheet1.write(0, 0, 'Authors')
sheet1.write(0, 1, 'Year')
sheet1.write(0, 2, 'Count')

c=2
for i in authorNameIn:
	yc=defaultdict(int)
	if len(di[i])== 0:
		sheet1.write(c, 0, i)
		sheet1.write(c, 2, 0)
		c=c+1
	else:
		for k in di[i]:
			yc[k]=yc[k]+1
		od = collections.OrderedDict(sorted(yc.items()))
		for key in od:
			sheet1.write(c, 0, i)
			sheet1.write(c, 1, key)
			sheet1.write(c, 2, od[key])
			c=c+1
	c=c+1

wb.save('Indian publications.xls')

'''USA----------------------------------------------------------------------'''

client = MongoClient()
db = client.vehicle
collection = db.car
query={
	"authors":{"$exists": True},
	"year":{"$exists": True}

}
projection={
	
	"authors":[],
	"year":1,
	
}
rm =list(collection.find(query,projection))
authUs=[y['authors'] for y in rm]
yearUs=[y['year'] for y in rm]
du=defaultdict(list)
p=0
for i in authUs:
	y=yearUs[p]
	for k in i:
		du[k].append(y)
	p=p+1

loc = ("/Users/apoorvasingh/Downloads/usaFilter.xlsx")
	 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
	 
authorNameUs=[]
sheet.cell_value(0, 0)


for i in range(sheet.nrows):
	  authorNameUs.append(sheet.cell_value(i,0))


wb = xlwt.Workbook()
sheet1 = wb.add_sheet('sheet 1')

sheet1.write(0, 0, 'Authors')
sheet1.write(0, 1, 'Year')
sheet1.write(0, 2, 'Count')

c=2
for i in authorNameUs:
	yc=defaultdict(int)
	if len(du[i])== 0:
		sheet1.write(c, 0, i)
		sheet1.write(c, 2, 0)
		c=c+1
	else:
		for k in du[i]:
			yc[k]=yc[k]+1
		od = collections.OrderedDict(sorted(yc.items()))
		for key in od:
			sheet1.write(c, 0, i)
			sheet1.write(c, 1, key)
			sheet1.write(c, 2, od[key])
			c=c+1
	c=c+1

wb.save('USA publications.xls')




