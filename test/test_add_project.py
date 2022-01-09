# -*- coding: utf-8 -*-
def test_add_project(app, json_projects):
    project = json_projects
    old_projects = app.soap.get_list_mantis_projects()
    app.project.create_project(project)
    new_projects = app.soap.get_list_mantis_projects()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=lambda i: i.name) == sorted(new_projects, key=lambda i: i.name)
    print("OK")
