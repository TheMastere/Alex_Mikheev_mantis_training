from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        delete_project_list = []
        for row in wd.find_elements_by_css_selector("table.width100 tr[class='row-1']") +\
                    wd.find_elements_by_css_selector("table.width100 tr[class='row-2']"):
            name = row.find_elements_by_css_selector("td")[0].text
            description = row.find_elements_by_css_selector("td")[4].text
            delete_project_list.append(Project(name=name, description=description))
        return delete_project_list

    def return_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def delete_project_by_name(self, name):
        self.open_project_page()
        wd = self.app.wd
        wd.find_element_by_link_text(name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def project_is_in_list(self, prj, prj_list):
        for pr in prj_list:
            if pr.name == prj.name:
                return True
        return False
