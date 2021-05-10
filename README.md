# Parking Lot System Project
This project was made to practice working with Object-Oriented Programming within Python.

The program allows a user to enter their vehicle's type and license plate number at which
their vehicle is shown within the system. The system's UI shows an ASCII version of the parking grid,
which allows the user to see the number of available spaces as well as what types of vehicles are currently
parked within the lot. The system also tracks a user's time within the lot, and will calculate a fare when their vehicle
is removed.


## Features
### Adding A Vehicle (Parking a Vehicle)
Parking a vehicle requires the user to specify their vehicle's type (Car, Truck, or Motorcycle) then prompts for the vehicle's plate number. 
This program will accept any valid string as a plate number. The program will check for duplicate plate numbers and prevent
multiple plate numbers from being added.

Once a vehicle is successfully added, the time of entry is presented for two seconds, then the system will return to the main menu.

If a vehicle is not successfully added, an error will be given and the system
will return to the main menu

### Removing a Vehicle (Leaving the Lot)
When leaving the lot, the user will specify the row and space of the vehicle they want to remove. If a valid space is selected, 
the vehicle will be removed from the space and the program will calculate a user's fare based on how many hours were spent in the lot.

Calculating the fare is done based on how long a vehicle was in the lot as well as by what type of vehicle was parked.
A minimum base price of one hour for each rate is required for each vehicle, otherwise, the fare will include the current hour and the previous hours.

### Viewing a Vehicle
At any point, the user can view the information of any vehicle currently stored within the lot.
Selecting a valid row and space will return the vehicle's type, plate number, and date/time of entry. 

### Static Interface (Linux Only)
Using the "os" module, the program makes use of the os.system() function which allows execution of linux commands from the source code.

In this instance it is used with the "clear" command to clear the screen prior to printing the interface. This gives the effect of a static interface
which ensures the presented information is readable at all times. 

### Row/Space Selection
One unique feature is the row and space selection which adds more choice for a user.

When Adding, Viewing, or Removing a Vehicle,  a user can specify which row and space within the lot they would like to access.

Valid options in the selection system are denoted by <> brackets

Here is an example of user input/output to view a vehicle:

1. Menu:
```
SPOTS AVAILABLE: 15
|-------------------|
|[ ] [ ] [ ] [c] [ ]|
|[ ] [ ] [m] [ ] [ ]|
|[t] [ ] [ ] [ ] [t]|
|[ ] [c] [ ] [ ] [ ]|
|-------------------|

Please Select An Option:
P - Park a Vehicle
E - Exit the Lot
V - View a Parked Vehicle
R - Display Vehicle Rates
Q - Quit Application

>V
```
2. Row Selection:
```
SPOTS AVAILABLE: 15
|-------------------|
|[ ] [ ] [ ] [c] [ ]| <0>
|[ ] [ ] [m] [ ] [ ]| <1>
|[t] [ ] [ ] [ ] [t]| <2>
|[ ] [c] [ ] [ ] [ ]| <3>
|-------------------|

Select Row to View:
>1

```
3. Space Selection:
```
VIEWING ROW: 1
|-------------------|
|[ ] [ ] [m] [ ] [ ]|
 <0> <1> <2> <3> <4> 
|-------------------|

Select Space to View:
>2

```
4. Vehicle Information Given:
```
VIEWING ROW: 1
|-------------------|
|[ ] [ ] [m] [ ] [ ]|
 <0> <1> <2> <3> <4> 
|-------------------|

Vehicle Type: Motorcycle
Plate Number: ccc-dddd
Entry Time: 05-09-2021 09:30 AM

Press Enter to return to menu

```

## Execution
This program uses Python 3.8. Please ensure you have the correct Python version before executing.

### Windows
After downloading and extracting the files to a directory, simply run "parking_lot.py" from the explorer or from the command line.

Ensure that the "linux" flag within config.txt is set to 0 for proper execution

### Linux
After downloading and extracting the files to a directory, the program can be executed from the command line using:

`python3 parking_lot.py`

To enable the static interface feature, set the "linux" flag within config.txt to 1. The same command to execute can be used. 

### Config
The config.txt file allows the changing of the total number of spaces within the lot as well as the number of rows.

The total_spaces value can support up to 3 digits, the rows value can supprt up to 2 digits.

The linux and demo_mode flags can be either 0 or 1, their usages are specifed above.


## Postmortem
This project was used to practice Python as well as my project design and management skills.
Completing the project, I want share my thoughts on how it went for me. 

One aspect of my project workflow that I want to improve is my number of commits. While it is not good practice to commit after every single change,
I feel that commits should occur with the completion of a major feature change. Many of my commits contain several changes in the message, and I want to learn to turn each of those major points into an 
individual commit.

One thing I felt strong on was defining what my programming goals were for each session. As I figured out which features to implement, I made specific notes to what I wanted to accomplish within a period of time.

Finally, I really enjoyed working with an open-ended idea such as a "parking lot system". Deciding which features I felt 
were useful to users was interesting and allowed me to consider several cases. In the end, I went for 
an accessible approach which gives a user more choice and accessibility to information.
