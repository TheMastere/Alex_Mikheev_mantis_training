# -*- coding: utf-8 -*-
from model.project import Project
from datetime import datetime

def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    new_project = Project(name="myprojectred", description="gawgjkawgjoawgioawgjkaknkgwgwg")
    while app.project.project_is_in_list(prj=new_project, prj_list=old_projects):
        new_project = Project(name=str(datetime.now()), description="gawgjkawgjoawgioawgjkaknkgwgwg")
    old_projects.append(new_project)
    app.project.create_project(new_project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) == len(new_projects)



