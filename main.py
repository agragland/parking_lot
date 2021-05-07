# Parking Lot Project - Andrew Ragland
import time


class Vehicle:
    def __init__(self, v_type, plate):
        self.type = v_type
        self.plate = plate
        self.entry_time = time.time()

    def get_type(self):
        return self.type

    def get_plate(self):
        return self.plate

    def get_entry_time(self):
        return self.entry_time

    def get_vehicle(self):
        return self.type, self.plate, self.entry_time


class Spot:
    def __init__(self):
        self.vehicle = None
        self.occupied = False

    def add_vehicle(self, v_type, plate):
        self.vehicle = Vehicle(v_type, plate)
        self.occupied = True

    def remove_vehicle(self):
        v_exit = self.vehicle
        self.vehicle = None
        self.occupied = False
        return v_exit

    def vehicle_info(self):
        return self.vehicle

    def is_available(self):
        return self.occupied


def display_spaces(spaces, avail):
    output = "SPOTS AVAILABLE: " + str(avail) + "\n"
    output += "|-------------------------------|\n"
    output += "|"
    for i in range(len(spaces)):
        if not spaces[i].occupied:
            output += "[ ]"
        else:
            output += "["
            output += "c" if spaces[i].vehicle_info().get_type() == "car" \
                else "t" if spaces[i].vehicle_info().get_type() == "truck" else "m"
            output += "]"
        if i < len(spaces) - 1:
            output += " "
    output += "|\n"
    output += "|-------------------------------|\n"

    print(output)


def remove_vehicle(spaces, plate):
    removed = None
    for space in spaces:
        if space.vehicle_info().get_plate() == plate:
            removed = space.remove_vehicle()
            break
            # redundant

            # calculate fare
    fare_calculation(removed)

def fare_calculation(vehicle):
    total_time = time.time() - vehicle.get_entry_time()
    rate = 0.0
    if vehicle.get_type() == "car":
        rate = total_time * 3.50
    elif vehicle.get_type() == "truck":
        rate = total_time * 4.50
    else:
        rate = total_time * 2.50

    print("Your Total for " + "{:.2f}".format(total_time) + " hours is $" + "{:.2f}".format(rate))


def main():
    # generate 8 spots
    spaces = []
    avail_spaces = 8
    total_spaces = 8
    for i in range(8):
        spaces.append(Spot())

    # add vehicles based on availability
    # search the lot, fill empty spaces, allow only unique plate numbers
    for k in range(3):
        if not spaces[k].occupied:
            spaces[k].add_vehicle("car", "aaa-bbbb")
            avail_spaces -= 1
        elif spaces[k].vehicle_info().get_plate() == "aaa-bbbb":
            break

    for k in range(5):
        if not spaces[k].occupied:
            spaces[k].add_vehicle("truck", "aaa-cccc")
            avail_spaces -= 1
        elif spaces[k].vehicle_info().get_plate() == "aaa-cccc":
            break

    time.sleep(5)

    remove_vehicle(spaces, "aaa-bbbb")
    avail_spaces += 1

    display_spaces(spaces, avail_spaces)


if __name__ == '__main__':
    main()
