import pytest

class Test9:
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge', 'firefox'])
    def test_customer_deposit_flow(self, run_all_browser_account):
        # Fixture gives us AccountPage already on account page (after customer login from test2 flow)
        account_page = run_all_browser_account
        
        # Verify we're on the account page and get initial info
        assert account_page.wait_for_account_page(), "Account page not loaded properly"
        
        # Get account information
        account_info = account_page.get_account_info()
        print(f"✅ Logged in as: {account_info['customer_name']}")
        print(f"✅ Account Number: {account_info['account_number']}")
        print(f"✅ Initial Balance: {account_info['balance']}")
        print(f"✅ Currency: {account_info['currency']}")
        print(f"✅ Available Accounts: {account_info['available_accounts']}")
        
        # Verify customer is Harry Potter (from test2 flow)
        assert account_info['customer_name'] == "Harry Potter", f"Expected Harry Potter, but got {account_info['customer_name']}"
        
        # Store initial balance
        initial_balance = account_info['balance']
        
        # Step 1: Make a deposit of 1000
        deposit_amount = 1000
        final_balance = account_page.make_deposit(deposit_amount)
        
        # Step 2: Assert balance is updated correctly
        expected_balance = initial_balance + deposit_amount
        assert final_balance == expected_balance, f"Expected balance {expected_balance}, but got {final_balance}"
        
        # Additional verification - get fresh account info
        updated_account_info = account_page.get_account_info()
        assert updated_account_info['balance'] == expected_balance, f"Balance verification failed: expected {expected_balance}, got {updated_account_info['balance']}"
        
        print(f"✅ Deposit successful! Balance updated from {initial_balance} to {final_balance}")
        print(f"✅ Deposit flow completed: Added {deposit_amount}, final balance = {final_balance}") 