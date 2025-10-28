from src.clinic import Clinic
from src.department import Department
from src.doctor import Doctor

# Create objects
clinic = Clinic("City Care Clinic", "Dubai", "0501234567", "info@citycare.com", "www.citycare.ae")
dept = Department("Cardiology", "8 AM – 6 PM")
doc = Doctor(1, "Ahmed", "Heart Specialist", "9 AM – 5 PM")

# Link objects
dept.add_doctor(doc)
clinic.add_department(dept)

# Print test results
print(clinic.get_info())
print(dept.get_info())
print(doc.get_info())
print("Departments:", clinic.list_departments())
print("Doctors in Cardiology:", dept.list_doctors())
