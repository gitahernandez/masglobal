from interfaces.employees_interface import EmployeesInterface
from config.app_config import MONTHS

class MonthtlySalaryEmployee(EmployeesInterface):
    def __init__(self, employee):
        super().__init__(employee)
        self.salaryValue = employee['monthlySalary']
        self.calculatedSalary = self.getSalary()

    def getSalary(self):
        return self.salaryValue * MONTHS
