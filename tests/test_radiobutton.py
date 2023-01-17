import time

import pytest

from elements.radio_button import Elements

@pytest.mark.usefixtures('setup')
class TestsForRadioButton:

    def test_radio_buttons(self):
        driver = Elements(self.driver)
        driver.find_yes().click()
        output_yes = driver.get_output_result()
        driver.find_impressive().click()
        output_impressive = driver.get_output_result()
        driver.find_no().click()
        output_no = driver.get_output_result()

        assert output_yes == 'Yes'
        assert output_impressive == 'Impressive'
        assert output_no == 'No'