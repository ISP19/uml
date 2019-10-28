from .slot import Slot
from .errors import ParkinglotError


class Parkinglot():
    def __init__(self, slot_count=1):
        self.slots = self.create_slots(slot_count)
        self.registration_numbers_record = []

    @staticmethod
    def create_slots(slot_count):
        return [Slot(id) for id in range(1, slot_count+1)]

    def car_in(self, car):
        slot = self.get_nearest_available_slot()
        slot.is_available = False
        slot.car = car

    def car_out(self, slot_id):
        for slot in self.slots:
            if slot.id == slot_id:
                slot.is_available = True
                slot.car = None

    def get_nearest_available_slot(self):
        for slot in self.slots:
            if slot.is_available:
                return slot
        else:
            raise ParkinglotError('Parkinglot is full')

    def record_car_info(self, car):
        self.registration_numbers_record.append(car.registration_number)
