from src.medicalrecord import MedicalRecord

r1 = MedicalRecord("Aliyah", "Dr. Brown", "Flu", ["Paracetamol", "Cough Syrup"], ["Blood Test"])
r2 = MedicalRecord("Omar", "Dr. Ahmed", "Diabetes Check")

print(r1.get_info())
r1.close_record()
print(r1.get_info())

print(r2.get_info())
