import pymongo
import pprint
from pymongo import MongoClient
from collections import defaultdict
import numpy as np
import xlrd
import math
import xlwt
from xlwt import Workbook

client = MongoClient()
db = client.vehicle
collection = db.car
query={
  "authors":{"$exists": True},

}
projection={
  
  "authors":[],
}
rm =list(collection.find(query,projection))
x=[y['authors'] for y in rm]
di=defaultdict(list)     #list of collaborators of an author
authorsIn=[]             #No. of authors
papersI=defaultdict(int) #No. of papers of an author

loc = ("/Users/apoorvasingh/Downloads/USA Faculties.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
authorNameIn=[]
sheet.cell_value(3, 3)

for i in range(2,sheet.nrows):
    authorNameIn.append(sheet.cell_value(i,3))


for i in x:
  for k in i:
    if k not in authorsIn:
      authorsIn.append(k)
    papersI[k]=papersI[k]+1


for i in x:
  for k in i:
    for name in i:
      if name not in di[k] and name in authorNameIn:
        di[k].append(name)
        

degI=defaultdict(int)     #degree non weigted of an authors
for j in authorsIn:
  degI[j]=len(di[j])-1

#print(degI)

query={
  "authors":{"$exists": True},
  "id":{"$exists": True},

}
projection={
    
  "authors":[],
  "id":[],
}
rm =list(collection.find(query,projection))
xa=[y['authors'] for y in rm]
xid=[y['id'] for y in rm]

a_of_id=defaultdict(list)      #authors of id
n=0
for i in xa:            
  for k in i:
      a_of_id[xid[n]].append(k)
  n=n+1
#print(a_of_id)



query={
  "authors":{"$exists": True},
  "references":{"$exists": True},

}
projection={
        
  "authors":[],
  "references":[],
}

rm =list(collection.find(query,projection))
xa=[y['authors'] for y in rm]
xref=[y['references'] for y in rm]

citations=defaultdict(int)        # citations of authors
p=0
for i in xref:
  for k in i:
    for auth in a_of_id[k]:
      if auth not in xa[p]:
        citations[auth]=citations[auth]+1
  p=p+1
#print(citations)

wb = Workbook()
         
        # add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0,0,"Authors")
sheet1.write(0,1,"Citation Count")
sheet1.write(0,2,"Degree")
sheet1.write(0,3,"Papers")
sheet1.write(0,4,"Result")

max=-1.0
ans=None
c=2

for i in authorNameIn:
  sheet1.write(c,0,i)
  sheet1.write(c,1,citations[i])
  sheet1.write(c,2,degI[i])
  sheet1.write(c,3,papersI[i])
  k=float((0.3*citations[i])+(0.1*papersI[i])+(0.2*degI[i]))
  sheet1.write(c,4,k)
  if k>max:
    max=k
    ans=i
  c=c+1
print ans


wb.save('influential_USA.xls')








