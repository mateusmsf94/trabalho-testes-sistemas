import pytest

class Test4:
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge', 'firefox'])
    def test_click_manager_login_button(self, run_all_browser):
        login_page = run_all_browser
        login_page.click_manager_login_button()
        assert login_page.wait_for_manager_page(), 'Manager page not found after clicking Bank Manager Login' 