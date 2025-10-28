class MedicalRecord:
    """Stores medical details for a specific patient visit."""

    def __init__(self, patient, doctor, diagnosis, medications=None, lab_tests=None):
        self.__patient = patient
        self.__doctor = doctor
        self.__diagnosis = diagnosis
        self.__medications = medications or []
        self.__lab_tests = lab_tests or []
        self.__status = "Open"

    def close_record(self):
        self.__status = "Closed"

    def get_info(self):
        return (f"Medical Record — Patient: {self.__patient}, Doctor: {self.__doctor}, "
                f"Diagnosis: {self.__diagnosis}, Medications: {', '.join(self.__medications) or 'None'}, "
                f"Lab Tests: {', '.join(self.__lab_tests) or 'None'}, Status: {self.__status}")

    def __str__(self):
        return self.get_info()
