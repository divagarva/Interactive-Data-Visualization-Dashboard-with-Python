import tkinter as tk
from tkinter import messagebox
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create main application window
root = tk.Tk()
root.title("Data Visualization Dashboard")
root.geometry("800x600")

# Global DataFrame to store the loaded data and a variable to hold the canvas
data = pd.DataFrame()
current_canvas = None

def load_sample_data():
    """Load sample data from seaborn."""
    global data
    data = sns.load_dataset('tips')  # Load sample dataset
    label_data_status.config(text="Sample Data Loaded: 'tips' Dataset")

def clear_plot():
    """Clear the current plot from the window."""
    global current_canvas
    if current_canvas is not None:
        current_canvas.get_tk_widget().pack_forget()
        current_canvas = None

def plot_line():
    """Plot a line graph of the data."""
    if data.empty:
        label_data_status.config(text="No data loaded")
        return
    clear_plot()
    fig, ax = plt.subplots()
    data.plot(ax=ax)
    global current_canvas
    current_canvas = FigureCanvasTkAgg(fig, master=root)
    current_canvas.draw()
    current_canvas.get_tk_widget().pack()

def plot_bar():
    """Plot a bar chart of the data."""
    if data.empty:
        label_data_status.config(text="No data loaded")
        return
    clear_plot()
    fig, ax = plt.subplots()
    data.plot(kind='bar', ax=ax)
    global current_canvas
    current_canvas = FigureCanvasTkAgg(fig, master=root)
    current_canvas.draw()
    current_canvas.get_tk_widget().pack()

def plot_scatter():
    """Plot a scatter plot of the data."""
    if data.empty:
        label_data_status.config(text="No data loaded")
        return
    clear_plot()
    fig, ax = plt.subplots()
    if len(data.columns) >= 2:  # Ensure there are at least two columns for scatter
        data.plot(kind='scatter', x=data.columns[0], y=data.columns[1], ax=ax)
    else:
        messagebox.showinfo("Plot Error", "Data must have at least two columns for scatter plot.")
    global current_canvas
    current_canvas = FigureCanvasTkAgg(fig, master=root)
    current_canvas.draw()
    current_canvas.get_tk_widget().pack()

def exit_program():
    """Exit the program."""
    root.quit()  # Stop the Tkinter event loop
    root.destroy()  # Close the window

# GUI Components
button_load_data = tk.Button(root, text="Load Sample Data", command=load_sample_data)
button_load_data.pack(pady=10)

label_data_status = tk.Label(root, text="No data loaded")
label_data_status.pack(pady=10)

button_line_plot = tk.Button(root, text="Line Plot", command=plot_line)
button_line_plot.pack(pady=5)

button_bar_plot = tk.Button(root, text="Bar Chart", command=plot_bar)
button_bar_plot.pack(pady=5)

button_scatter_plot = tk.Button(root, text="Scatter Plot", command=plot_scatter)
button_scatter_plot.pack(pady=5)

# Exit button to close the program with visible text
button_exit = tk.Button(root, text="Exit", command=exit_program, bg='lightgray', fg='black')
button_exit.pack(pady=20)

# Run the main loop
root.mainloop()
