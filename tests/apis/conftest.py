import pytest
from playwright.sync_api import APIRequestContext
from apis.clients.user_client import UserClient
from apis.clients.dept_client import DeptClient
from faker import Faker

# try this class to remove api_fixture
@pytest.fixture(scope="function")
def api_request(playwright) -> APIRequestContext:
    context = playwright.request.new_context()
    yield context
    context.dispose()


@pytest.fixture
def user_client(api_request) -> UserClient:
    return UserClient(api_request)

@pytest.fixture
def dept_client(api_request):
    return DeptClient(api_request)

@pytest.fixture
def fake() -> Faker:
    return Faker()
