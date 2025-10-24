from tkinter import messagebox

# warnings and information messages

def not_cond_warning():
    messagebox.showwarning(title="Patient warning", message="The system is NOT MR Conditional. Don't you bloody dare scan that patient!!!!!1!!!!!!")

def lead_3830_warning():
    messagebox.showwarning(title="Patient warning", message="This system contains the 3830 lead. Please perform a manual check and confirm lead placement.")

def conditional_message():
    messagebox.showinfo(title="MR Conditional system", message="This is an MR Conditional system. Advice has been created.")

def error_in_check():
    messagebox.showwarning(title="Error", message="There was an error in the system check.")

def mixed_manuf_warning():
    messagebox.showwarning(title="Patient warning", message="The mixed manufacturer system can not be scanned at ICHT.")

def device_not_supported_error():
    messagebox.showinfo("Error", "This device type isn't supported yet")

def six_week_warning(date):
    messagebox.showwarning(title="Patient warning", message=f"The system was implanted less than 6 weeks ago. If the system is MR Conditional, The patient can not be scanned before {date}.")