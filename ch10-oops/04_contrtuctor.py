

class Employee:
    name=""
    language = "Py"
    salary=12
    
    def __init__(self, name, salary, language):  # __ -> dunder method
        print("I am creating an object.")
        self.name=name
        self.salary=salary
        self.language=language
    
    def getInfo(self):
        print(f"lang={self.language}. salary={self.salary}")
        
    @staticmethod # now no need to put self
    def greet():
        print("Good Morning")
      
khari=Employee("Kh", 134,"JAVA")

khari.getInfo()
khari.greet()
