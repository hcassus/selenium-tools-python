from selenium.webdriver.common.by import By
from table_assistant.interfaces.titled_table_assistant import TitledTableAssistant

from selenium_tools.table_assistant.abstract import HeaderTableAssistant


class ExplicitHeaderTableAssistant(HeaderTableAssistant, TitledTableAssistant):
    def __init__(self, table_webelement):
        super(ExplicitHeaderTableAssistant, self).__init__(table_webelement)

    def _get_header_column_locator(self):
        return By.XPATH, "./thead/tr/*"
