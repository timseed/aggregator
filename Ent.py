#!/usr/bin/python

'''The Ent is a class that holds a tuple
   this can look like this
   ('name','tim')
   or 
   ('name','tim','passport','123')

'''

class Ent(object):

   def __init__(self,name,unique,regex="",value=""):
      self.name=name
      self.unique=unique
      self.regex=regex
      self.value=value

   ''' 4 Items means we have 2 data rows - check the examples at the head of this file '''
   def len(self):
       return len(self)/2

   def getname(self):
       return self.name
 
   def getunique(self):
       return self.unique

   def getregex(self):
       return self.regex
   
   def getvalue(self):
       return self.value

   def setvalue(self,value):
       self.value=value

   #''' index 0 means item 0+1 ... data and value'''
   #def get(self,index):
       #if (index*2)<self.len():
       #  field=self 
       #else
       #   raise Exception('INVALID')

   def show(self):
        print ("==============")
        print ("  Ent Def")
        print ("Name       %s" % (self.name)) 
        print ("Unique     %s" % (self.unique)) 
        print ("Regex      %s" % (self.regex)) 
        print ("Value      %s" % (self.value)) 
