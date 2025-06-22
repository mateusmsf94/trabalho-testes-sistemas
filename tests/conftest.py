import pytest

from pages.LoginPage import LoginPage
from pages.CustomerPage import CustomerPage

def pytest_addoption(parser):
    parser.addoption('--browser_selenium', default='chrome')

@pytest.fixture
def open_bank_demo(request):
    selected_browser = request.config.getoption('browser_selenium').lower
    login_page = LoginPage(browser=selected_browser)
    login_page.open_page()
    yield login_page
    login_page.close()

@pytest.fixture
def open_customer_select_and_login(request):
    selected_browser = request.config.getoption('browser_selenium').lower
    customer_page = CustomerPage(browser=selected_browser)
    customer_page.open_page()
    yield customer_page
    customer_page.close()
    

@pytest.fixture
def run_all_browser(all_browser):
    login_page = LoginPage(browser=all_browser)
    login_page.open_page()
    yield login_page
    login_page.close()

@pytest.fixture
def run_all_browser_customer(all_browser):
    # Go through login flow first
    login_page = LoginPage(browser=all_browser)
    login_page.open_page()
    login_page.click_login_button()
    login_page.wait_for_customer_page()
    
    # Create CustomerPage with existing driver
    customer_page = CustomerPage(driver=login_page.driver)  # Pass existing driver
    
    yield customer_page
    customer_page.close()

@pytest.fixture
def run_all_browser_customer_isolated(all_browser):
    # Direct access to customer page (isolated)
    customer_page = CustomerPage(browser=all_browser)
    customer_page.open_page()
    yield customer_page
    customer_page.close()