from interfaces.employees_interface import EmployeesInterface
from config.app_config import HOURS, MONTHS


class HourlySalaryEmployee(EmployeesInterface):
    def __init__(self, employee):
        super().__init__(employee)
        self.salaryValue = employee['hourlySalary']
        self.calculatedSalary = self.getSalary()
        
    def getSalary(self):
        return HOURS * self.salaryValue * MONTHS

    

    


