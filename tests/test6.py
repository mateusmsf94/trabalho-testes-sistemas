import pytest

class Test6:
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge', 'firefox'])
    def test_manager_add_customer_and_open_account(self, run_all_browser_manager):
        # Fixture gives us ManagerPage already on manager page (after login flow)
        manager_page = run_all_browser_manager
        
        # Step 1: Add a new customer (continuing from test5 flow)
        manager_page.add_customer("John", "Doe", "12345")
        
        # Assert the success alert appears with correct message and click OK
        add_customer_alert = manager_page.wait_and_assert_customer_added_alert()
        print(f"✅ Customer added successfully! Alert message: {add_customer_alert}")
        
        # Step 2: Open account for the newly added customer
        # Search for customer containing "doe" to handle any name variations
        selected_customer = manager_page.open_account_for_customer("doe", "Dollar")
        
        # Assert the account creation success alert and click OK
        account_alert = manager_page.wait_and_assert_account_created_alert()
        print(f"✅ Account opened successfully for {selected_customer}! Alert message: {account_alert}") 