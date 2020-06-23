# -*- coding: utf-8 -*-
import pytest
from project import Project
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_project(app):
    app.login(username="administrator", password="root")
    app.create_project(Project(name="myprojectred", description="gawgjkawgjoawgioawgjkaknkgwgwg"))
    app.logout()

