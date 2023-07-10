class Employee:
    def __init__(self,name):
        self.name = name
    
    def calculatePay(self):
        pass

class SalariedEmployee(Employee):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary = salary
    
    def calculatePay(self):
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, name,hourly_rate,hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculatePay(self):
        return self.hours_worked*self.hourly_rate
    
salaried_employee1=SalariedEmployee("Shree",100000)
print("Details of Salaried Employee:")
print("Name: ",salaried_employee1.name)
print("Salary: ",salaried_employee1.calculatePay())

hourly_employee1=HourlyEmployee("Shree",10000,40)
print("Details of Hourly Employee:")
print("Name: ",hourly_employee1.name)
print("Salary: ",hourly_employee1.calculatePay())

