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
authUs=[y['authors'] for y in rm]
yearUs=[y['year'] for y in rm]
du=defaultdict(list)
p=0
for i in authUs:
  y=yearUs[p]
  for k in i:
    du[k].append(y)
  p=p+1


loc = ("/Users/apoorvasingh/Downloads/filterindia.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
authorNameUs=[]
sheet.cell_value(0, 0)


for i in range(sheet.nrows):
    authorNameUs.append(sheet.cell_value(i,0))

wb = xlwt.Workbook()
sheet1 = wb.add_sheet('sheet 1')

sheet1.write(0, 0, 'Authors')
sheet1.write(0, 1, 'Minimum')
sheet1.write(0, 2, 'Maximum')
sheet1.write(0, 3, 'Average')
sheet1.write(0, 4, 'Standard Deviation')

c=2
for i in authorNameUs:
  yc=defaultdict(int)
  for k in du[i]:
    yc[k]=yc[k]+1
  od = collections.OrderedDict(sorted(yc.items()))
  arr_of_counts=[]
  for key in od:
    arr_of_counts.append(od[key])

  if(len(arr_of_counts)!=0):
    avg=mean(arr_of_counts)
  else: avg=0

  variance = 0
  for j in arr_of_counts:
    variance = variance + ( avg- j) ** 2
  if len(arr_of_counts)!=0:
    variance=variance/len(arr_of_counts)
    sd=variance ** 0.5
  else: sd=0

  if len(arr_of_counts)!=0:
    smallest=min(arr_of_counts)
    largest=max(arr_of_counts)
  else: smallest=largest=0


  sheet1.write(c, 0, i)
  sheet1.write(c, 1, smallest)
  sheet1.write(c, 2, largest)
  sheet1.write(c, 3, avg)
  sheet1.write(c, 4, sd)

  c=c+1
c=c+1

wb.save('India_publications_new.xls')




