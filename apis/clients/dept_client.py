from .base_client import BaseAPIClient
#TODO fake class
class DeptClient(BaseAPIClient):
    DEPT_ENDPOINT = "/unknown"

    def get_departments(self):
        return self.request.get(f"{self.base_url}{self.DEPT_ENDPOINT}")