"""Employee pay calculator."""

class Employee:

    

    def __init__(self, name, salary_type, commission = "", hasCommission = True):
        self.name = name
        self.salary_type =  salary_type
        self.commission = commission
        self.hasCommission = hasCommission
        self.setHasCommission()




    #Total pay of employees, including commissions.    
    def get_pay(self):
       if self.hasCommission:
           return self.salary_type.getPaycheck() + self.commission.totalCommission()
       else:
            return self.salary_type.getPaycheck()




    #Sets the boolean value for hasCommision by checking what is in commision.
    #Raises error if anything other than a Commision object or "" is entered.     

    def setHasCommission(self):
        if(isinstance(self.commission, Commission)):
            self.hasCommission = True

        elif (self.commission == ""):
            self.hasCommission = False

        else:
            raise TypeError("Please either leave commission empty or assign a Commission object. ")        







    def strforHasCommission(self):
        if self.hasCommission:
            return f" and receives a {self.commission.__str__()}."

        else:
            return "."
       

    def __str__(self):

         print (f"'{self.name} works on a {self.salary_type.__str__()}" + f"{self.strforHasCommission()}" +  f" Their total pay is {self.get_pay()}.'")
         return (f"'{self.name} works on a {self.salary_type.__str__()}" + f"{self.strforHasCommission()}" +  f" Their total pay is {self.get_pay()}.'")
         


    


class Salary:

    def __init__(self, paycheck):
        self.paycheck = paycheck


    def getPaycheck(self):
        return self.paycheck

     
    def __str__(self):
        if type(self) is MonthlySalary:
          return f"monthly salary of {self.paycheck}"

        elif type(self) is HourlySalary:
          return f"contract of {self.numberOfHours} hours at {self.paycheck}/hour"



class MonthlySalary(Salary):


         
    def __init__(self, paycheck):
        super().__init__(paycheck)

        



class HourlySalary(Salary):


        
    def __init__(self, paycheck, numberOfHours):
        super().__init__(paycheck)
        self.numberOfHours = numberOfHours



    def getPaycheck(self):
        return self.paycheck * self.numberOfHours



class Commission:
    def __init__(self, commission_salary):
        self.commission_salary = commission_salary

    
    def totalCommission(self):
        return self.commission_salary



    def __str__(self):
        if (type(self) is ContractCommission):
            return f"commission for {self.numberOfContracts} contract(s) at {self.commission_salary}/contract"

        elif (type(self) is BonusCommission):
            return f"bonus commission of {self.commission_salary}"


"""All bonus commissions eg. 3 contracts at £100 each"""
class BonusCommission(Commission):
    def __init__(self, commission_salary):
        super().__init__(commission_salary)


"""All contract commissions eg. 3 contracts at £100 each"""
class ContractCommission(Commission):

    def __init__(self, commission_salary, numberOfContracts):
        super().__init__(commission_salary)
        self.numberOfContracts = numberOfContracts

    def totalCommission(self):
        return self.numberOfContracts * self.commission_salary













"""Declare all employees here!"""


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlySalary(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlySalary(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlySalary(3000), ContractCommission(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlySalary(25, 150), ContractCommission(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlySalary(2000), BonusCommission(1500))


# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. 
ariel = Employee('Ariel', HourlySalary(30, 120), BonusCommission(600))




# string = 'Billie works on a monthly salary of 4000.  Their total pay is 4000.'
# print(str(billie))
# assert str(billie) == string



listOfEmployees = [billie, charlie, renee, jan, robbie, ariel]

for employee in listOfEmployees:
    employee.__str__()





