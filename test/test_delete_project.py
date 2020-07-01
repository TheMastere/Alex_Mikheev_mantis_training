

from model.project import Project
import random

def test_delete_project(app):
    #app.session.login("administrator", "root")
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_project = app.soap.get_project_list(username, password)
    if (len(old_project)) == 0:
        new_project = Project(name="myprojectred", description="gawgjkawgjoawgioawgjkaknkgwgwg")
        app.project.create_project(new_project)
        old_project = app.soap.get_project_list(username, password)
    pr = random.choice(old_project)
    app.project.delete_project_by_name(pr.name)
    old_project.remove(pr)
    new_project = app.soap.get_project_list(username, password)
    assert len(old_project) == len(new_project)