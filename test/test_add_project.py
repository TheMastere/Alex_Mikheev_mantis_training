# -*- coding: utf-8 -*-
from model.project import Project
from datetime import datetime


def test_add_project(app):
    old_project = app.project.get_project_list()
    new_project = Project(name="myprojectred", description="gawgjkawgjoawgioawgjkaknkgwgwg")
    while app.project.project_is_in_list(prj=new_project, prj_list=old_project):
        new_project = Project(name=str(datetime.now()), description="gawgjkawgjoawgioawgjkaknkgwgwg")
    old_project.append(new_project)
    app.project.create_project(new_project)
    new_project = app.project.get_project_list()
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)

