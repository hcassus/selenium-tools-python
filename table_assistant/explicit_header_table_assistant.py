from selenium.webdriver.common.by import By

from table_assistant.abstract.header_table_assistant import HeaderTableAssistant
from table_assistant.interfaces.titled_table_assistant import TitledTableAssistant

class ExplicitHeaderTableAssistant(HeaderTableAssistant, TitledTableAssistant):

    def __init__(self, table):
        super(ExplicitHeaderTableAssistant, self).__init__(table)

    def _get_header_column_locator(self):
        return By.XPATH, "./thead/tr/*"
