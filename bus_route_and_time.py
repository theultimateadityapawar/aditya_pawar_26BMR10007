from datetime import datetime
print("input the current time")
n = int(input("Enter the month: "))
z = int(input("Enter the day: "))
x = int(input("Enter the hour (24-hour format): "))
v = int(input("Enter the minute: "))

current = datetime.now()

target = datetime(2026, n, z, x, v)

remaining_time = target - current


routes = {
    "N1": "JAMMU",
    "N2": "DELHI",
    "N3": "CHANDIGARH",
    "N4": "SHIMLA",
    "E1": "GUWAHATI",
    "E2": "KOLKATA",
    "E3": "PATNA",
    "S1": "HYDERABAD",
    "S2": "BANGALORE",
    "S3": "CHENNAI",
    "W1": "MUMBAI",
    "W2": "AHMEDABAD",
    "W3": "SURAT",
    "W4": "JAIPUR"
}


# Display bus routes in tabular form

print("\n================ BUS ROUTES ================")
print(f"{'BUS CODE':<12} {'DESTINATION':<15}")
print("--------------------------------------------")

for code, destination in routes.items():
    print(f"{code:<12} {destination:<15}")

print("============================================")


# Ask for bus number

bus_no = input("\nEnter bus number: ")

code = bus_no[:2].upper()


# Check the bus code

if code in routes:

    print("\nBus is going to", routes[code])

    if remaining_time.total_seconds() > 0:
        print("Remaining time:", remaining_time)
    else:
        print("The bus departure time has already passed.")

else:

    print("Bus is cancelled")

