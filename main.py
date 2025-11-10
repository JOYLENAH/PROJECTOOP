"""
E-VOTING SYSTEM PROJECT
By: Babirye Joy Lenah
Demonstrating OOP Concepts:
- Abstraction
- Inheritance
- Polymorphism
- Encapsulation
With a Tkinter Graphical User Interface (GUI)
"""

# --------------------- IMPORTS ---------------------
import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod


# ============================================================
#               1️⃣ ABSTRACTION (Abstract Base Class)
# ============================================================

class Person(ABC):
    def __init__(self, name):
        # Encapsulation: Private attribute
        self._name = name

    @abstractmethod
    def show_info(self):
        pass


# ============================================================
#               2️⃣ INHERITANCE & POLYMORPHISM
# ============================================================

class Admin(Person):
    def __init__(self, name):
        super().__init__(name)
        self.candidates = []
        self.votes = {}

    def add_candidate(self, candidate_name):
        """Admin adds a candidate to the election"""
        if candidate_name not in self.candidates:
            self.candidates.append(candidate_name)
            self.votes[candidate_name] = 0
            return f"Candidate '{candidate_name}' added."
        else:
            return f"Candidate '{candidate_name}' already exists."

    def view_results(self):
        """Display current election results"""
        if not self.votes:
            return "No votes yet!"
        results = "Election Results:\n"
        for candidate, count in self.votes.items():
            results += f"{candidate}: {count} votes\n"
        return results

    # Polymorphism: same method name as in Voter but different behavior
    def show_info(self):
        return f"Admin: {self._name}"


class Voter(Person):
    def __init__(self, name):
        super().__init__(name)
        self.has_voted = False

    # Polymorphism: different implementation of show_info()
    def show_info(self):
        return f"Voter: {self._name}"


# ============================================================
#               3️⃣ MAIN GUI APPLICATION CLASS
# ============================================================

class EVotingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("E-Voting System")
        self.root.geometry("460x520")
        self.root.config(bg="#eaf4f4")

        # Create default admin
        self.admin = Admin("Joy (Admin)")
        self.voter = None

        self.home_screen()

    # --------------------- UTILITY ---------------------
    def clear(self):
        """Clear all widgets from the screen"""
        for widget in self.root.winfo_children():
            widget.destroy()

    # ============================================================
    #                   HOME SCREEN
    # ============================================================
    def home_screen(self):
        self.clear()
        tk.Label(self.root, text="E-Voting System", font=("Arial", 18, "bold"), bg="#eaf4f4").pack(pady=40)
        tk.Button(self.root, text="Admin", width=20, bg="#0077b6", fg="white", command=self.admin_login).pack(pady=10)
        tk.Button(self.root, text="Voter", width=20, bg="#0077b6", fg="white", command=self.voter_login).pack(pady=10)

    # ============================================================
    #                   ADMIN SECTION
    # ============================================================
    def admin_login(self):
        self.clear()
        tk.Label(self.root, text="Admin Panel", font=("Arial", 16, "bold"), bg="#eaf4f4").pack(pady=30)
        tk.Button(self.root, text="Add Candidate", width=20, bg="#0096c7", fg="white", command=self.add_candidate_screen).pack(pady=10)
        tk.Button(self.root, text="View Results", width=20, bg="#0096c7", fg="white", command=self.view_results).pack(pady=10)
        tk.Button(self.root, text="Back", width=20, bg="gray", fg="white", command=self.home_screen).pack(pady=20)

    def add_candidate_screen(self):
        self.clear()
        tk.Label(self.root, text="Enter Candidate Name:", bg="#eaf4f4", font=("Arial", 12)).pack(pady=10)
        name_entry = tk.Entry(self.root, width=25)
        name_entry.pack(pady=5)
        tk.Button(self.root, text="Add", bg="#0077b6", fg="white",
                  command=lambda: messagebox.showinfo("Info", self.admin.add_candidate(name_entry.get()))).pack(pady=10)
        tk.Button(self.root, text="Back", bg="gray", fg="white", command=self.admin_login).pack(pady=10)

    def view_results(self):
        messagebox.showinfo("Results", self.admin.view_results())

    # ============================================================
    #                   VOTER SECTION
    # ============================================================
    def voter_login(self):
        self.clear()
        tk.Label(self.root, text="Enter Your Name:", bg="#eaf4f4", font=("Arial", 12)).pack(pady=10)
        name_entry = tk.Entry(self.root, width=25)
        name_entry.pack(pady=5)
        tk.Button(self.root, text="Login", bg="#0077b6", fg="white",
                  command=lambda: self.voter_menu(name_entry.get())).pack(pady=10)
        tk.Button(self.root, text="Back", bg="gray", fg="white", command=self.home_screen).pack(pady=10)

    def voter_menu(self, name):
        self.voter = Voter(name)
        self.clear()
        tk.Label(self.root, text=f"Welcome, {name}", font=("Arial", 16, "bold"), bg="#eaf4f4").pack(pady=30)
        tk.Button(self.root, text="Cast Vote", width=20, bg="#0096c7", fg="white", command=self.cast_vote_screen).pack(pady=10)
        tk.Button(self.root, text="Back", width=20, bg="gray", fg="white", command=self.home_screen).pack(pady=20)

    # ============================================================
    #                   CAST VOTE SECTION
    # ============================================================
    def cast_vote_screen(self):
        self.clear()
        tk.Label(self.root, text="Cast Your Vote", font=("Arial", 16, "bold"), bg="#eaf4f4").pack(pady=15)

        if not self.admin.candidates:
            tk.Label(self.root, text="No candidates available yet!", bg="#eaf4f4").pack(pady=10)
        else:
            # Buttons for candidates
            tk.Label(self.root, text="Select or type a candidate's name below:", bg="#eaf4f4", font=("Arial", 12)).pack(pady=5)
            for c in self.admin.candidates:
                tk.Button(self.root, text=c, width=20,
                          command=lambda x=c: self.record_vote(x)).pack(pady=3)

            # Text box for manual input
            tk.Label(self.root, text="Or type candidate name:", bg="#eaf4f4", font=("Arial", 11)).pack(pady=5)
            candidate_entry = tk.Entry(self.root, width=25)
            candidate_entry.pack(pady=3)

            tk.Button(self.root, text="Submit Vote", width=15, bg="#0077b6", fg="white",
                      command=lambda: self.submit_typed_vote(candidate_entry.get())).pack(pady=10)

        tk.Button(self.root, text="Back", bg="gray", fg="white",
                  command=lambda: self.voter_menu(self.voter._name)).pack(pady=10)

    # ============================================================
    #                   HELPER METHODS
    # ============================================================
    def submit_typed_vote(self, name):
        """Check typed name validity before recording"""
        if not name:
            messagebox.showwarning("Warning", "Please type a candidate name!")
            return
        if name not in self.admin.candidates:
            messagebox.showerror("Error", f"Candidate '{name}' not found!")
        else:
            self.record_vote(name)

    def record_vote(self, candidate):
        """Record the vote"""
        if self.voter.has_voted:
            messagebox.showwarning("Warning", "You have already voted!")
        else:
            self.admin.votes[candidate] += 1
            self.voter.has_voted = True
            messagebox.showinfo("Success", f"You voted for {candidate}")
            self.voter_menu(self.voter._name)


# ============================================================
#                   RUN THE APPLICATION
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = EVotingApp(root)
    root.mainloop()
