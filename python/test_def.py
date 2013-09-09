class test:       
     def echo(self,
              a=1, 
              b=2):
          self.a=a
          self.b=b
          print "self.a------- %s,self.b------- %s"
          print self.a,self.b 
          print "a------- %s,b------- %s"
          print a,b 
df=test()
df.echo() 
