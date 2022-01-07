from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create_project(self, new_project):
        wd = self.app.wd
        self.open_project_list()
        # check button create project
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # Fill form for contact
        self.fill_project_field(new_project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def open_project_list(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()


    def fill_project_field(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_list()
        self.project_cache = []
        for row in wd.find_elements_by_css_selector("tr[class*='row-1']"):
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].text
            if name == "General":
                break
            description = cells[4].text
            self.project_cache.append(Project(name=name, description=description))
        for row in wd.find_elements_by_css_selector("tr[class*='row-2']"):
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].text
            if name == "General":
                break
            description = cells[4].text
            self.project_cache.append(Project(name=name, description=description))
        return list(self.project_cache)

    def delete_contact_by_name(self, name):
        wd = self.app.wd
        self.open_project_list()
        wd.find_element_by_link_text(name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//*/text()[normalize-space(.)='']/parent::*").click()























