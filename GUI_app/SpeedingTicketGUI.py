# Name: Sunmi Kim
# Date: 06/09/2023
# Title: Speeding Fine Calculator GUI Application

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from speedingfine import SpeedingFineCalculator 

class SpeedingFineFrame(ttk.Frame): # Presentation Tier
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.speedingFineCalculator = SpeedingFineCalculator()

        #Save the parent so we can call destroy on the parent window
        self.parent = parent
        
        # Define variables for text entry fields
        self.speedLimit= tk.DoubleVar()
        self.clockedSpeed= tk.DoubleVar()
        self.speedingFine= tk.DoubleVar()
       
        self.initComponents()
        
    def initComponents(self):
        self.pack()
        self.initMainFrame()
        self.initButtonsFrame()
         
    def initMainFrame(self): 
        # Create frame
        frame = ttk.Frame(self, padding='10 10 10 10')
        frame.grid()

        label1 = ttk.Label(frame, text="Minimum Fine: $50")
        label1.grid(column=0, row=0, sticky=tk.W)

        label2 = ttk.Label(frame, text="Penalty per MPH over limit: $5")
        label2.grid(column=0, row=1, sticky=tk.W)

        label3 = ttk.Label(frame, text="Penalty for 50 MPH over limit: $200")
        label3.grid(column=0, row=2, sticky=tk.W)

        label4 = ttk.Label(frame, text="Speed limit: ")
        label4.grid(column=0, row=3, sticky=tk.W)

        limit = ttk.Entry(frame, width=20, textvariable=self.speedLimit)
        limit.delete(0, tk.END)
        limit.grid(column=1, row=3)

        label5 = ttk.Label(frame, text="Clocked speed: ")
        label5.grid(column=0, row=4, sticky=tk.W)

        speed = ttk.Entry(frame, width=20, textvariable=self.clockedSpeed)
        speed.delete(0, tk.END)
        speed.grid(column=1, row=4)

        label6 = ttk.Label(frame, text="Speeding Fine: ")
        label6.grid(column=0, row=5, sticky=tk.W)

        # Make the entry box for speeding fine read-only
        fine = ttk.Entry(frame, width=20, textvariable=self.speedingFine, state='readonly')
        fine.delete(0, tk.END)
        fine.grid(column=1, row=5)
        
    def initButtonsFrame(self):
        # Create Frame object using grid method to add to the parent frame (self).
        # adding the corresponding event-handlers to the buttons.   
        button_frame = ttk.Frame(self)
        button_frame.grid()

        calculateButton = ttk.Button(button_frame, text="Calculate", command=self.calculateFine)
        calculateButton.grid(column=0, row=0)

        clearButton = ttk.Button(button_frame, text="Clear", command=self.clear)
        clearButton.grid(column=1, row=0)

        exitButton = ttk.Button(button_frame, text="Exit", command=self.exit)
        exitButton.grid(column=2, row=0)

    def calculateFine(self):
        try:
            limit = self.speedLimit.get()
            speed = self.clockedSpeed.get()

            # Update the speedingLimit property to pass limit
            self.speedingFineCalculator.speedingLimit = limit
            fine = self.speedingFineCalculator.calculateSpeedingFine(speed)
            self.speedingFine.set(fine)
        except ValueError as e:
            messagebox.showerror("Please enter valid positive numbers", str(e))

    def clear(self):
        # clear all the text entry boxes to 0
        self.speedLimit.set(0)
        self.clockedSpeed.set(0)
        self.speedingFine.set(0)
    
    def exit(self):
        self.parent.destroy()
        
def main():
    root = tk.Tk()
    root.title("Speeding Fine Calculator of Funnyville")
    SpeedingFineFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
