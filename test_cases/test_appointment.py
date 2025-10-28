from src.appointment import Appointment

a1 = Appointment("Aliyah", "Dr. Brown", "2025-10-29", "10:00 AM")
a2 = Appointment("Omar", "Dr. Ahmed", "2025-10-30", "11:30 AM")

print(a1.get_info())
a1.reschedule("2025-10-31", "1:00 PM")
print(a1.get_info())

a2.cancel()
print(a2.get_info())
