class Department:
    def __init__(self, dept_name, operating_hours):
        self.dept_name = dept_name
        self.operating_hours = operating_hours
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def list_doctors(self):
        return [d.name for d in self.doctors]

    def get_info(self):
        return f"Department: {self.dept_name}, Hours: {self.operating_hours}"
