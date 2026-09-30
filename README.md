# aditya_pawar_26BMR10007
# Bus Route and Departure Time Checker

## 1. Project Overview

The **Bus Route and Departure Time Checker** is a simple Python-based console application that allows users to check the destination of a bus using its bus code and calculate the remaining time until a specified departure time.

The program displays a list of available bus codes and their corresponding destinations in a tabular format. The user then enters the desired date and time and provides a bus number. The program identifies the bus route and displays the destination along with the remaining time until the specified departure time.

If the entered bus code is not present in the available routes, the program displays **"Bus is cancelled"**.

---

## 2. Features

* Accepts the month, day, hour, and minute from the user.
* Uses the system's current date and time.
* Calculates the remaining time until the specified departure time.
* Displays all available bus codes and destinations in a table.
* Allows the user to enter a bus number.
* Automatically extracts the first two characters of the bus number as the bus code.
* Accepts lowercase bus codes by converting the input to uppercase.
* Identifies the destination associated with a valid bus code.
* Displays a message if the specified departure time has already passed.
* Displays **"Bus is cancelled"** when an invalid bus code is entered.

---

## 3. Bus Routes

The program currently contains the following bus routes:

| Bus Code | Destination |
| -------- | ----------- |
| N1       | JAMMU       |
| N2       | DELHI       |
| N3       | CHANDIGARH  |
| N4       | SHIMLA      |
| E1       | GUWAHATI    |
| E2       | KOLKATA     |
| E3       | PATNA       |
| S1       | HYDERABAD   |
| S2       | BANGALORE   |
| S3       | CHENNAI     |
| W1       | MUMBAI      |
| W2       | AHMEDABAD   |
| W3       | SURAT       |
| W4       | JAIPUR      |

---

## 4. Technologies and Tools Used

### Programming Language

* **Python 3**

### Python Module

* **datetime** — used to obtain the current date and time and calculate the difference between the current time and the specified departure time.

### Data Structure

* **Dictionary** — used to store bus codes and their corresponding destinations.

### Other Python Concepts Used

* User input using `input()`
* Type conversion using `int()`
* Conditional statements (`if`, `else`)
* `for` loops
* Dictionary methods such as `.items()`
* String slicing
* String formatting
* Date and time arithmetic

---

## 5. Installation and Setup

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

You can check whether Python is installed by opening a terminal or command prompt and running:

```bash
python3 --version
```

or:

```bash
python --version
```

If Python is installed, the terminal will display its version.

### Step 2: Save the Program

Save the Python code in a file, for example:

```text
bus_route.py
```

### Step 3: Open the Terminal

Navigate to the folder where the Python file is saved.

For example:

```bash
cd path/to/your/project
```

### Step 4: Run the Program

On Linux or macOS:

```bash
python3 bus_route.py
```

On Windows:

```bash
python bus_route.py
```

No external Python packages are required because the program uses the built-in `datetime` module.

---

## 6. How to Use the Program

When the program starts, it asks the user to enter the date and time:

```text
input the current time
Enter the month:
Enter the day:
Enter the hour (24-hour format):
Enter the minute:
```

The program then displays the available bus routes:

```text
================ BUS ROUTES ================
BUS CODE     DESTINATION
--------------------------------------------
N1           JAMMU
N2           DELHI
N3           CHANDIGARH
N4           SHIMLA
E1           GUWAHATI
E2           KOLKATA
E3           PATNA
S1           HYDERABAD
S2           BANGALORE
S3           CHENNAI
W1           MUMBAI
W2           AHMEDABAD
W3           SURAT
W4           JAIPUR
============================================
```

The user is then asked to enter a bus number.

For example:

```text
Enter bus number: N2
```

The program will display:

```text
Bus is going to DELHI
Remaining time: ...
```

---

## 7. Testing Instructions

The program can be tested using different types of inputs.

### Test Case 1: Valid Bus Code

**Input:**

```text
N2
```

**Expected Output:**

```text
Bus is going to DELHI
Remaining time: ...
```

---

### Test Case 2: Another Valid Bus Code

**Input:**

```text
S3
```

**Expected Output:**

```text
Bus is going to CHENNAI
Remaining time: ...
```

---

### Test Case 3: Lowercase Bus Code

**Input:**

```text
n2
```

The program converts the bus code to uppercase using:

```python
code = bus_no[:2].upper()
```

**Expected Output:**

```text
Bus is going to DELHI
```

---

### Test Case 4: Invalid Bus Code

**Input:**

```text
X1
```

Since `X1` is not present in the route dictionary, the expected output is:

```text
Bus is cancelled
```

---

### Test Case 5: Departure Time Already Passed

Enter a date and time that is earlier than the current system time.

**Expected Output:**

```text
Bus is going to DELHI
The bus departure time has already passed.
```

---

## 8. Important Notes

* The program currently uses the year **2026** when creating the target date.
* The computer's system clock is used to obtain the current date and time.
* The bus code is taken from the **first two characters** of the entered bus number.
* For example, entering `N1234` results in the bus code `N1`.
* The program does not require an internet connection.
* No external Python libraries need to be installed.

---

## 9. Project Structure

A simple project structure can be:

```text
Bus-Route-Project/
│
├── bus_route.py
│
└── README.md
```

Where:

* `bus_route.py` contains the Python program.
* `README.md` contains the project documentation.

---

## 10. Future Improvements

Possible improvements to the project include:

* Allowing the user to select the year instead of using a fixed year.
* Storing different departure times for different buses.
* Adding multiple buses for each route.
* Adding a graphical user interface (GUI).
* Adding a feature to search for buses by destination.
* Adding estimated arrival times.
* Saving bus route information in a file or database.
* Adding input validation for incorrect dates and times.
* Displaying the current time automatically instead of asking the user to enter it.
