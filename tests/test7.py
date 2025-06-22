import pytest
import re

class Test7:
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge', 'firefox'])
    def test_manager_complete_flow_with_customer_verification(self, run_all_browser_manager):
        # Fixture gives us ManagerPage already on manager page (after login flow)
        manager_page = run_all_browser_manager
        
        # Step 1: Add a new customer (continuing from test6 flow)
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
        
        # Extract account number from the alert message
        # Alert format: "Account created successfully with account Number :1016"
        account_number_match = re.search(r'account Number :\s*(\d+)', account_alert, re.IGNORECASE)
        if account_number_match:
            created_account_number = account_number_match.group(1)
            print(f"✅ Extracted account number: {created_account_number}")
        else:
            raise AssertionError(f"Could not extract account number from alert: {account_alert}")
        
        # Step 3: Verify customer appears in customers table with correct data
        customer_data = manager_page.verify_customer_in_table(
            first_name="John",
            last_name="Doe", 
            expected_post_code="12345",
            expected_account_number=created_account_number
        )
        
        print(f"✅ Complete flow verified! Customer {customer_data['first_name']} {customer_data['last_name']} is in the table with postal code {customer_data['post_code']} and account number {created_account_number}") 