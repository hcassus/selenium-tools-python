from selenium_tools.table_assistant.tests.utils.browser_manager import BrowserManager


def tearDownModule():
    browser_manager = BrowserManager()
    browser_manager.quit_chrome_browser()
