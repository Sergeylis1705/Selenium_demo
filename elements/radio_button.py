from selenium_base_new.base import SeleniumBase



class Elements(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.button_yes = 'label[for="yesRadio"]'
        self.button_impressive = 'label[for="impressiveRadio"]'
        self.button_no = 'label[for="noRadio"]'
        self.text_success = 'span[class="text-success"]'

    def find_yes(self):
        return self.is_visiable('css', self.button_yes, 'Yes')

    def find_impressive(self):
        return self.is_visiable('css', self.button_impressive, 'Impressive')

    def find_no(self):
        return self.is_visiable('css', self.button_yes, 'Yes')

    def get_output_result(self) -> str:
        return self.is_visiable('css', self.text_success, 'result_text').text



