from abc import abstractmethod

from general_table_assistant import GeneralTableAssistant
from ..interfaces.titled_table_assistant import TitledTableAssistant


class HeaderTableAssistant(GeneralTableAssistant, TitledTableAssistant):
    def __init__(self, table):
        super(HeaderTableAssistant, self).__init__(table)
        self.column_indexes = None
        self.header_column_locator = self._get_header_column_locator()

    @abstractmethod
    def _get_header_column_locator(self):
        pass

    def get_value_by_column_name_and_row(self, column_name, row):
        self.initialize_columns()
        column_index = self.get_column_index(column_name)
        return self.get_value_by_position(row, column_index)

    def get_value_by_reference_column_name(self, reference_column_name, reference_column_value, actual_column_name):
        self.initialize_columns()
        reference_column_index = self.get_column_index(reference_column_name)
        actual_column_index = self.get_column_index(actual_column_name)
        actual_row_index = self._get_row_index(reference_column_index, reference_column_value)
        return self.get_value_by_position(actual_row_index, actual_column_index)

    def get_column_index(self, column_name):
        return self.column_indexes[column_name]

    def initialize_columns(self):
        if self.column_indexes is None:
            self.column_indexes = dict()

            headers = self.table.find_elements(*self.header_column_locator)
            index = 1
            for header in headers:
                text = header.text
                self.column_indexes[text] = index
                index += 1
