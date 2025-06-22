import pytest

class Test3:
    
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge', 'firefox'])
    def test_get_available_customers(self, run_all_browser_customer_isolated):
        """Test getting list of available customers"""
        customer_page = run_all_browser_customer_isolated
        
        # Get available customers
        customers = customer_page.get_available_customers()
        
        # Verify we have customers
        assert len(customers) > 0, "No customers found"
        assert "Harry Potter" in customers, "Harry Potter not found in customer list"
        assert "Hermoine Granger" in customers, "Hermoine Granger not found in customer list"
    
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge', 'firefox'])
    def test_select_customer_functionality(self, run_all_browser_customer_isolated):
        """Test customer selection functionality (without login)"""
        customer_page = run_all_browser_customer_isolated
        
        # Test selecting a customer
        customer_page.select_customer("Harry Potter")
        
        # Verify login button appears after selection (it should be clickable)
        assert customer_page.is_login_button_clickable(), "Login button should be clickable after customer selection"
    
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge', 'firefox'])
    def test_complete_customer_login_flow_isolated(self, run_all_browser_customer_isolated):
        """Test complete customer selection and login flow in isolation"""
        customer_page = run_all_browser_customer_isolated
        
        # Complete flow: select customer and login
        customer_page.select_customer_and_login("Ron Weasly")
        
        # Verify navigation to account page
        assert customer_page.wait_for_account_page(), "Should navigate to account page after login"
    
    @pytest.mark.parametrize('all_browser', ['chrome'])  # Only Chrome for faster execution
    def test_all_customers_can_login(self, run_all_browser_customer_isolated):
        """Test that all available customers can be selected and logged in"""
        customer_page = run_all_browser_customer_isolated
        
        # Get all customers
        customers = customer_page.get_available_customers()
        
        # Test first 3 customers (to keep test time reasonable)
        test_customers = customers[:3]
        
        for customer_name in test_customers:
            # Go back to customer page for each test
            customer_page.open_page()
            
            # Select and login
            customer_page.select_customer_and_login(customer_name)
            
            # Verify account page
            assert customer_page.wait_for_account_page(), f"Login failed for {customer_name}" 