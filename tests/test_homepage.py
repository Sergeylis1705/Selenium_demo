import pytest

from homepage_nav.Homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_limks = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert actual_limks == expected_links, 'Validating Nav Links Test'

    def test_button(self):
        homepage_nav = HomepageNav(self.driver)
        actual_button = homepage_nav.get_button_text()
        expected_button = homepage_nav.SING_BUTTON
        assert actual_button == expected_button, 'Validating Sing IN Button'

    def test_text(self):
        homepage_nav = HomepageNav(self.driver)
        actual_text = homepage_nav.get_hi_there_text()
        expected_text = homepage_nav.hi_there_text
        assert actual_text == expected_text, 'Text'

    def test_message(self):
        homepage_nav = HomepageNav(self.driver)
        actual_message = homepage_nav.get_message_text()
        expected_message = homepage_nav.message_text
        assert actual_message == expected_message, 'Message text'

    def test_join(self):
        homepage_nav = HomepageNav(self.driver)
        actual_join = homepage_nav.get_join_text()
        expected_join = homepage_nav.join_text
        assert actual_join == expected_join, 'join text'
