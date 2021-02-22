from interfaces.employees_interface import EmployeesInterface
from config.app_config import HOURS, MONTHS


class HourlySalaryEmployee(EmployeesInterface):
    def __init__(self, employee):
        super().__init__(employee)
        self.salary_value = employee['hourlySalary']
        self.calculated_salary = self.getSalary()
        
    def getSalary(self):
        return HOURS * self.salary_value * MONTHS

    

    


