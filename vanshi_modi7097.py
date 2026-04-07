
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

events = []

# ---------------- FUNCTIONS ---------------- #

def add_event():
    try:
        name = entry_name.get().strip()
        from_day = entry_from.get().strip()
        to_day = entry_to.get().strip()
        location = entry_location.get().strip()
        attendees = int(entry_attendees.get().strip())
        budget = float(entry_budget.get().strip())

        if not name or not from_day or not to_day or not location:
            raise ValueError

        events.append({
            "name": name,
            "from": from_day,
            "to": to_day,
            "location": location,
            "attendees": attendees,
            "budget": budget
        })

        messagebox.showinfo("Success", "Event Added!")
        clear_fields()
        display_events()

    except:
        messagebox.showerror("Error", "Enter valid details!")


def update_event():
    try:
        index = listbox.curselection()[0]
        events[index] = {
            "name": entry_name.get(),
            "from": entry_from.get(),
            "to": entry_to.get(),
            "location": entry_location.get(),
            "attendees": int(entry_attendees.get()),
            "budget": float(entry_budget.get())
        }
        messagebox.showinfo("Updated", "Event Updated")
        display_events()
        clear_fields()
    except:
        messagebox.showerror("Error", "Select event & enter valid data")


def delete_event():
    try:
        index = listbox.curselection()[0]
        events.pop(index)
        messagebox.showinfo("Deleted", "Event Deleted")
        display_events()
    except:
        messagebox.showerror("Error", "Select event first")


def display_events():
    listbox.delete(0, tk.END)
    for i, e in enumerate(events):
        listbox.insert(tk.END,
            f"{i+1}. {e['name']} | {e['from']} to {e['to']} | {e['location']} | {e['attendees']} | ₹{e['budget']}"
        )


def select_event(event):
    try:
        index = listbox.curselection()[0]
        e = events[index]
        clear_fields()
        entry_name.insert(0, e["name"])
        entry_from.insert(0, e["from"])
        entry_to.insert(0, e["to"])
        entry_location.insert(0, e["location"])
        entry_attendees.insert(0, e["attendees"])
        entry_budget.insert(0, e["budget"])
    except:
        pass


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_from.delete(0, tk.END)
    entry_to.delete(0, tk.END)
    entry_location.delete(0, tk.END)
    entry_attendees.delete(0, tk.END)
    entry_budget.delete(0, tk.END)


# -------- GRAPH 1: Attendees (Bar Chart) -------- #
def show_attendees_graph():
    if not events:
        messagebox.showwarning("Warning", "No data")
        return

    names = [e["name"] for e in events]
    attendees = [e["attendees"] for e in events]

    plt.figure()
    plt.bar(names, attendees)

    plt.title("Attendees per Event")
    plt.xlabel("Event Name")
    plt.ylabel("Number of Attendees")

    for i, v in enumerate(attendees):
        plt.text(i, v + 1, str(v), ha='center')

    plt.show()


# -------- GRAPH 2: Budget (Pie Chart) -------- #
def show_budget_graph():
    if not events:
        messagebox.showwarning("Warning", "No data")
        return

    names = [e["name"] for e in events]
    budgets = [e["budget"] for e in events]

    plt.figure()
    plt.pie(
        budgets,
        labels=names,
        autopct='%1.1f%%',
        startangle=90
    )

    plt.title("Budget Distribution (₹)")
    plt.axis('equal')

    plt.show()


# ---------------- UI ---------------- #

root = tk.Tk()
root.title("Event Management System")
root.geometry("760x650")

canvas = tk.Canvas(root, bg="#fff0f5")
canvas.pack(fill="both", expand=True)

canvas.create_text(380, 30, text="🌸 🌼 🌺 🌷 🌸 🌼 🌺 🌷", font=("Arial", 20))
canvas.create_text(380, 630, text="🌸 🌼 🌺 🌷 🌸 🌼 🌺 🌷", font=("Arial", 20))

canvas.create_text(380, 80, text="Event Management System",
                   font=("Arial", 18, "bold"), fill="purple")

frame = tk.Frame(canvas, bg="white", bd=3, relief="ridge")
canvas.create_window(380, 260, window=frame)


def label(text, row):
    tk.Label(frame, text=text, bg="white",
             font=("Arial", 10, "bold")).grid(row=row, column=0, padx=10, pady=8)


def entry(row):
    e = tk.Entry(frame, width=25)
    e.grid(row=row, column=1, padx=10, pady=8)
    return e


label("Event Name", 0)
entry_name = entry(0)

label("From Day", 1)
entry_from = entry(1)

label("To Day", 2)
entry_to = entry(2)

label("Location", 3)
entry_location = entry(3)

label("Attendees", 4)
entry_attendees = entry(4)

label("Budget", 5)
entry_budget = entry(5)


# Buttons
btn_frame = tk.Frame(canvas, bg="#fff0f5")
canvas.create_window(380, 400, window=btn_frame)

tk.Button(btn_frame, text="Add", width=12, bg="#4CAF50",
          fg="white", command=add_event).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Update", width=12, bg="#2196F3",
          fg="white", command=update_event).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete", width=12, bg="#f44336",
          fg="white", command=delete_event).grid(row=0, column=2, padx=5)

tk.Button(btn_frame, text="Attendees Graph", width=15,
          bg="#ff69b4", command=show_attendees_graph).grid(row=1, column=0, pady=5)

tk.Button(btn_frame, text="Budget Graph", width=15,
          bg="#ffa500", command=show_budget_graph).grid(row=1, column=1, pady=5)


# Listbox
listbox = tk.Listbox(canvas, width=95, height=10)
canvas.create_window(380, 550, window=listbox)
listbox.bind("<<ListboxSelect>>", select_event)

root.mainloop()
