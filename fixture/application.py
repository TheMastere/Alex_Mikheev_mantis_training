from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.project = ProjectHelper

    def open_login_page(self):
        wd = self.wd
        wd.get("http://localhost/mantisbt-1.2.20/login_page.php")

    def destroy(self):
        self.wd.quit()








