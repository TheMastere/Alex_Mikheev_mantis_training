

from model.project import Project
import random

def test_delete_project(app):
    app.session.login("administrator", "root")
    old_project = app.project.get_project_list()
    if (len(old_project)) == 0:
        new_project = Project(name="myprojectred", description="gawgjkawgjoawgioawgjkaknkgwgwg")
        app.project.create_project(new_project)
        old_project = app.project.get_project_list()
    pr = random.choice(old_project)
    app.project.delete_project_by_name(pr.name)
    old_project.remove(pr)
    new_project = app.project.get_project_list()
    assert len(old_project) == len(new_project)