from __future__ import print_function
from unittest.case import TestCase
from selenium import webdriver
import os


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
        cls.driver = webdriver.Chrome()
        path = "file://"+os.path.abspath("table_assistant/tests/sample.html")
        cls.driver.get(path)
        cls.table = cls.driver.find_element(*cls.table_locator)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()