from configparser import ConfigParser

class Base:
    def __init__(self,driver):
        cf = ConfigParser()
        cf.read("conf.conf")
        self.base_url = cf.get("basic","url")
        self.driver = driver

    def _open(self):
        url = self.base_url
        self.driver.get(url)

    def open(self):
        self._open()

    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    