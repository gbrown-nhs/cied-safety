import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import medtronic
from datetime import datetime
import popups
import datechecks

def process_data(email_recipient, patient_name, mrn, dob, referral, generator_model, ra_lead_model, rv_lead_model, lv_lead_model, generator_implantation_date, ra_implantation_date, rv_implantation_date, lv_implantation_date,
                 mrscl_ref, all_medtronic, device_type):
    if all_medtronic == False:
        popups.mixed_manuf_warning()
    else:
        datechecks.check_impl_date(generator_implantation_date, ra_implantation_date, rv_implantation_date, lv_implantation_date)
        if device_type == "Single chamber PPM":
            medtronic.CIED_single_chamber_ppm(email_recipient, patient_name, mrn, dob, referral, generator_model, rv_lead_model, generator_implantation_date, rv_implantation_date, mrscl_ref)
        elif device_type == "Dual chamber PPM":
            medtronic.CIED_dual_chamber_ppm(email_recipient, patient_name, mrn, dob, referral, generator_model, ra_lead_model, rv_lead_model, generator_implantation_date, ra_implantation_date, rv_implantation_date, mrscl_ref)     
        else:
            popups.device_not_supported_error()   


class DeviceFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medtronic CIED Information Form")

        self.fields = {
            "Email recipient": tk.StringVar(),
            "Patient name": tk.StringVar(),
            "MRN": tk.StringVar(),
            "DoB": tk.StringVar(),
            "Referred for": tk.StringVar(),
            "Generator model number": tk.StringVar(),
            "RA Lead model number": tk.StringVar(),
            "RV Lead model number": tk.StringVar(),
            "LV Lead model number": tk.StringVar(),
            "Generator implantation date": tk.StringVar(),
            "RA Lead implantation date": tk.StringVar(),
            "RV Lead implantation date": tk.StringVar(),
            "LV Lead implantation date": tk.StringVar(),
            "MRSCL reference number": tk.StringVar()
        }

        self.input_widgets = {}  # Store row widgets to show/hide
        section_font = font=tkFont.Font(size=12, weight=tkFont.BOLD)
        row = 0

        tk.Label(root, text="Safety call information", font=section_font).grid(row=row, column=0, sticky='w', padx=10, pady=5)
        row += 1

        tk.Label(root, text="Email recipient").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["Email recipient"], width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.input_widgets["Email recipient"] = entry
        row += 1

        tk.Label(root, text="Patient name").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["Patient name"], width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.input_widgets["Patient name"] = entry
        row += 1

        tk.Label(root, text="MRN").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["MRN"], width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.input_widgets["MRN"] = entry
        row += 1

        tk.Label(root, text="DoB").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["DoB"], width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.input_widgets["DoB"] = entry
        row += 1

        tk.Label(root, text="Referred for").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["Referred for"], width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.input_widgets["Referred for"] = entry
        row += 1

        tk.Label(root, text="MRSCL reference number").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["MRSCL reference number"], width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.input_widgets["MRSCL reference number"] = entry
        row += 1

        tk.Label(root, text="Device information", font=section_font).grid(row=row, column=0, sticky='w', padx=10, pady=5)
        row += 1


        # Dropdown for device type
        self.device_type = tk.StringVar()
        self.device_type.set("Single chamber PPM")  # Default

        tk.Label(root, text="Device Type").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        dropdown = tk.OptionMenu(root, self.device_type,
                                 "Single chamber PPM", "Dual chamber PPM", "Leadless PPM", "CRT-D", "CRT-P", "DR-ICD", "VR-ICD",
                                 command=self.update_fields_visibility)
        dropdown.grid(row=row, column=1, padx=10, pady=5)
        row += 1


        tk.Label(root, text="Generator model number").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["Generator model number"], width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.input_widgets["Generator model number"] = entry
        tk.Label(root, text="Generator implantation date").grid(row=row, column=2, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["Generator implantation date"], width=40)
        entry.grid(row=row, column=3, padx=10, pady=5)
        self.input_widgets["Generator implantation date"] = entry
        row += 1

        tk.Label(root, text="RA Lead model number").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["RA Lead model number"], width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.input_widgets["RA Lead model number"] = entry
        tk.Label(root, text="RA Lead implantation date").grid(row=row, column=2, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["RA Lead implantation date"], width=40)
        entry.grid(row=row, column=3, padx=10, pady=5)
        self.input_widgets["RA Lead implantation date"] = entry
        row += 1

        tk.Label(root, text="RV Lead model number").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["RV Lead model number"], width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.input_widgets["RV Lead model number"] = entry
        tk.Label(root, text="RV Lead implantation date").grid(row=row, column=2, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["RV Lead implantation date"], width=40)
        entry.grid(row=row, column=3, padx=10, pady=5)
        self.input_widgets["RV Lead implantation date"] = entry
        row += 1

        tk.Label(root, text="LV Lead model number").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["LV Lead model number"], width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.input_widgets["LV Lead model number"] = entry
        tk.Label(root, text="LV Lead implantation date").grid(row=row, column=2, sticky='w', padx=10, pady=5)
        entry = tk.Entry(root, textvariable=self.fields["LV Lead implantation date"], width=40)
        entry.grid(row=row, column=3, padx=10, pady=5)
        self.input_widgets["LV Lead implantation date"] = entry
        row += 1


        # Boolean checkboxes
        self.checkboxes = {
            "All system components are Medtronic": tk.BooleanVar()
        }

        for label, var in self.checkboxes.items():
            tk.Checkbutton(root, text=label, variable=var).grid(row=row, column=0, columnspan=2, sticky='w', padx=10, pady=5)
            row += 1

        tk.Button(root, text="Submit", command=self.submit).grid(row=row, column=0, columnspan=2, pady=15)

        self.update_fields_visibility(self.device_type.get())  # Initialize visibility

    def update_fields_visibility(self, device_type):
        """Show/hide fields based on device type selection."""
        if device_type == "Single chamber PPM":
            self.input_widgets["RA Lead model number"].grid_remove()
            self.input_widgets["RV Lead model number"].grid()
            self.input_widgets["LV Lead model number"].grid_remove()
            self.input_widgets["RA Lead implantation date"].grid_remove()
            self.input_widgets["RV Lead implantation date"].grid()
            self.input_widgets["LV Lead implantation date"].grid_remove()
        elif device_type == "Dual chamber PPM":
            self.input_widgets["RA Lead model number"].grid()
            self.input_widgets["RV Lead model number"].grid()
            self.input_widgets["LV Lead model number"].grid_remove()
            self.input_widgets["RA Lead implantation date"].grid()
            self.input_widgets["RV Lead implantation date"].grid()
            self.input_widgets["LV Lead implantation date"].grid_remove()
        elif device_type == "CRT-D":
            self.input_widgets["RA Lead model number"].grid()
            self.input_widgets["RV Lead model number"].grid()
            self.input_widgets["LV Lead model number"].grid()
        elif device_type == "CRT-P":
            self.input_widgets["RA Lead model number"].grid()
            self.input_widgets["RV Lead model number"].grid()
            self.input_widgets["LV Lead model number"].grid()
        elif device_type == "DR-ICD":
            self.input_widgets["RA Lead model number"].grid()
            self.input_widgets["RV Lead model number"].grid()
            self.input_widgets["LV Lead model number"].grid_remove()
        elif device_type == "VR-ICD":
            self.input_widgets["RA Lead model number"].grid_remove()
            self.input_widgets["RV Lead model number"].grid()
            self.input_widgets["LV Lead model number"].grid_remove()
        elif device_type == "Leadless PPM":
            self.input_widgets["RA Lead model number"].grid_remove()
            self.input_widgets["RV Lead model number"].grid_remove()
            self.input_widgets["LV Lead model number"].grid_remove()
            self.input_widgets["RA Lead implantation date"].grid_remove()
            self.input_widgets["RV Lead implantation date"].grid_remove()
            self.input_widgets["LV Lead implantation date"].grid_remove()
        else:
            # Default: show all
            for widget in self.input_widgets.values():
                widget.grid()

    def submit(self):
        # Get all field values
        email_recipient = self.fields["Email recipient"].get()
        patient_name = self.fields["Patient name"].get()
        mrn = self.fields["MRN"].get()
        dob = self.fields["DoB"].get()
        referral = self.fields["Referred for"].get()
        generator_model = self.fields["Generator model number"].get().upper()
        ra_lead_model = self.fields["RA Lead model number"].get()
        rv_lead_model = self.fields["RV Lead model number"].get()
        lv_lead_model = self.fields["LV Lead model number"].get()
        generator_implantation_date = self.fields["Generator implantation date"].get()
        ra_implantation_date = self.fields["RA Lead implantation date"].get()
        rv_implantation_date = self.fields["RV Lead implantation date"].get()
        lv_implantation_date = self.fields["LV Lead implantation date"].get()
        mrscl_ref = self.fields["MRSCL reference number"].get()

        # Get checkboxes
        all_medtronic = self.checkboxes["All system components are Medtronic"].get()

        # Device type
        device_type = self.device_type.get()

        # Call processing function
        process_data(email_recipient, patient_name, mrn, dob, referral, generator_model, ra_lead_model, rv_lead_model, lv_lead_model,
                     generator_implantation_date, ra_implantation_date, rv_implantation_date, lv_implantation_date, mrscl_ref,
                     all_medtronic, device_type)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DeviceFormApp(root)
    root.mainloop()
