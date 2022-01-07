from model.project import Project
import random

def test_delete_random_contact(app):
    config = app.config['web']
    if len(app.soap.get_list_mantis_projects(config['username'], config['password'])) == 0:
        app.project.create_project(Project(name="ProjectName"))
    old_projects = app.soap.get_list_mantis_projects(config['username'], config['password'])
    project = random.choice(old_projects)
    app.project.delete_contact_by_name(project.name)
    new_projects = app.soap.get_list_mantis_projects(config['username'], config['password'])
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=lambda i: i.name) == sorted(new_projects, key=lambda i: i.name)
