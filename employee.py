"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    

    def __init__(self, name, salary_type=""):
        self.name = name
        self.salary_type =  salary_type

    def get_pay(self):
        pass

    def __str__(self):
        print( f"{self.name} works on a {self.salary_type.__str__()}")




class Salary:

    def __init__(self, paycheck):
        self.paycheck = paycheck


    def __str__(self):
        if type(self) is MonthlySalary:
            return "MonthlySalary"

        elif type(self) is HourlySalary:
            return "HourlySalary"


class MonthlySalary(Salary):


         
    def __init__(self, paycheck):
        super().__init__(paycheck)



billie_salary_type = MonthlySalary(4000)


        



class HourlySalary(Salary):


        
    def __init__(self, paycheck, numberOfHours):
        super().__init__(paycheck)
        self.numberOfHours = numberOfHours


  ##Code

    # Billie works on a monthly salary of 4000.  Their total pay is 4000.

billie = Employee('Billie', billie_salary_type)
billie.__str__()

    # Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

    # Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

    # Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

    # Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

    # Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')




