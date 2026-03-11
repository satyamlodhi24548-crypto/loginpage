import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import re

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Information Form")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.root.configure(bg='#e6f7ff')  # Light blue background
        
        # Style for colorful theme
        style = ttk.Style()
        style.configure('TFrame', background='#e6f7ff')
        style.configure('TLabel', background="#fff9e6", foreground='#333333')
        style.configure('TButton', background='#4CAF50', foreground='white', font=('Helvetica', 10, 'bold'))
        style.map('TButton', background=[('active', '#45a049')])
        
        # Main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title with animation
        self.title_label = ttk.Label(main_frame, text="Personal Information Form", 
                         font=("Helvetica", 18, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Start title animation
        self.animate_title()
        
        # Name
        ttk.Label(main_frame, text="Name:").grid(row=1, column=0, sticky="w", pady=5)
        self.name_entry = ttk.Entry(main_frame, width=35)
        self.name_entry.grid(row=1, column=1, pady=5)
        
        # Email
        ttk.Label(main_frame, text="Email:").grid(row=2, column=0, sticky="w", pady=5)
        self.email_entry = ttk.Entry(main_frame, width=35)
        self.email_entry.grid(row=2, column=1, pady=5)
        
        # Phone
        ttk.Label(main_frame, text="Phone:").grid(row=3, column=0, sticky="w", pady=5)
        self.phone_entry = ttk.Entry(main_frame, width=35)
        self.phone_entry.grid(row=3, column=1, pady=5)
        
        # Aadhar Card
        ttk.Label(main_frame, text="Aadhar Card:").grid(row=4, column=0, sticky="w", pady=5)
        self.aadhar_entry = ttk.Entry(main_frame, width=35)
        self.aadhar_entry.grid(row=4, column=1, pady=5)
        
        # Date of Birth
        ttk.Label(main_frame, text="Date of Birth (DD/MM/YYYY):").grid(row=5, column=0, sticky="w", pady=5)
        self.dob_entry = ttk.Entry(main_frame, width=35)
        self.dob_entry.grid(row=5, column=1, pady=5)
        
        # Gender
        ttk.Label(main_frame, text="Gender:").grid(row=6, column=0, sticky="w", pady=5)
        self.gender_var = tk.StringVar()
        gender_frame = ttk.Frame(main_frame)
        gender_frame.grid(row=6, column=1, sticky="w")
        ttk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, 
                       value="Male").pack(side=tk.LEFT)
        ttk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, 
                       value="Female").pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(gender_frame, text="Other", variable=self.gender_var, 
                       value="Other").pack(side=tk.LEFT)
        
        # City
        ttk.Label(main_frame, text="City:").grid(row=7, column=0, sticky="w", pady=5)
        self.city_entry = ttk.Entry(main_frame, width=35)
        self.city_entry.grid(row=7, column=1, pady=5)
        
        # State
        ttk.Label(main_frame, text="State:").grid(row=8, column=0, sticky="w", pady=5)
        self.state_entry = ttk.Entry(main_frame, width=35)
        self.state_entry.grid(row=8, column=1, pady=5)
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=9, column=0, columnspan=2, pady=20)
        
        submit_btn = ttk.Button(button_frame, text="Submit", command=self.submit_form)
        submit_btn.pack(side=tk.LEFT, padx=5)
        
        reset_btn = ttk.Button(button_frame, text="Reset", command=self.reset_form)
        reset_btn.pack(side=tk.LEFT, padx=5)
        
        exit_btn = ttk.Button(button_frame, text="Exit", command=root.quit)
        exit_btn.pack(side=tk.LEFT, padx=5)
    
    def animate_title(self):
        """Animate the title by changing colors"""
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
        self.color_index = 0
        def change_color():
            self.title_label.configure(foreground=colors[self.color_index])
            self.color_index = (self.color_index + 1) % len(colors)
            self.root.after(500, change_color)  # Change color every 500ms
        change_color()
    
    def validate_form(self):
        """Validate form inputs"""
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        aadhar = self.aadhar_entry.get().strip()
        dob = self.dob_entry.get().strip()
        city = self.city_entry.get().strip()
        state = self.state_entry.get().strip()
        
        # Validation checks
        if not name:
            messagebox.showerror("Error", "Name is required!")
            return False
        
        if name and not name.isalpha():
            messagebox.showerror("Error", "Name should contain only alphabets!")
            return False
        
        if email and not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            messagebox.showerror("Error", "Invalid email format!")
            return False
        
        if phone and not re.match(r'^\d{10}$', phone):
            messagebox.showerror("Error", "Phone should be 10 digits!")
            return False
        
        if aadhar and not re.match(r'^\d{12}$', aadhar):
            messagebox.showerror("Error", "Aadhar should be 12 digits!")
            return False
        
        return True
    
    def submit_form(self):
        """Submit form and display data"""
        if not self.validate_form():
            return
        
        data = f"""
=== SUBMITTED INFORMATION ===

Name: {self.name_entry.get().strip()}
Email: {self.email_entry.get().strip()}
Phone: {self.phone_entry.get().strip()}
Aadhar Card: {self.aadhar_entry.get().strip()}
Date of Birth: {self.dob_entry.get().strip()}
Gender: {self.gender_var.get()}
City: {self.city_entry.get().strip()}
State: {self.state_entry.get().strip()}

===============================
        """
        
        messagebox.showinfo("Success", "Form submitted successfully!\n" + data)
    
    def reset_form(self):
        """Reset all form fields"""
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.aadhar_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.state_entry.delete(0, tk.END)
        self.gender_var.set("")
        messagebox.showinfo("Info", "Form reset successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
