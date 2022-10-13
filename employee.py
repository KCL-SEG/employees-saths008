"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    

    def __init__(self, name, salary_type, commision = ""):
        self.name = name
        self.salary_type =  salary_type
        self.commision = commision
#Default value of commision = "" so when totalCommision() is applied to it, it returns an errora
    def get_pay(self):
        if self.commision == "":
            return self.salary_type.getPaycheck()
        else:
            return self.salary_type.getPaycheck() + self.commision.totalCommision()

    def __str__(self):

        if self.commision == "":
            return f"{self.name} works on a {self.salary_type.__str__()}.  Their total pay is {self.get_pay()}."

        else:
            return f"{self.name} works on a {self.salary_type.__str__()} and receives a {self.commision.__str__()}.  Their total pay is {self.get_pay()}."







class Salary:

    def __init__(self, paycheck):
        self.paycheck = paycheck


    def getPaycheck(self):
        return self.paycheck

   #def __str__(self):
    #   if type(self) is MonthlySalary:
        #   return f"monthly salary of {self.paycheck}."

     #  elif type(self) is HourlySalary:
     #      return f"contract of {self.numberOfHours} hours at {self.paycheck}/hour"


class MonthlySalary(Salary):


         
    def __init__(self, paycheck):
        super().__init__(paycheck)

    def __str__(self):
        return f"monthly salary of {self.paycheck}"

        



class HourlySalary(Salary):


        
    def __init__(self, paycheck, numberOfHours):
        super().__init__(paycheck)
        self.numberOfHours = numberOfHours



    def getPaycheck(self):
        return self.paycheck * self.numberOfHours

    def __str__(self):
        return f"contract of {self.numberOfHours} hours at {self.paycheck}/hour"



  ##Code

    # Billie works on a monthly salary of 4000.  Their total pay is 4000.


class Commision:
    def __init__(self, commision_salary):
        self.commision_salary = commision_salary

    
    def totalCommision(self):
        return self.commision_salary

 # In case employee has no commision.
    def zeroCommision(self):
        if (self.commision_salary == ""):
            return 0



class BonusCommision(Commision):
    def __init__(self, commision_salary):
        super().__init__(commision_salary)

    def  __str__(self):
        self.zeroCommision()
        return f"bonus commision of {self.commision_salary}"




class ContractCommision(Commision):

    def __init__(self, commision_salary, numberOfContracts):
        super().__init__(commision_salary)
        self.numberOfContracts = numberOfContracts

    def __str__(self):
        return f"commision for {self.numberOfContracts} contract(s) at {self.commision_salary}/contract"

    def totalCommision(self):
        self.zeroCommision()
        return self.numberOfContracts * self.commision_salary

















billie = Employee('Billie', MonthlySalary(4000))
billie.__str__()

    # Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.

charlie = Employee('Charlie', HourlySalary(25, 100))
charlie.__str__()
    # Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlySalary(3000), ContractCommision(200, 4))
renee.__str__()

    # Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlySalary(25, 150), ContractCommision(220, 3))
jan.__str__()
    # Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.

robbie = Employee('Robbie', MonthlySalary(2000), BonusCommision(1500))
robbie.__str__()

    # Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.

ariel = Employee('Ariel', HourlySalary(30, 120), BonusCommision(600))
ariel.__str__()



