import tkinter as tk

# Define the calculate_tip function
# This function will be called when the "Calculate" button is clicked
def calculate_tip():
    # Get input values from entries
    # Get the values entered by the user in the input fields
    bill_amount = float(entry_bill_amount.get())
    # Get the bill amount entered by the user
    tip_percent = float(entry_tip_percent.get())
    # Get the tip percentage entered by the user
    num_people = int(entry_num_people.get())
    # Get the number of people entered by the user

    # Calculate tip and total amounts
    # Calculate the tip amount based on the bill amount and tip percentage
    tip_amount = bill_amount * tip_percent / 100
    # Calculate the total amount by adding the tip amount to the bill amount
    total_amount = bill_amount + tip_amount

    # Calculate per-person amounts
    # Calculate the tip amount per person by dividing the tip amount by the number of people
    tip_per_person = tip_amount / num_people
    # Calculate the total amount per person by dividing the total amount by the number of people
    total_per_person = total_amount / num_people

    # Update labels with calculated values
    # Update the labels with the calculated values, formatting them to two decimal places
    label_tip_amount.config(text=f"Tip Amount: ${tip_amount:.2f}")
    label_total_amount.config(text=f"Total Amount: ${total_amount:.2f}")
    label_tip_per_person.config(text=f"Tip per Person: ${tip_per_person:.2f}")
    label_total_per_person.config(text=f"Total per Person: ${total_per_person:.2f}")

# Create the main window
root = tk.Tk()
root.title("Tip Calculator")
# Create the main window with the title "Tip Calculator"

# Create input fields and labels
input_fields = [
    {"label": "Bill Amount:", "row": 0},
    {"label": "Tip Percent:", "row": 1},
    {"label": "Number of People:", "row": 2}
]
# Define a list of input fields with their corresponding labels and row numbers

entries = []
for field in input_fields:
    label = tk.Label(root, text=field["label"])
    label.grid(row=field["row"], column=0, padx=10, pady=10)
    # Create a label for each input field
    entry = tk.Entry(root, width=10)
    entry.grid(row=field["row"], column=1, padx=10, pady=10)
    # Create an input field for each label
    entries.append(entry)
    # Add the input field to the list of entries

# Create calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate_tip)
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
# Create a button to calculate the tip and total amounts

# Create output labels
output_labels = [
    {"text": "Tip Amount:", "row": 4, "column": 0},
    {"text": "Total Amount:", "row": 4, "column": 1},
    {"text": "Tip per Person:", "row": 5, "column": 0},
    {"text": "Total per Person:", "row": 5, "column": 1}
]
# Define a list of output labels with their corresponding text and row and column numbers

labels = []
for label in output_labels:
    label_widget = tk.Label(root, text="")
    label_widget.grid(row=label["row"], column=label["column"], padx=10, pady=10)
    # Create a label for each output field
    labels.append(label_widget)
    # Add the label to the list of labels

# Assign labels to global variables
globals()["entry_bill_amount"] = entries[0]
globals()["entry_tip_percent"] = entries[1]
globals()["entry_num_people"] = entries[2]
globals()["label_tip_amount"] = labels[0]
globals()["label_total_amount"] = labels[1]
globals()["label_tip_per_person"] = labels[2]
globals()["label_total_per_person"] = labels[3]
# Assign the input fields and output labels to global variables so they can be accessed in the calculate_tip function

# Start the main loop
root.mainloop()
# Start the main event loop of the GUI