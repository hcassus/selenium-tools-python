from __future__ import print_function

import os
from unittest.case import TestCase

from selenium_tools.table_assistant.tests.utils.browser_manager import BrowserManager


class TableAssistantTestCase(TestCase):
    EMAIL_COLUMN_NAME = "E-mail"

    USER_COLUMN_NAME = "User"

    TARA_USER = "tara.teller"

    JAX_USER = "jack.teller"

    JANE_EMAIL = "jane.doe@gmail.com"

    JAX_EMAIL = "jack.teller@tellermorrow.com"

    JAX_LAST_NAME = "Teller"

    USER_COLUMN_INDEX = 3

    LAST_NAME_COLUMN_INDEX = 2

    EMAIL_COLUMN_INDEX = 4

    THIRD_ROW = 3

    SECOND_ROW = 2

    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserManager().get_chrome_browser()
        path = "file://" + os.path.abspath("selenium_tools/table_assistant/tests/sample.html")
        cls.driver.get(path)
        cls.table = cls.driver.find_element(*cls.table_locator)
