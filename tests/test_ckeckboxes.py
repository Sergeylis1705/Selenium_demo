import time

import pytest

from elements.check_box import Elements

@pytest.mark.usefixtures('setup')
class TestsForCheckboxes:

    def test_checkboxes(self):
        driver = Elements(self.driver)
        expand_all = driver.find_expand_all()
        expand_all.click()
        time.sleep(2)
        actual_text = driver.get_checkboxes_text()
        expected_text = driver.expected_checkboxes()
        assert actual_text == expected_text, 'Text'