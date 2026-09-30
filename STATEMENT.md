# Bus Route and Departure Time Checker

## 1. Problem Statement

Finding the destination and departure information of a bus can be difficult when bus routes are represented using short codes. Users may need to remember which bus code corresponds to which destination and determine how much time is left before the specified departure time.

The **Bus Route and Departure Time Checker** is designed to provide a simple console-based solution to this problem. The program displays the available bus codes and their destinations in a tabular format. It allows the user to enter a bus number and identifies its destination using the bus code.

The program also calculates the remaining time between the current system time and the user-specified departure time. If the entered bus code is not available, the program informs the user that the bus is cancelled.

---

## 2. Scope of the Project

The scope of this project is to provide a basic and easy-to-use bus route and departure time checking system using Python.

The project currently covers:

* Displaying a list of available bus codes and destinations.
* Accepting a bus number from the user.
* Identifying the destination using the first two characters of the bus number.
* Calculating the remaining time until a specified departure time.
* Informing the user when the specified departure time has already passed.
* Handling invalid or unavailable bus codes.

The current project is designed as a **console-based application** and does not connect to real-time bus tracking systems, GPS services, online transportation databases, or external APIs.

Future versions could expand the scope by adding real-time bus locations, multiple departure schedules, route searching, databases, and a graphical user interface.

---

## 3. Target Users

The project is intended for users who need a simple way to identify bus routes and check departure time information.

### Primary Target Users

* **Bus passengers** — to quickly identify the destination of a bus using its bus code.
* **Students** — as a simple example of applying Python programming concepts to a practical problem.
* **Beginners learning Python** — to understand dictionaries, loops, conditional statements, user input, and date/time operations.

### Secondary Target Users

* **Small transport operators** — as a basic prototype for organizing bus route information.
* **Developers and students** — as a starting point for developing a more advanced transportation management system.

---

## 4. High-Level Features

The main features of the project are:

### 4.1 Bus Route Table

The program displays all available bus codes and their corresponding destinations in a table.

Example:

```text
BUS CODE     DESTINATION
--------------------------------------------
N1           JAMMU
N2           DELHI
N3           CHANDIGARH
N4           SHIMLA
...
```

### 4.2 Bus Code Identification

The program extracts the first two characters of the entered bus number and uses them as the bus code.

For example:

```text
Input: N234
Bus Code: N2
```

### 4.3 Destination Lookup

The program uses a Python dictionary to match the bus code with its destination.

For example:

```text
N2 → DELHI
S3 → CHENNAI
W1 → MUMBAI
```

### 4.4 Remaining Time Calculation

The program uses Python's `datetime` module to calculate the difference between the current system time and the specified departure time.

### 4.5 Departure Time Check

The program checks whether the specified departure time has already passed.

If it has passed, the program displays:

```text
The bus departure time has already passed.
```

### 4.6 Invalid Bus Code Handling

If the entered bus code is not present in the available routes, the program displays:

```text
Bus is cancelled
```

### 4.7 Case-Insensitive Bus Code Input

The program converts the entered bus code to uppercase, allowing inputs such as:

```text
N2
n2
```

to be treated as the same bus code.

---

## 5. Project Objective

The main objective of the project is to create a simple Python application that combines **bus route lookup** with **departure time calculation**.

The project also demonstrates the practical use of fundamental Python concepts such as:

* Dictionaries
* Loops
* Conditional statements
* User input
* String slicing
* String formatting
* Date and time operations
