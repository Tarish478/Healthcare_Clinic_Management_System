class Prescription:
    def __init__(self, prescription_id, patient_name, doctor_name, medicine, dosage):
        self.prescription_id = prescription_id
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.medicine = medicine
        self.dosage = dosage

    def __str__(self):
        return f"Prescription {self.prescription_id}: {self.medicine} ({self.dosage}) for {self.patient_name}"
