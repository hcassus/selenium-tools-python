from abc import ABCMeta, abstractmethod


class TableAssistant(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_value_by_position(self, row, column):
        pass

    @abstractmethod
    def count_rows(self):
        pass

    @abstractmethod
    def get_value_by_reference_column_index(self, reference_column_index, reference_column_value, actual_column_index):
        pass

