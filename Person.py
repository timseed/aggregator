#!/usr/bin/python
from Ent import * 



class Person(object):
  """ Person Class which has some simple Entities. name, civilid, idcard and passport """

  def __init__(self):
      """ Build the default Person definition """
      self.entities=[]      #A List of Ent types
      self.data=()
      self.name=Ent("name","similar")
      self.civ=Ent("civ","exact","[0-9]{8}")
      self.idcard=Ent("id","exact","[0-9A-Za-z]{20}")
      self.passport=Ent("passport","exact","[0-9A-Za-z]{10}")
      self.gsm=Ent("gsm","exact","[0-9]{10}")
      self.address=Ent("address","exact","[0-9]{10}")
      self.car=Ent("car","exact","[0-9]{10}")
      self.entities.append(self.name)
      self.entities.append(self.civ)
      self.entities.append(self.idcard)
      self.entities.append(self.passport)
      self.entities.append(self.gsm)
      self.entities.append(self.address)
      self.entities.append(self.car)
      #self.add(self,self.name)
      #self.add(self,self.civ)

  def addent(self,e):
       '''Add an Entity to this Definition '''
       self.entities.append(Ent(e))
  
  def adddata(self,data):
       '''Add data to this Definition '''
       self.data=self.data+tuple(data)
       # Now using this Tuple we need to Update the Entity DATA member Variable
       for e in self.entities:
           if self.data.count(e.getname())>0:
              pos=self.data.index(e.getname())
              e.setvalue(self.data[pos+1])
            
  def getdata(self):
      """ Return the data tuple """
      return self.data     
  
  def showdata(self):
      """ Shows the data objects in the Object """
      print self.data

  def showent(self):
      """ Shows the Ent objects in the Object """
      for e in self.entities:
          e.show()


  def match(self,field,value):
      """We need to check if the field and value matches our criteria"""
      success= -1
      for e  in self.entities:
          if e.name == field:
             #print("Found the Field")
             if e.value == value:
                #print "************ Matched the Value **************"
                success=1
                break 
             #else:
                #print ("Field %s EValue <%s> != <%s>" % (field,e.value,value))
      return success
