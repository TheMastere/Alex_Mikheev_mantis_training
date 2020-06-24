from selenium import webdriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_login_page(self):
        wd = self.wd
        wd.get("http://localhost/mantisbt-1.2.20/login_page.php")

    def open_project_page(self):
        wd = self.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create_project(self, project):
        wd = self.wd
        self.open_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.return_projects_page()

    def return_projects_page(self):
        wd = self.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def destroy(self):
        self.wd.quit()








