from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from ..interfaces.table_assistant import TableAssistant

ROW_XPATH = "./tbody/tr"

CELL_XPATH = "{0}[{1}]/td[{2}]".format(ROW_XPATH,"{0}","{1}")


class GeneralTableAssistant(TableAssistant):

    def __init__(self, table):
        self.table = table

    def get_value_by_position(self, row, column):
        final_xpath = CELL_XPATH.format(row, column)
        cell = self.table.find_element(By.XPATH, final_xpath)
        return cell.text

    def _get_rows(self):
        return self.table.find_elements(By.XPATH, ROW_XPATH)

    def count_rows(self):
        rows = self._get_rows()
        return len(rows)

    def _get_row_index(self, reference_column_index, reference_value):
        rows = self._get_rows()
        rownum = 0
        for row in rows:
            rownum += 1
            cell = row.find_element(By.XPATH, "./td["+str(reference_column_index)+"]")
            text = cell.text
            if text == reference_value:
                return rownum
        raise NoSuchElementException("No rows match the given criteria: reference column: " + str(reference_column_index) + ", reference value: " + str(reference_value))

    def get_value_by_reference_column_index(self, reference_column_index, reference_column_value, actual_column_index):
        actual_row_index = self._get_row_index(reference_column_index, reference_column_value)
        return self.get_value_by_position(actual_row_index, actual_column_index)
