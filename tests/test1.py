import pytest

class Test1:
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge', 'firefox'])
    def test_click_login_button(self, run_all_browser):
        login_page = run_all_browser
        login_page.click_login_button()
        assert login_page.wait_for_customer_page(), 'Customer page not found after clicking Customer Login'