from src.patient import Patient

p1 = Patient("Aliyah", "1999-05-03", "0501122334", "Dubai", "Daman", ["Penicillin"])
p2 = Patient("Omar", "1988-11-22", "0509876543", "Abu Dhabi", "AXA")

p1.add_medical_history("Asthma")
p2.add_medical_history("High Blood Pressure")

print(p1.get_info())
print(p2.get_info())
