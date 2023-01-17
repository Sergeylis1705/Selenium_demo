import time

import pytest

from homepage_nav.Homepage_nav import HomepageNav

@pytest.mark.usefixtures('setup')
class TestsForField:

    def test_for_field(self):
        driver = HomepageNav(self.driver)
        name_field = driver.find_full_name_field()
        name_field.send_keys('Google')
        time.sleep(2)
        email_field = driver.find_full_name_field_Email()
        email_field.send_keys('Google@gmail.com')
        time.sleep(2)
        current_field = driver.find_full_name_field_Current()
        current_field.send_keys('Google')
        time.sleep(2)
        permanent_field = driver.find_full_name_field_Permanent()
        permanent_field.send_keys('Google')
        time.sleep(2)
        button = driver.button()
        button.click()
        time.sleep(2)
        actual_name = driver.get_output_name()
        actual_email = driver.get_output_email()
        actual_current = driver.get_output_current()
        actual_permanent = driver.get_output_permanent()
        expected_name = driver.name_text
        expected_email = driver.email
        expected_current = driver.current
        expected_permanent = driver.permanent
        assert actual_name == expected_name
        assert actual_email == expected_email
        assert actual_current == expected_current
        assert actual_permanent == expected_permanent




