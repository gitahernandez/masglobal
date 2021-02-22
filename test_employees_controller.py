import unittest
import json
from controllers.employees_controller import EmployeesController
import unittest, mock


class EmployeesControllerTest(unittest.TestCase):

    @mock.patch('controllers.employees_controller.EmployeesService.get_employees')
    def test_get_employees_employee_1(self, services_get_employees_mock):
        response_mock = json.loads('[{"id":1,"name":"Andrea","contractTypeName":"HourlySalaryEmployee","roleId":1,"roleName":"Administrator","roleDescription":null,"hourlySalary":10000.0,"monthlySalary":50000.0},{"id":2,"name":"Alex","contractTypeName":"MonthlySalaryEmployee","roleId":2,"roleName":"Contractor","roleDescription":null,"hourlySalary":10000.0,"monthlySalary":50000.0}]')
        services_get_employees_mock.return_value = response_mock
        controller = EmployeesController()
        status, result = controller.get_employees('1')
        self.assertEqual(status, 200)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.calculated_salary, 14400000.0)


    @mock.patch('controllers.employees_controller.EmployeesService.get_employees')
    def test_get_employees_employee_2(self, services_get_employees_mock):
        response_mock = json.loads('[{"id":1,"name":"Andrea","contractTypeName":"HourlySalaryEmployee","roleId":1,"roleName":"Administrator","roleDescription":null,"hourlySalary":10000.0,"monthlySalary":50000.0},{"id":2,"name":"Alex","contractTypeName":"MonthlySalaryEmployee","roleId":2,"roleName":"Contractor","roleDescription":null,"hourlySalary":10000.0,"monthlySalary":50000.0}]')
        services_get_employees_mock.return_value = response_mock
        controller = EmployeesController()
        status, result = controller.get_employees('2')
        self.assertEqual(status, 200)
        self.assertEqual(result.id, 2)
        self.assertEqual(result.calculated_salary, 600000.0)


    @mock.patch('controllers.employees_controller.EmployeesService.get_employees')
    def test_get_employees_all(self, services_get_employees_mock):
        response_mock = json.loads('[{"id":1,"name":"Andrea","contractTypeName":"HourlySalaryEmployee","roleId":1,"roleName":"Administrator","roleDescription":null,"hourlySalary":10000.0,"monthlySalary":50000.0},{"id":2,"name":"Alex","contractTypeName":"MonthlySalaryEmployee","roleId":2,"roleName":"Contractor","roleDescription":null,"hourlySalary":10000.0,"monthlySalary":50000.0}]')
        services_get_employees_mock.return_value = response_mock
        controller = EmployeesController()
        status, result = controller.get_employees(None)
        self.assertEqual(status, 200)
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 2)


if __name__ == '__main__':
    unittest.main()
