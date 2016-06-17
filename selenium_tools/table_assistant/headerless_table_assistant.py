from table_assistant.interfaces.table_assistant import TableAssistant

from selenium_tools.table_assistant.abstract import GeneralTableAssistant


class HeaderlessTableAssistant(GeneralTableAssistant, TableAssistant):
    def __init__(self, table_webelement):
        super(HeaderlessTableAssistant, self).__init__(table_webelement)
