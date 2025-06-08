

class Employee:
    language = "Py"
    salary=12
    
    def getInfo(self):
        print(f"lang={self.language}. salary={self.salary}")
        
    @staticmethod # now no need to put self
    def greet():
        print("Good Morning")
      
khari=Employee()

khari.getInfo()
khari.greet()


