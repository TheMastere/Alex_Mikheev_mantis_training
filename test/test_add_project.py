# -*- coding: utf-8 -*-
import pytest
from model.project import Project
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_project(app):
    app.session.login(username="administrator", password="root")
    app.project.create(Project(name="myprojectred", description="gawgjkawgjoawgioawgjkaknkgwgwg"))
    app.session.logout()

