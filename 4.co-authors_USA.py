# min,max,avg,std-div of #co-authors per paper per author

from __future__ import division
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
from statistics import mean


'''India--------------------------------------------------------------------------'''
client = MongoClient()
db = client.vehicle
collection = db.car
query={
  "authors":{"$exists": True},
  "id":{"$exists": True}

}
projection={
  
  "authors":[],
  "id":[],
  
}
rm =list(collection.find(query,projection))
authIn=[y['authors'] for y in rm]
id_a=[y['id'] for y in rm]



loc = ("/Users/apoorvasingh/Downloads/usaFilter.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
authorNameIn=[]
sheet.cell_value(0, 0)


for i in range(sheet.nrows):
    authorNameIn.append(sheet.cell_value(i,0))


papers_of_authors=defaultdict(list)


p=0
for i in authIn:
  for j in i:
    papers_of_authors[j].append(id_a[p])
  p=p+1



co_authors_of_papers=defaultdict(int)


p=0
for i in id_a:
  co_authors_of_papers[i]=len(authIn[p])-1
  p=p+1



wb = xlwt.Workbook()
sheet1 = wb.add_sheet('sheet 1')

sheet1.write(0, 0, 'Authors')
sheet1.write(0, 1, 'Minimum')
sheet1.write(0, 2, 'Maximum')
sheet1.write(0, 3, 'Average')
sheet1.write(0, 4, 'Standard Deviation')

c=2

for i in authorNameIn:
  arr=[]
  for paper in papers_of_authors[i]:
    arr.append(co_authors_of_papers[paper])
  if(len(arr)!=0):
    avg=mean(arr)
  else: avg=0

  variance = 0
  for j in arr:
    variance = variance + ( avg- j) ** 2
  if len(arr)!=0:
    variance=variance/len(arr)
    sd=variance ** 0.5
  else: sd=0

  if len(arr)!=0:
    smallest=min(arr)
    largest=max(arr)
  else: smallest=largest=0

  sheet1.write(c, 0, i);
  sheet1.write(c, 1, smallest);
  sheet1.write(c, 2, largest);
  sheet1.write(c, 3, avg);
  sheet1.write(c, 4, sd);

  c=c+1

wb.save('co_authorsU.xls')

