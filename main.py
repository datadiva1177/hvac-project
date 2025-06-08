import tkinter as tk
from tkinter import messagebox
import datetime
from InventoryManager import InventoryManager
from purchases_module import PurchasesWindow
from reports_module import ReportsWindow
from saleswindow import SalesWindow
from access_module import AccessWindow
from printview_module import PrintViewWindow

CURRENT_USER = "Admin"

def get_current_datetime():
    return datetime.datetime.now().strftime("%B %d, %Y - %I:%M:%S %p")

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("RENFI HVAC Inventory Management System")
        self.geometry("1200x600")
        self.configure(bg="white")

        self.create_widgets()
        self.update_clock()

    def create_widgets(self):
        # HEADER
        tk.Label(self, text="RENFI HVAC Inventory Management System", font=("Arial", 24, "bold"), bg="white").pack(pady=10)

        # User + Date & Time Frame
        self.info_label = tk.Label(self, text="", font=("Arial", 12), bg="white")
        self.info_label.pack(pady=5)

        # Button Grid Frame
        button_frame = tk.Frame(self, bg="white")
        button_frame.pack(pady=15)

        # Use nested frames per row to keep using .pack()
        row1 = tk.Frame(button_frame, bg="white")
        row1.pack()
        row2 = tk.Frame(button_frame, bg="white")
        row2.pack()
        row3 = tk.Frame(button_frame, bg="white")
        row3.pack()

        self.create_big_button(row1, "INVENTORY", "#2563EB", self.open_inventory)
        self.create_big_button(row1, "SALES", "#10B981", self.open_sales)
        self.create_big_button(row2, "PURCHASES", "#F59E0B", self.open_purchases)
        self.create_big_button(row2, "REPORT", "#6366F1", self.open_reports)
        self.create_big_button(row3, "ACCESS", "#8B5CF6", self.access_window)
        self.create_big_button(row3, "PRINTVIEW", "#EC4899", self.printview_window)
        # Bottom Buttons
        bottom_frame = tk.Frame(self, bg="white")
        bottom_frame.pack(pady=20)

        tk.Button(bottom_frame, text="Refresh", command=self.refresh, font=("Arial", 12), bg="#6B7280", fg="white", width=10).pack(side=tk.LEFT, padx=10)
        tk.Button(bottom_frame, text="Exit", command=self.exit_app, font=("Arial", 12), bg="#111827", fg="white", width=10).pack(side=tk.LEFT, padx=10)

    def create_big_button(self, parent, text, color, command):
        tk.Button(
            parent,
            text=text,
            font=("Arial", 14, "bold"),
            width=20,
            height=4,
            bg=color,
            fg="white",
            command=command
        ).pack(side=tk.LEFT, padx=20, pady=15)

    def update_clock(self):
        current_time = get_current_datetime()
        self.info_label.config(text=f"User: {CURRENT_USER} | {current_time}")
        self.after(1000, self.update_clock)

    def refresh(self):
        messagebox.showinfo("Refreshed", "Dashboard has been refreshed.")

    def exit_app(self):
        self.destroy()

    def open_inventory(self):
        InventoryManager(self)

    def open_sales(self):
        window = SalesWindow(self)
        window.grab_set()
        window.focus()

    def open_purchases(self):
        PurchasesWindow(self)  # pass self only if PurchasesWindow expects a parent

    def open_reports(self):
        ReportsWindow(self)

    def access_window(self):
        window = AccessWindow(self)
        window.grab_set()
        window.focus()

    def printview_window(self):
        window = PrintViewWindow(self)
        window.grab_set()
        window.focus()


if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
