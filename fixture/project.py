from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
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
        proj_name = ["tr.row-1", "tr.row-2"]
        for name in proj_name:
            elements = wd.find_elements_by_css_selector(name)
            for element in elements:
                cells = element.find_elements_by_css_selector("td")
                address = cells[0].find_element_by_tag_name("a").get_attribute("href")
                project_name = cells[0].text
                pr = address.index("=")
                project_id = address[pr+1:len(address)]
                project_description = cells[4].text
                delete_project_list.append(Project(id=project_id, name=project_name, description=project_description))
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

    def project_list(self, prj, prj_list):
        for pr in prj_list:
            if pr.name == prj.name:
                return True
        return False