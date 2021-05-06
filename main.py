# Parking Lot Project - Andrew Ragland
import time


class Vehicle:
    def __init__(self, v_type, dl_num):
        self.type = v_type
        self.dl_num = dl_num
        self.entry_time = time.time()

    def get_type(self):
        return self.type

    def get_dl_num(self):
        return self.dl_num

    def get_entry_time(self):
        return self.entry_time

    def get_vehicle(self):
        return self.type, self.dl_num, self.entry_time


class Spot:
    def __init__(self):
        self.vehicle = None
        self.occupied = False

    def add_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.occupied = True

    def remove_vehicle(self):
        v_exit = self.vehicle
        self.vehicle = None
        self.occupied = False
        return v_exit

    def get_spot(self):
        if self.vehicle is None:
            return None, self.occupied
        else:
            return self.vehicle.get_vehicle(), self.occupied


def main():
    test_spot = Spot()

    test_spot.add_vehicle(Vehicle("car", 12345))

    print(test_spot.get_spot())

    test_spot.remove_vehicle()

    print(test_spot.get_spot())


if __name__ == '__main__':
    main()
