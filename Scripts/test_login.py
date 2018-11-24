import pytest

from Base.get_driver import get_driver
from Page.page_login import PageLogin









class TestLogin():
    #实例化
    def setup_class(self):
        self.login = PageLogin(get_driver())

    def teardown_class(self):
        self.login.driver.quit()

    def test_login(self,username="147257368",pwd="2131"):
        self.login.page_input_username(username)
        self.login.page_input_pwd(pwd)
        self.login.page_click_login_btn()
if __name__ == '__main__':
    pytest.main("-s test_login.py")