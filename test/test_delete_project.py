from model.project import Project
import random

def test_delete_random_contact(app):
    if len(app.soap.get_list_mantis_projects()) == 0:
        app.project.create_project(Project(name="ProjectName"))
    old_projects = app.soap.get_list_mantis_projects()
    project = random.choice(old_projects)
    app.project.delete_contact_by_name(project.name)
    new_projects = app.soap.get_list_mantis_projects()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=lambda i: i.name) == sorted(new_projects, key=lambda i: i.name)
