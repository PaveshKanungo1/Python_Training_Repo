class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def calculate_salary(self):
        print("Calling for wrong class.")

class FullTimeEmployee(Employee):
    TAX_RATE = 0.10
    PF_RATE = 0.12

    def calculate_salary(self):
        tax = self.base_salary * self.TAX_RATE
        pf = self.base_salary * self.PF_RATE
        final_salary = self.base_salary - tax - pf
        return final_salary
    
class PartTimeEmployee(Employee):
    TAX_RATE = 0.10
    PF_RATE = 0.12

    def calculate_salary(self):
        tax = self.base_salary * self.TAX_RATE
        pf = self.base_salary * self.PF_RATE
        final_salary = self.base_salary - tax - pf
        return final_salary
    
class Contractor(Employee):
    TAX_RATE = 0.10 

    def calculate_salary(self):
        tax = self.base_salary * self.TAX_RATE
        final_salary = self.base_salary - tax
        return final_salary
    
full_time = FullTimeEmployee("Pavesh1", 1, 5000)
part_time = PartTimeEmployee("Pavesh2", 2, 3000)
contractor = Contractor("Pavesh3", 3, 4000)

print("Full-Time Employee Final Salary:", full_time.calculate_salary())
print("Part-Time Employee Final Salary:", part_time.calculate_salary())
print("Contractor Final Salary:", contractor.calculate_salary())

    

