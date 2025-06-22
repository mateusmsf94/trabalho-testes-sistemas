import pytest

class Test2:
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge', 'firefox'])
    def test_login_user_account(self, run_all_browser_customer):
        # Fixture gives us CustomerPage already on customer page (after login flow)
        customer_page = run_all_browser_customer
        
        # Select customer and login
        customer_page.select_customer_and_login("Harry Potter")
        assert customer_page.wait_for_account_page(), 'Account page not found'
        
        