from src.billing import Billing

b1 = Billing("Aliyah", 500, 20)
b2 = Billing("Omar", 800, 10)

print(b1.get_info())
b1.mark_paid()
print(b1.get_info())

print(b2.get_info())
