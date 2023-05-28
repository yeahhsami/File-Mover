import tkinter as tk
from tkinter import filedialog
import file_organizer

def select_source_directory():
    source_dir = filedialog.askdirectory()
    source_entry.insert(tk.END, source_dir)

def move_files():
    source_dir = source_entry.get()
    destination_dir = destination_entry.get()
    file_organizer.move_files(source_dir, destination_dir)

# Create the main window
window = tk.Tk()
window.title("File Mover")

# Create labels and entry fields
source_label = tk.Label(window, text="Source Directory:")
source_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

source_entry = tk.Entry(window, width=50)
source_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

source_button = tk.Button(window, text="Browse", command=select_source_directory)
source_button.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

destination_label = tk.Label(window, text="Destination Directory:")
destination_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

destination_entry = tk.Entry(window, width=50)
destination_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

# Create a button to initiate the file moving process
move_button = tk.Button(window, text="Move Files", command=move_files)
move_button.grid(row=2, column=0, columnspan=3, padx=5, pady=10)

# Start the GUI main loop
window.mainloop()
