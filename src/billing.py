class Billing:
    """Handles billing information for patient visits."""
    def __init__(self, patient_name, total_amount, insurance_coverage=0):
        self.__patient_name = patient_name
        self.__total_amount = total_amount
        self.__insurance_coverage = insurance_coverage
        self.__paid = False

    def apply_insurance(self):
        return self.__total_amount - (self.__total_amount * self.__insurance_coverage / 100)

    def mark_paid(self):
        self.__paid = True

    def get_info(self):
        return f"Billing for {self.__patient_name}: AED {self.apply_insurance()}, Paid: {self.__paid}"
