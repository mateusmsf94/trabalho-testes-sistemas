import pytest

class Test5:
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge', 'firefox'])
    def test_manager_add_customer(self, run_all_browser_manager):
        # Fixture gives us ManagerPage already on manager page (after login flow)
        manager_page = run_all_browser_manager
        
        # Add a new customer
        manager_page.add_customer("John", "Doe", "12345")
        
        # Assert the success alert appears with correct message and click OK
        alert_text = manager_page.wait_and_assert_customer_added_alert()
        assert "John" not in alert_text or "Doe" not in alert_text, "Alert should not contain customer name details"
        
        print(f"✅ Customer added successfully! Alert message: {alert_text}") 