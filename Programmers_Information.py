# Create a class programmer for storing information of a few programmers working at Microsoft.

class programmer():
    company="Microsoft"
    def __init__(self, name , salary, id):
        self.name=name
        self.salary=salary
        self.id=id

    def getInformation(self):
        print(f"Programmer name is {self.name} his company name is {self.company} his salary is {self.salary} his ID is {self.id}\n")
      

Pratyay=programmer("Pratyay", 564125, "CSBS62")
Sutanu=programmer("Sutanu", 211655, "CSBS22")
Jayanta=programmer("Jayanta", 56565, "CSBS55")
Sayan=programmer("Sayan", 44125, "CSE13")
Avik=programmer("Avik", 41225, "CSE33")

Pratyay.getInformation()
Sutanu.getInformation()
Jayanta.getInformation()
Sayan.getInformation()
Avik.getInformation()
