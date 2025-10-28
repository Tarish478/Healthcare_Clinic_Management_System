class LabOrder:
    def __init__(self, order_id, patient_name, test_type, result=None):
        self.order_id = order_id
        self.patient_name = patient_name
        self.test_type = test_type
        self.result = result

    def add_result(self, result):
        self.result = result

    def __str__(self):
        return f"Lab Order {self.order_id}: {self.test_type} for {self.patient_name} - Result: {self.result or 'Pending'}"
