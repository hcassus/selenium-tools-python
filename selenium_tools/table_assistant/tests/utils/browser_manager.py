from selenium import webdriver


class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]


class BrowserManager(Singleton):
    chrome_driver = None

    def get_chrome_browser(self):
        if self.chrome_driver is None:
            self.chrome_driver = webdriver.Chrome()
        return self.chrome_driver

    def quit_chrome_browser(self):
        self.chrome_driver.quit()
        self.chrome_driver = None
