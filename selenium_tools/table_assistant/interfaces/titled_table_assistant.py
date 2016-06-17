from abc import abstractmethod

from table_assistant import TableAssistant


class TitledTableAssistant(TableAssistant):
    @abstractmethod
    def get_value_by_reference_column_name(self, reference_column_name, reference_column_value, actual_column_name):
        pass

    @abstractmethod
    def get_value_by_column_name_and_row(self, column_name, row):
        pass
