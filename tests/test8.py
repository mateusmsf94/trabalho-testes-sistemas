import pytest
import re
from pages.LoginPage import LoginPage
from pages.CustomerPage import CustomerPage

class Test8:
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge', 'firefox'])
    def test_complete_manager_to_customer_flow(self, run_all_browser_manager_to_customer):
        # Fixture gives us ManagerPage already on manager page (after login flow)
        manager_page = run_all_browser_manager_to_customer
        
        # Step 1: Add a new customer (John Doe)
        manager_page.add_customer("John", "Doe", "12345")
        
        # Assert the success alert appears with correct message and click OK
        add_customer_alert = manager_page.wait_and_assert_customer_added_alert()
        print(f"✅ Customer added successfully! Alert message: {add_customer_alert}")
        
        # Step 2: Open account for the newly added customer
        selected_customer = manager_page.open_account_for_customer("doe", "Dollar")
        
        # Assert the account creation success alert and click OK
        account_alert = manager_page.wait_and_assert_account_created_alert()
        print(f"✅ Account opened successfully for {selected_customer}! Alert message: {account_alert}")
        
        # Extract account number from the alert message
        account_number_match = re.search(r'account Number :\s*(\d+)', account_alert, re.IGNORECASE)
        if account_number_match:
            created_account_number = account_number_match.group(1)
            print(f"✅ Extracted account number: {created_account_number}")
        else:
            raise AssertionError(f"Could not extract account number from alert: {account_alert}")
        
        # Step 3: Verify customer appears in customers table
        customer_data = manager_page.verify_customer_in_table(
            first_name="John",
            last_name="Doe", 
            expected_post_code="12345",
            expected_account_number=created_account_number
        )
        print(f"✅ Manager flow verified! Customer {customer_data['first_name']} {customer_data['last_name']} created with account {created_account_number}")
        
        # Step 4: Click Home button to return to login page
        manager_page.click_home_button()
        print("✅ Clicked Home button - returned to login page")
        
        # Step 5: Create LoginPage with existing driver and navigate to customer login
        login_page = LoginPage(browser=None)  # Don't create new browser
        login_page.driver = manager_page.driver  # Use existing driver
        
        # Click Customer Login button
        login_page.click_login_button()
        login_page.wait_for_customer_page()
        print("✅ Navigated to customer page")
        
        # Step 6: Create CustomerPage with existing driver (similar to test2 flow)
        customer_page = CustomerPage(driver=manager_page.driver)
        
        # Step 7: Select John Doe and login (same as test2 but for John Doe)
        customer_page.select_customer_and_login("John Doe")
        assert customer_page.wait_for_account_page(), 'Account page not found'
        print(f"✅ Successfully logged in as John Doe and reached account page!")
        
        print(f"✅ Complete end-to-end flow successful: Manager created John Doe → Customer logged in as John Doe") 