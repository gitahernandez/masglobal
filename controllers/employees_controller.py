import requests
import json
import logging
from factories.employees_factory import EmployeesFactory
from services.employees_service import EmployeesService

log = logging.getLogger(__name__)

class EmployeesController:
        
    def get_employees(self, employee_id):
        try:
            service = EmployeesService()
            employee_list = service.get_employees()
            employee_factory = EmployeesFactory()
            if employee_list and employee_id:
                log.info(f"Getting information for id {employee_id}")
                employee_row = [employee for employee in employee_list if employee['id'] == int(employee_id)]
                if employee_row:
                    return 200, employee_factory.create_employee(employee_row[0])
                else:
                    return 404, "Employee not found"
                    
            else:
                log.info("Getting information for all employees")
                return 200, [employee_factory.create_employee(employee) for employee in employee_list]

        except Exception as e:
            error_text = f"Error getting employees information : {e}"
            log.error(error_text)
            return 400, error_text

        