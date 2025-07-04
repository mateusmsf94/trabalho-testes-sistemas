import pytest

from pages.LoginPage import LoginPage
from pages.CustomerPage import CustomerPage
from pages.ManagerPage import ManagerPage
from pages.AccountPage import AccountPage

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

@pytest.fixture
def run_all_browser_manager(all_browser):
    # Go through manager login flow first
    login_page = LoginPage(browser=all_browser)
    login_page.open_page()
    login_page.click_manager_login_button()
    login_page.wait_for_manager_page()
    
    # Create ManagerPage with existing driver
    manager_page = ManagerPage(driver=login_page.driver)  # Pass existing driver
    
    yield manager_page
    manager_page.close()

@pytest.fixture 
def run_all_browser_manager_to_customer(all_browser):
    # Go through manager login flow first
    login_page = LoginPage(browser=all_browser)
    login_page.open_page()
    login_page.click_manager_login_button()
    login_page.wait_for_manager_page()
    
    # Create ManagerPage with existing driver
    manager_page = ManagerPage(driver=login_page.driver)
    
    # Return both manager_page for setup and driver for customer transition
    yield manager_page
    manager_page.close()

@pytest.fixture
def run_all_browser_account(all_browser):
    # Go through customer login flow to reach account page (like test2)
    login_page = LoginPage(browser=all_browser)
    login_page.open_page()
    login_page.click_login_button()
    login_page.wait_for_customer_page()
    
    # Create CustomerPage with existing driver
    customer_page = CustomerPage(driver=login_page.driver)
    
    # Select Harry Potter and login to reach account page
    customer_page.select_customer_and_login("Harry Potter")
    customer_page.wait_for_account_page()
    
    # Create AccountPage with existing driver
    account_page = AccountPage(driver=customer_page.driver)
    
    yield account_page
    account_page.close()