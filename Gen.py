#!/bin/python

class GenLine(object):

  def __init__(self,data=""):
      """ A Line of data in Tuple Format"""
      self.data=()
      if len(data)>0:
         self.data=data

  def len(self):
      """ The Number of GROUPS of data in this tuple. The data SHOULD BE field,value.... """
      return len(self.data)/2

  def get(self,tuple_id):
      """ Needs Index of Item. Referring to the field,value"""
      if tuple_id > self.len():
         print("Wanted item %d we have %d items " % (tuple_id,self.len()))
         print("Data Length is %d " %(len(self.data)))
         print ', ,'.join([str(i[0]) for i in self.data])
         raise Exception("INVALID")
      else:
        field=self.data[tuple_id*2]    
        value=self.data[(tuple_id*2)+1]    
        #print("Field <%s> Value <%s>"%(field,value))
        return field,value

  def show(self):
      """ List the data item """
      for i in range(0,self.len()):
         print("%d -> %s" % (i,self.data[i]))
      print("========")

  def getdata(self):
      """Return the data tuple"""
      return self.data


class GenObjects(object):
    """ Generate a List of GenLine Objects """

    def __init__(self,file=""):
       """ Filename - and it is assumed it is a CSV File with Column headers
           However filename can be empty to initialize the class"""
       self.file = file
       self.myitems=[]     #A Collection of GenLine objects
       self.Assemble()


    def AddFile(self,newfile):
        """This allows you to add extra data files to the GenObjects collection"""
        self.file = newfile
        self.Assemble()

    def Assemble(self):
        """ Assumes the file is a CSV. This is automatically called from the __init__ Method"""
        if len(self.file):
          f = open(self.file)
          cols=f.readline().split(','); 
          cols = [ c.rstrip().lstrip() for c in cols]    
          for line in f:
            t=()
            data=line.split(',')
            data= [d.rstrip().lstrip() for d in data]
            pos=0
            for d in data:
                if len(d):
                    t=t+(cols[pos],d)
                pos=pos+1
            gl=GenLine(t) 
            self.myitems.insert(0,gl)
          f.close()

    def show(self):
         """ Lists all the items """
         for i in self.myitems:
            i.show() 

    def  len(self):
         """ Returns the number of Items"""
         return len(self.myitems)

    def  get(self,index):
         """ Gets the item at position index. Throws INVALID if the index more than the number of items """
         if index < self.len():
             return self.myitems[index]
         else:
             raise Exception('INVALID')


    def setdata(self,dataarray):
        """ Load the Generator with Tuple Data array """
        for d in dataarray:
            gl=GenLine(d)
            self.myitems.insert(0,gl)

