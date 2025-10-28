class Appointment:
    """Represents a patient appointment with a doctor."""

    def __init__(self, patient, doctor, date, time, status="Scheduled"):
        self.__patient = patient
        self.__doctor = doctor
        self.__date = date
        self.__time = time
        self.__status = status

    def reschedule(self, new_date, new_time):
        self.__date = new_date
        self.__time = new_time
        self.__status = "Rescheduled"

    def cancel(self):
        self.__status = "Cancelled"

    def get_info(self):
        return (f"Appointment: {self.__patient} with {self.__doctor} "
                f"on {self.__date} at {self.__time} — Status: {self.__status}")

    def __str__(self):
        return self.get_info()
