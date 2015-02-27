#!/ust/bin/python
from Person import *
from Ent    import *

class Population(object):
  debug=0
  def __init__(self):
      self.group = []    #A list of Person

  def add(self,p):
      self.group.append(p)

  def len(self):
      return len(self.group)

  def get(self,index):
      if index> self.len():
         raise Exception('INVALID')
      else:
         return self.group[index]

  def find(self,field,value):
      """ We need to look in the People List - to find these data items"""
      res=-1
      pos=0
      for p in self.group:
         res=p.match(field,value)
         if res > -1:
            res=pos
            break 
         pos=pos+1
      return res       #We do not match         

  def show(self):
      """ Output Population collection"""
      print("Dumping Populationi Defintion")
      for p in self.group:
          p.showdata()


  def update(self,personidx,datatuple):
      """ Update the Person record - specified by the Index """
      if self.debug:
         print("Updating Person id %d" %(personidx))
         print("There are %d Records " %(len(self.group)))
#     print("Before they look like %s "% self.group[personidx].showdata())
#     self.group[personidx].showent()
      (self.group[personidx]).adddata(datatuple)


  def getdata(self):
      """Read all the People data - the tuples. And return an array.
         The Array is sorted in BIGGEST LENGTH first """
      pdata=[]
      udata=[]
      for p in self.group:
          tdata=p.getdata()
          pdata.insert(0,tdata)
      pdata.sort(lambda x,y: cmp(len(y),len(x)))
      for i in range(0,len(pdata)):
         l=[]
         tt=pdata[i]
         for i in list(set(tt[::2])):
            p=tt.index(i)
            l.append(tt[p])
            l.append(tt[p+1])
 
         udata.append(tuple(l))
      return udata

  # We need to match id or name....
  # Do we have anyone who matches ?
#  def Match(self,ent):
      
      

