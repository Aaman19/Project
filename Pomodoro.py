import tkinter as tk
from tkinter import messagebox
import time

class PomodoroTimer:
    def __init__(self, master):
        # Initialize the Pomodoro timer
        self.master = master
        self.master.title('Pomodoro Timer')
        self.time_left = 1500  # 25 minutes in seconds
        self.time_left_str = self.format_time(self.time_left)
        self.is_running = False

        # Create the GUI widgets
        self.create_widgets()

    def create_widgets(self):
        # Create the time label
        self.time_left_label = tk.Label(self.master, text=self.time_left_str, font=('Helvetica', 48))
        self.time_left_label.pack(padx=20, pady=20)

        # Create the start button
        self.start_button = tk.Button(self.master, text='Start', command=self.start)
        self.start_button.pack(pady=20)

        # Create the reset button
        self.reset_button = tk.Button(self.master, text='Reset', command=self.reset)
        self.reset_button.pack(pady=20)

        # Create the stop button
        self.stop_button = tk.Button(self.master, text='Stop', command=self.stop)
        self.stop_button.pack(pady=20)

    def start(self):
        # Start the timer
        if not self.is_running:
            self.is_running = True
            self.countdown()

    def reset(self):
        # Reset the timer
        self.time_left = 1500
        self.time_left_str = self.format_time(self.time_left)
        self.time_left_label.config(text=self.time_left_str)
        self.is_running = False

    def countdown(self):
        # Countdown the timer
        if self.is_running and self.time_left > 0:
            # Wait for 1 second before calling this method again
            self.master.after(1000, self.countdown)

            # Decrease the time left by 1 second
            self.time_left -= 1

            # Format the time left as MM:SS
            self.time_left_str = self.format_time(self.time_left)

            # Update the time label
            self.time_left_label.config(text=self.time_left_str)

            # Check if the time is up
            if self.time_left == 0:
                self.is_running = False
                # Show a message box to indicate that the timer has finished
                messagebox.showinfo('Pomodoro Timer', 'Time is up! Take a break.')

    def stop(self):
        # Stop the timer
        self.is_running = False
        # Show a message box to indicate that the timer has been stopped
        messagebox.showinfo('Pomodoro Timer', 'Timer has been stopped.')


    def format_time(self, seconds):
        # Format the time as MM:SS
        return time.strftime('%M:%S', time.gmtime(seconds))

root = tk.Tk()
timer = PomodoroTimer(root)
root.mainloop()