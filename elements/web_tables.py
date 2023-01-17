from selenium_base_new.base import SeleniumBase



class Elements(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.add_button_form = '#addNewRecordButton'
        self.first_name_form = 'input[id="firstName"]'
        self.last_name_form = 'input[id="lastName"]'
        self.age_form = 'input[id="age"]'
        self.email_form = 'input[id="userEmail"]'
        self.salary_form = 'input[id="salary"]'
        self.department_form = 'input[id="department"]'
        self.submit_button_form = 'input[id="department"]'
        self.search_box = 'input[id="searchBox"]'
        self.roll_box = 'select[aria-label="rows per page"]'
        self.roll_box = 'select[aria-label="rows per page"]'
        self.action_edit = '#edit-record-1'
        self.action_delete = '#delete-record-1'



    def find_yes(self):
        return self.is_visiable('css', self.button_yes, 'Yes')

    def find_impressive(self):
        return self.is_visiable('css', self.button_impressive, 'Impressive')

    def find_no(self):
        return self.is_visiable('css', self.button_yes, 'Yes')

    def get_output_result(self) -> str:
        return self.is_visiable('css', self.text_success, 'result_text').text
