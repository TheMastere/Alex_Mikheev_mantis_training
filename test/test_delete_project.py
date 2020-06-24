

from model.project import Project
import random

def test_delete_project(app):
    old_project = app.project.get_project_list()
    if (len(old_project)) == 0:
        new_project = Project(name="myprojectred", description="gawgjkawgjoawgioawgjkaknkgwgwg")
        app.project.create(new_project)
        old_project = app.project.get_project_list()
    pr = random.choice(old_project)
    app.project.delete_project_by_name(pr.name)
    old_project.remove(pr)
    new_project = app.project.get_project_list()
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)