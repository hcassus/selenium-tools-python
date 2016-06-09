from table_assistant.abstract.general_table_assistant import GeneralTableAssistant

from table_assistant.interfaces.table_assistant import TableAssistant


class HeaderlessTableAssistant(GeneralTableAssistant, TableAssistant):
    def __init__(self, table_webelement):
        super(HeaderlessTableAssistant, self).__init__(table_webelement)
