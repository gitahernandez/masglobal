from interfaces.employees_interface import EmployeesInterface
from config.app_config import MONTHS

class MonthtlySalaryEmployee(EmployeesInterface):
    def __init__(self, employee):
        super().__init__(employee)
        self.salary_value = employee['monthlySalary']
        self.calculated_salary = self.getSalary()

    def getSalary(self):
        return self.salary_value * MONTHS
