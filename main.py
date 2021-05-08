# Parking Lot Project - Andrew Ragland
import time, os

spaces = []
avail_spaces = 8
total_spaces = 8

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

    def add_vehicle(self, vehicle):
        self.vehicle = vehicle
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


def display_spaces():
    global spaces
    global avail_spaces
    output = "SPOTS AVAILABLE: " + str(avail_spaces) + "\n"
    output += "|-------------------------------|\n"
    output += "|"
    for space in spaces:
        if not space.occupied:
            output += "[ ]"
        else:
            output += "["
            output += "c" if space.vehicle_info().get_type() == 1 \
                else "t" if space.vehicle_info().get_type() == 2 \
                else "m"
            output += "]"
        if spaces.index(space) < len(spaces) - 1:
            output += " "
    output += "|\n"
    output += "|-------------------------------|\n"

    # only uncomment when running on linux machine
    # os.system("clear")
    print(output)


# FUNCTIONS FOR PARKING A VEHICLE #
def enter_vehicle(v_type, plate):
    global spaces, avail_spaces

    for uniq in spaces:
        if uniq.occupied:
            if uniq.vehicle_info().get_plate() == plate:
                display_spaces()
                print("Error: Vehicle Already In Lot")
                time.sleep(2)
                return

    for space in spaces:
        if not space.occupied:
            new_vehicle = Vehicle(v_type, plate)
            space.add_vehicle(new_vehicle)
            avail_spaces -= 1
            display_spaces()
            print("Vehicle Added to Lot!\n"
                  "Time Entered: " + str(time.strftime('%I:%M %p',
                                                       time.localtime(new_vehicle.get_entry_time()))))
            time.sleep(2)
            break


# FUNCTIONS FOR EXITING THE LOT #
def fare_calculation(vehicle):
    total_time = time.time() - vehicle.get_entry_time()
    rate = 0.0
    if vehicle.get_type() == "car":
        rate = total_time * 3.50
    elif vehicle.get_type() == "truck":
        rate = total_time * 4.50
    else:
        rate = total_time * 2.50

    ret = "Your Total for " + "{:.2f}".format(total_time) + " hours is $" + "{:.2f}".format(rate)

    return ret


def exit_lot(plate):
    global spaces, avail_spaces
    removed = None
    for space in spaces:
        if space.occupied:
            if space.vehicle_info().get_plate() == plate:
                removed = space.remove_vehicle()
                avail_spaces += 1
                break

    # calculate fare
    print(fare_calculation(removed))
    time.sleep(2)


# HANDLING USER COMMANDS #
def command_handler(command):
    if command == "P":
        display_spaces()
        new_type = int(input("Enter Vehicle Type:\n"
                             "1. Car\n"
                             "2. Truck\n"
                             "3. Motorcycle\n"
                             ">"))
        display_spaces()
        new_plate = input("Enter New Vehicle Plate Number:\n"
                          ">")
        enter_vehicle(new_type, new_plate)

    elif command == "E":
        display_spaces()
        exit_plate = input("Enter Vehicle Plate Number:\n"
                           ">")
        display_spaces()
        exit_lot(exit_plate)

    elif command == "R":
        display_spaces()
        input("Current Parking Rates:\n"
              "Cars - $3.50/hour\n"
              "Trucks - $4.50/hour\n"
              "Motorcycles - $2.00/hour\n"
              "\nPress Enter to return to menu")
    elif command == "quit":
        return
    else:
        display_spaces()
        print("Error: Invalid Command")
        time.sleep(1)


def main():
    global spaces, avail_spaces

    for i in range(8):
        spaces.append(Spot())

    command = ""
    while command != "quit":
        display_spaces()
        print("Please Select An Option:\n"
              "P - Park a Vehicle\n"
              "E - Exit the Lot\n"
              "R - Display Vehicle Rates\n")

        command = input(">")
        command_handler(command)


if __name__ == '__main__':
    main()
