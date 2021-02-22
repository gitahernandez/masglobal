import requests
import json
import logging

from config.app_config import EMPLOYEES_SERVICE_URL

log = logging.getLogger(__name__)


class EmployeesService:
        
    def get_employees(self):
        try:
            x = requests.get(EMPLOYEES_SERVICE_URL)
            employee_list = json.loads(x.text)
            return employee_list
        except Exception as e:
            log.error(f"Error getting employees information from: {EMPLOYEES_SERVICE_URL}, error: {e}")
            return []
