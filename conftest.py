import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

#login page
@pytest.fixture
def login(page):
    login_page = LoginPage(page)
    login_page.open()   # opens automatically
    return login_page

#dashboard page
@pytest.fixture
def dashboard(page):
    return DashboardPage(page)

# Screenshot on Failure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Take screenshot only when test fails
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")