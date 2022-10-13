"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    

    def __init__(self, name, salary_type, commission = ""):
        self.name = name
        self.salary_type =  salary_type
        self.commission = commission
#Default value of commission = "" so when totalCommission() is applied to it, it returns an errora
    def get_pay(self):
        if self.commission == "":
            return self.salary_type.getPaycheck()
        else:
            return self.salary_type.getPaycheck() + self.commission.totalCommission()



    def __str__(self):

        if self.commission == "":
            print(f'"{self.name} works on a {self.salary_type.__str__()}.  Their total pay is {self.get_pay()}."')
            return f'"{self.name} works on a {self.salary_type.__str__()}.  Their total pay is {self.get_pay()}."'

        else:
            print(f'"{self.name} works on a {self.salary_type.__str__()} and receives a {self.commission.__str__()}.  Their total pay is {self.get_pay()}."')
            return f'"{self.name} works on a {self.salary_type.__str__()} and receives a {self.commission.__str__()}.  Their total pay is {self.get_pay()}."'
        




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


class Commission:
    def __init__(self, commission_salary):
        self.commission_salary = commission_salary

    
    def totalCommission(self):
        return self.commission_salary

 # In case employee has no commission.
    def zeroCommission(self):
        if (self.commission_salary == ""):
            return 0



class BonusCommission(Commission):
    def __init__(self, commission_salary):
        super().__init__(commission_salary)

    def  __str__(self):
        self.zeroCommission()
        return f"bonus commission of {self.commission_salary}"




class ContractCommission(Commission):

    def __init__(self, commission_salary, numberOfContracts):
        super().__init__(commission_salary)
        self.numberOfContracts = numberOfContracts

    def __str__(self):
        return f"commission for {self.numberOfContracts} contract(s) at {self.commission_salary}/contract"

    def totalCommission(self):
        self.zeroCommission()
        return self.numberOfContracts * self.commission_salary

















billie = Employee('Billie', MonthlySalary(4000))
billie.__str__()

    # Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.

charlie = Employee('Charlie', HourlySalary(25, 100))
charlie.__str__()
    # Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlySalary(3000), ContractCommission(200, 4))
renee.__str__()

    # Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlySalary(25, 150), ContractCommission(220, 3))
jan.__str__()
    # Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.

robbie = Employee('Robbie', MonthlySalary(2000), BonusCommission(1500))
robbie.__str__()

    # Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. 

ariel = Employee('Ariel', HourlySalary(30, 120), BonusCommission(600))
ariel.__str__()



