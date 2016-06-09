from selenium.webdriver.common.by import By

from table_assistant.abstract.header_table_assistant import HeaderTableAssistant
from table_assistant.interfaces.titled_table_assistant import TitledTableAssistant


class ImplicitHeaderTableAssistant(HeaderTableAssistant, TitledTableAssistant):
    def __init__(self, table_webelement):
        super(ImplicitHeaderTableAssistant, self).__init__(table_webelement)
        self.header_lines = 1

    def _get_header_column_locator(self):
        return By.XPATH, "./tbody/tr[1]/*"

    def count_rows(self):
        return super(ImplicitHeaderTableAssistant, self).count_rows() - self.header_lines

    def get_value_by_position(self, row, column):
        return super(ImplicitHeaderTableAssistant, self).get_value_by_position(row + self.header_lines, column)

    def _get_row_index(self, reference_column_index, reference_value):
        return super(ImplicitHeaderTableAssistant, self)._get_row_index(reference_column_index,
                                                                        reference_value) - self.header_lines
