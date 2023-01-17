from selenium.webdriver.remote.webelement import WebElement
from typing import List

from selenium_base_new.base import SeleniumBase


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.nav_links: str = "#mainNavigationFobs>li"
        # self.NAV_LINK_TEXT = 'Women,Men,Kids,Home,Beauty,Shoes,Handbags,Jewelry,Furniture,Toys,Gifts,Trending,Sale'
        # self.sing_in_button: str = '#myRewardsLabel-status span'
        # self.SING_BUTTON = 'Sign In'
        # self.hi_there: str = '#media-rail'
        # self.hi_there_text = 'Free Shipping with $49 purchase or fast & free Store Pickup. Exclusions'
        # self.message = '#registry-link'
        # self.message_text = 'Wedding Registry'
        # self.join = 'p[class="message"]'
        # self.join_text = 'Join Star Rewards for free to unlock major benefits, track order & more.'
        self.name_text = 'Google'
        self.email = 'Google@gmail.com'
        self.current = 'Google'
        self.permanent = 'Google'


    def get_nav_links(self) -> List[WebElement]:
        return self.are_visiable('css', self.nav_links, 'Header Navigation links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links]
        return ",".join(nav_links_text)
    #
    # def get_button(self) -> WebElement:
    #     return self.is_visiable('css', self.sing_in_button, 'Sing in button')
    #
    # def get_button_text(self):
    #     button = self.get_button().text
    #     return button
    #
    # def get_hi_there(self):
    #     return self.is_visiable('CSS', self.hi_there, 'Text')
    #
    # def get_hi_there_text(self):
    #     text = self.get_hi_there().text
    #     return text
    #
    # def get_message(self):
    #     return self.is_visiable('CSS', self.message, 'Wedding')
    #
    # def get_message_text(self):
    #     text_message = self.get_message().text
    #     return text_message
    #
    def get_join(self):
        return self.is_visiable('CSS', self.join, 'Wedding')

    def get_join_text(self):
        text_join = self.get_join().text
        return text_join



    def find_full_name_field(self) -> WebElement:
        return self.is_visiable('css', '#userName', 'Name Field')

    def find_full_name_field_Email(self) -> WebElement:
        return self.is_visiable('css', '#userEmail', 'Email Field')

    def find_full_name_field_Current(self) -> WebElement:
        return self.is_visiable('css', '#currentAddress', 'CurrentAddress Field')

    def find_full_name_field_Permanent(self) -> WebElement:
        return self.is_visiable('css', '#permanentAddress', 'PermanentAddress Field')

    def button(self) -> WebElement:
        return self.is_visiable('css', '#submit', 'Button')

    def output_name(self):
        return self.is_visiable('css', 'p[id="name"]', 'Name Sub')

    def output_email(self):
        return self.is_visiable('css', '#email', 'Email Sub')

    def output_current(self):
        return self.is_visiable('css', 'p[id="currentAddress"]', 'Current Sub')

    def output_permanent(self):
        return self.is_visiable('css', 'p[id="permanentAddress"]', 'Permanent Sub')

    def get_output_name(self) -> str:
        return self.is_visiable('css', '#name', 'anytext').text

    def get_output_email(self):
        output_email = self.output_email().text.split(':')[1]
        return output_email

    def get_output_current(self):
        output_current = self.output_current().text.split(':')[1]
        return output_current

    def get_output_permanent(self):
        output_permanent = self.output_permanent().text.split(':')[1]
        return output_permanent
