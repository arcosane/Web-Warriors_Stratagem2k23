class Parent(object): 
       
    
    def __init__(self, name, id): 
        self.name = name 
        self.id = id
   
   
    def  emp1(self): 
        return self.id , self.name
   
    def emp2(self): 
        if self.id > 500000:
           return " Valid Employee "
        else:
           return " Invalid Employee "
   
   
class Child(Parent): 
    
    def End(self):
        print( " END OF PROGRAM " ) 
      
# Driver code 
Employee1 = Parent( "Employee1" , 600445)  # parent class object
print( Employee1.emp1() , Employee1.emp2() ) 
Employee2 = Child( "Employee2" , 198754) # child class object 
print( Employee2.emp1() , Employee2.emp2() ) 
Employee2.End()