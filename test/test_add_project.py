# -*- coding: utf-8 -*-
from model.project import Project
from datetime import datetime

def test_add_project(app):
    #app.session.login("administrator", "root")
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_projects = app.soap.get_project_list(username, password)
    new_project = Project(name="myprojectred", description="gawgjkawgjoawgioawgjkaknkgwgwg")
    while app.project.project_is_in_list(prj=new_project, prj_list=old_projects):
        new_project = Project(name=str(datetime.now()), description="gawgjkawgjoawgioawgjkaknkgwgwg")
    old_projects.append(new_project)
    app.project.create_project(new_project)
    new_projects = app.soap.get_project_list(username, password)
    assert len(old_projects) == len(new_projects)



