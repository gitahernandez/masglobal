import abc


class EmployeesInterface(metaclass=abc.ABCMeta):
    
    def __init__(self, employee):
        self.id = employee['id']
        self.name = employee['name']
        self.contractTypeName = employee['contractTypeName']
        self.roleId = employee['roleId']
    
    @abc.abstractmethod
    def getSalary(self, salary_value):
        pass



    