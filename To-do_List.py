import tkinter as tk
from tkinter import filedialog

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a list to store the to-do items
# This list will hold all the to-do items added by the user
todo_items = []

# Create a function to add a to-do item
def add_item():
    # Get the text from the input field
    # This gets the text entered by the user in the input field
    item = entry_item.get()
    if item!= "":
        # Add the item to the list and the listbox
        # Add the item to the todo_items list and also add it to the listbox
        todo_items.append(item)
        listbox_todo.insert(tk.END, item)
        # Clear the input field
        # Clear the input field so that the user can enter a new item
        entry_item.delete(0, tk.END)

# Create a function to delete a to-do item
def delete_item(index):
    # Remove the item from the list and the listbox
    # Remove the item at the specified index from the todo_items list and the listbox
    todo_items.pop(index)
    listbox_todo.delete(index)

# Create a function to save the to-do list as a text file
def save_list():
    # Open a file dialog to save the file
    # Open a file dialog to allow the user to choose a location and filename to save the to-do list
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file is None:
        return
    # Write each item to the file
    # Write each item in the todo_items list to the file, one item per line
    for item in todo_items:
        file.write(item + "\n")
    file.close()

# Create input fields and labels
label_item = tk.Label(root, text="Add a to-do item:")
label_item.grid(row=0, column=0, padx=10, pady=10)
# Create a label to prompt the user to enter a to-do item

entry_item = tk.Entry(root, width=30)
entry_item.grid(row=0, column=1, padx=10, pady=10)
# Create an input field for the user to enter a to-do item

button_add = tk.Button(root, text="Add", command=add_item)
button_add.grid(row=0, column=2, padx=10, pady=10)
# Create a button to add the to-do item to the list

# Create the to-do list
listbox_todo = tk.Listbox(root, width=50, height=10)
listbox_todo.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
# Create a listbox to display the to-do items

# Create a scrollbar for the to-do list
scrollbar_todo = tk.Scrollbar(root, orient=tk.VERTICAL, command=listbox_todo.yview)
scrollbar_todo.grid(row=1, column=3, padx=10, pady=10, sticky=tk.NS)
listbox_todo.configure(yscrollcommand=scrollbar_todo.set)
# Create a scrollbar to allow the user to scroll through the to-do list if it is too long

# Create a function to delete the selected to-do item(s)
def delete_selected():
    # Get the selected indices
    # Get the indices of the selected items in the listbox
    selection = listbox_todo.curselection()
    # Delete each selected item
    # Delete each selected item from the todo_items list and the listbox
    for index in reversed(selection):
        delete_item(index)

# Create a button to delete the selected to-do item(s)
button_delete = tk.Button(root, text="Delete Selected", command=delete_selected)
button_delete.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
# Create a button to delete the selected to-do items

# Create a button to clear the entire to-do list
button_clear = tk.Button(root, text="Clear All", command=lambda: listbox_todo.delete(0, tk.END))
button_clear.grid(row=2, column=2, padx=10, pady=10)
# Create a button to clear the entire to-do list

# Create a button to save the to-do list as a text file
button_save = tk.Button(root, text="Save List", command=save_list)
button_save.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
# Create a button to save the to-do list as a text file

# Start the main loop
root.mainloop()
# Start the main event loop of the GUI