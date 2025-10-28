class Doctor:
    def __init__(self, id, name, specialization, working_hours):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.working_hours = working_hours

    def get_info(self):
        return f"Dr. {self.name}, {self.specialization}, Hours: {self.working_hours}"
