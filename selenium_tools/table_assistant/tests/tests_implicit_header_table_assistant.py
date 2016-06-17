from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium_tools.table_assistant import TableAssistantTestCase
from ..implicit_header_table_assistant import ImplicitHeaderTableAssistant


class ImplicitHeaderTableAssistantTests(TableAssistantTestCase):
    @classmethod
    def setUpClass(cls):
        cls.table_locator = (By.ID, "test_table_without_explicit_headers")
        super(ImplicitHeaderTableAssistantTests, cls).setUpClass()
        cls.table_assist = ImplicitHeaderTableAssistant(cls.table)

    @classmethod
    def tearDownClass(cls):
        super(ImplicitHeaderTableAssistantTests, cls).tearDownClass()

    def test_line_count(self):
        self.assertEqual(4, self.table_assist.count_rows())

    def test_get_value_by_position_test(self):
        self.assertEqual(self.JAX_LAST_NAME,
                         self.table_assist.get_value_by_position(self.THIRD_ROW, self.LAST_NAME_COLUMN_INDEX))

    def test_get_value_by_column_index_reference(self):
        self.assertEqual(self.JAX_EMAIL,
                         self.table_assist.get_value_by_reference_column_index(self.USER_COLUMN_INDEX, self.JAX_USER,
                                                                               self.EMAIL_COLUMN_INDEX))

    def test_non_existing_reference_throws_exception(self):
        self.assertRaises(NoSuchElementException, self.table_assist.get_value_by_reference_column_index,
                          self.USER_COLUMN_INDEX, self.TARA_USER, self.EMAIL_COLUMN_INDEX)

    def test_get_value_by_column_name_and_row(self):
        self.assertEqual(self.JANE_EMAIL,
                         self.table_assist.get_value_by_column_name_and_row(self.EMAIL_COLUMN_NAME, self.SECOND_ROW))

    def test_get_value_by_reference_column_name(self):
        self.assertEqual(self.JAX_USER,
                         self.table_assist.get_value_by_reference_column_name(self.EMAIL_COLUMN_NAME, self.JAX_EMAIL,
                                                                              self.USER_COLUMN_NAME))
