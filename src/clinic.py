class Clinic:
    def __init__(self, name, address, contact_number, email, website):
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.email = email
        self.website = website
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def list_departments(self):
        return [d.dept_name for d in self.departments]

    def get_info(self):
        return f"{self.name}, located at {self.address}"