#!/usr/bin/python2.7

from Ent import *        #Entity Name, ID etc
from Gen import *        #Information Generator
from Person import *     #A Person has Entities
from Population import * #A Collection of Person
debug=0


def Reduce():
  for i in range(0,Generator.len()):
    g=Generator.get(i) 
    tuplen=g.len()
    if debug:
       print("####################")
       print("%4d <%s> "%(i,g.getdata()))
       print("TupLen <%d>"%(tuplen))
    # We need to split the Tuple - and see what Field we are being presented with
    datatuple=()
    found=-1
    for loop in range(0,tuplen):
        f,v=g.get(loop)
        if debug:
           if loop==1:
              junk=1
              g.show()
           print("Looking for Field <%s> Value <%s>"%(f,v))
        pidx=Oman.find(f,v)
        if pidx > -1:
           if debug:
              print("Found ... Need to Update")
           found=pidx
        datatuple=datatuple+(f,v)

    if found > -1 and Oman.len()>0:
       if debug:
          print ("UPDATE Data is %s"%(datatuple,)) 
       Oman.update(found,datatuple)
    else: 
      if len(datatuple): 
        if debug:
           print("Not found.... Create") 
        p=Person()
        p.adddata(datatuple)
        Oman.add(p)
        if debug:
           print("Added 1 Person") 

Oman=Population()
Generator=GenObjects("O2.txt")
Generator.AddFile("EE.txt")
Generator.AddFile("Water.txt")
Generator.AddFile("avis.txt")




Reduce()
for loop in range(1,4):
   pdata=Oman.getdata()
   Generator=GenObjects()
   Generator.setdata(pdata)
   Oman=Population()
   Reduce()

Oman.show() 


#p.show()
