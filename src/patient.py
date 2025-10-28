class Patient:
    """Represents a patient with personal, contact, and insurance details."""

    def __init__(self, name, dob, contact, address, insurance, allergies=None):
        self.__name = name
        self.__dob = dob
        self.__contact = contact
        self.__address = address
        self.__insurance = insurance
        self.__allergies = allergies or []
        self.__medical_history = []

    def add_medical_history(self, record):
        self.__medical_history.append(record)

    def get_info(self):
        return (f"Patient: {self.__name}, DOB: {self.__dob}, Contact: {self.__contact}, "
                f"Insurance: {s
