from dtos.monthly_salary_employes import MonthtlySalaryEmployee
from dtos.houry_salary_employes import HourlySalaryEmployee


class EmployeesFactory:
    def create_employee(self, employee):
        if employee['contractTypeName'] == 'HourlySalaryEmployee':
            return HourlySalaryEmployee(employee)


        elif employee['contractTypeName'] == 'MonthlySalaryEmployee':
            return MonthtlySalaryEmployee(employee)

