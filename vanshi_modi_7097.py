import matplotlib.pyplot as plt

events = []

# ADD EVENT
def add_event():
    id = int(input("Enter Event ID: "))
    name = input("Enter Event Name: ")
    etype = input("Enter Event Type: ")
    cost = float(input("Enter Event Cost: "))

    event = {"id": id, "name": name, "type": etype, "cost": cost}
    events.append(event)
    print("Event Added Successfully!")

# DISPLAY EVENTS
def display_events():
    if not events:
        print("No events found!")
    else:
        for e in events:
            print(e)

# UPDATE EVENT
def update_event():
    id = int(input("Enter Event ID to update: "))
    for e in events:
        if e["id"] == id:
            e["name"] = input("Enter new name: ")
            e["type"] = input("Enter new type: ")
            e["cost"] = float(input("Enter new cost: "))
            print("Event Updated!")
            return
    print("Event not found!")

# DELETE EVENT
def delete_event():
    id = int(input("Enter Event ID to delete: "))
    for e in events:
        if e["id"] == id:
            events.remove(e)
            print("Event Deleted!")
            return
    print("Event not found!")

# CHART: Cost Distribution (Only Chart)
def chart_cost():
    if not events:
        print("No data for chart!")
        return

    names = [e["name"] for e in events]
    costs = [e["cost"] for e in events]

    plt.pie(costs, labels=names, autopct='%1.1f%%')
    plt.title("Event Cost Distribution")
    plt.show()

# MENU
while True:
    print("\n--- Event Management System ---")
    print("1. Add Event")
    print("2. Display Events")
    print("3. Update Event")
    print("4. Delete Event")
    print("5. Chart: Cost Distribution")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_event()
    elif choice == 2:
        display_events()
    elif choice == 3:
        update_event()
    elif choice == 4:
        delete_event()
    elif choice == 5:
        chart_cost()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
