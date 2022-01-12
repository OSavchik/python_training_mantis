from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        config = self.app.config['web']
        client = Client("%s/api/soap/mantisconnect.php?wsdl" % config['baseUrl'])
        try:
           list = client.service.mc_login(username, password)
           return True
        except WebFault:
            return False


    def get_list_mantis_projects(self):
        config = self.app.config['web']
        client = Client("%s/api/soap/mantisconnect.php?wsdl" % config['baseUrl'])
        self.project_cache = []
        mantis_projects = client.service.mc_projects_get_user_accessible(config['username'], config['password'])
        for project in mantis_projects:
            self.project_cache.append(Project(name=project.name, description=project.description))
        return list(self.project_cache)

