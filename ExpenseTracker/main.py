import customtkinter as ctk
import json
import os
from datetime import datetime

ctk.set_appearance_mode("dark")

ACCENT_GREEN = "#2D5A27"
ACCENT_HOVER = "#3D7A35"
BG_SECONDARY = "#1A1C1E"


class ExpenseTracker(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("EXPENSE TRACKER")
        self.geometry("450x650")

        self.configure(fg_color="#0F0F0F")
        self.data_file = "tracker_data.json"
        self.load_data()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.header_label = ctk.CTkLabel(
            self,
            text="Financial Overview",
            font=("Segoe UI", 28, "bold"),
            text_color=ACCENT_GREEN
        )
        self.header_label.grid(row=0, column=0, padx=20, pady=(30, 10), sticky="w")

        self.input_frame = ctk.CTkFrame(self, fg_color=BG_SECONDARY, corner_radius=15)
        self.input_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.desc_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Description",
            height=45, border_width=1,
            fg_color="#252729"
        )
        self.desc_entry.pack(fill="x", padx=15, pady=(15, 5))

        self.amount_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Amount ($)",
            height=45, border_width=1,
            fg_color="#252729"
        )
        self.amount_entry.pack(fill="x", padx=15, pady=5)

        self.type_menu = ctk.CTkOptionMenu(
            self.input_frame,
            values=["Income", "Expense"],
            fg_color=ACCENT_GREEN,
            button_color=ACCENT_GREEN,
            button_hover_color=ACCENT_HOVER,
            dropdown_hover_color=ACCENT_HOVER,
            height=35
        )
        self.type_menu.pack(fill="x", padx=15, pady=(5, 15))

        self.add_button = ctk.CTkButton(
            self,
            text="+ Add Transaction",
            font=("Segoe UI", 14, "bold"),
            fg_color=ACCENT_GREEN,
            hover_color=ACCENT_HOVER,
            height=50,
            corner_radius=10,
            command=self.add_transaction
        )
        self.add_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.summary_card = ctk.CTkFrame(self, fg_color=BG_SECONDARY, corner_radius=15)
        self.summary_card.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="nsew")

        self.summary_title = ctk.CTkLabel(
            self.summary_card,
            text="Current Month",
            font=("Segoe UI", 12, "bold"),
            text_color="#888888"
        )
        self.summary_title.pack(pady=(15, 0))

        self.balance_text = ctk.CTkLabel(
            self.summary_card,
            text="$0.00",
            font=("Segoe UI", 36, "bold")
        )
        self.balance_text.pack(pady=5)

        self.stats_label = ctk.CTkLabel(
            self.summary_card,
            text="In: $0 | Out: $0",
            font=("Segoe UI", 13),
            text_color="#AAAAAA"
        )
        self.stats_label.pack(pady=(0, 15))

        self.update_summary()

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    self.transactions = json.load(f)
            except:
                self.transactions = []
        else:
            self.transactions = []

    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.transactions, f, indent=4)

    def add_transaction(self):
        desc = self.desc_entry.get()
        amount = self.amount_entry.get()
        t_type = self.type_menu.get()
        date = datetime.now().strftime("%Y-%m")

        if desc and amount:
            try:
                entry = {
                    "description": desc,
                    "amount": float(amount),
                    "type": t_type,
                    "date": date
                }
                self.transactions.append(entry)
                self.save_data()
                self.update_summary()
                self.desc_entry.delete(0, 'end')
                self.amount_entry.delete(0, 'end')
            except ValueError:
                pass

    def update_summary(self):
        current_month = datetime.now().strftime("%Y-%m")
        total_income = sum(
            t['amount'] for t in self.transactions if t['date'] == current_month and t['type'] == "Income")
        total_expense = sum(
            t['amount'] for t in self.transactions if t['date'] == current_month and t['type'] == "Expense")
        balance = total_income - total_expense

        self.balance_text.configure(
            text=f"${balance:,.2f}",
            text_color="#4ADE80" if balance >= 0 else "#F87171"  # Modern neon red/green
        )
        self.stats_label.configure(
            text=f"Income: ${total_income:,.2f}   •   Expenses: ${total_expense:,.2f}"
        )


if __name__ == "__main__":
    app = ExpenseTracker()
    app.mainloop()