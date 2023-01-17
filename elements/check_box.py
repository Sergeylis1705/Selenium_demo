from selenium_base_new.base import SeleniumBase



class Elements(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkboxes = 'span[class="rct-title"]'
        self.expand_all = 'button[title="Expand all"]'
        self.expected_checkboxes = ['Home', 'Desktop', 'Notes', 'Commands', 'Documents', 'WorkSpace', 'React', 'Angular',
                                    'Veu', 'Office', 'Public', 'Private', 'Classified', 'General', 'Downloads', 'Word File.doc', 'Excel File.doc']
        self.find_lists = 'svg[class="rct-icon rct-icon-expand-close"]'





    def find_expand_all(self):
        return self.is_visiable('css', self.expand_all, 'Sing in button')

    def find_checkboxes_list(self):
        return self.are_visiable('css', self.checkboxes, 'Header Navigation links')

    def get_checkboxes_text(self) -> str:
        checkboxes = self.find_checkboxes_list()
        checkboxes_text = [boxes.text for boxes in checkboxes]
        return ",".join(checkboxes_text)


