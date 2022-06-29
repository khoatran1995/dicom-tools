# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 15:03:49 2021

@author: Khoa Tran
"""

HEIGHT = 400
WIDTH = 700


BG = "#FFFBD2"
buttonBG = "#D3D3D3"


def FixPatientIDMass():

    def info_function(path_dicoms):
        info_data = pd.read_excel(path_dicoms + "\\PatientList.xlsx","Sheet1")
        for s in info_data.SN:
            z = pydicom.dcmread(info_data.FilePath[s],force=True)
            z.PatientID = str(info_data.NewPatientID[s])
            z.save_as(info_data.FilePath[s])
        a = "Completed. You can change these file names to its PatientID by tool 'PatientID->Filename'"
        b = "Note: Copy these files to a different folder before using tool 'PatientID->Filename'"
        label2 = tk.Label(frame, text = a,bg=BG,font=("Arial", 12), fg ="black")
        label2.place(relx=0.05,rely=0.77,relwidth =0.9, relheight=0.05)
        label3 = tk.Label(frame, text = b,bg=BG,font=("Arial", 11), fg ="black")
        label3.place(relx=0.,rely=0.85, relwidth =1, relheight=0.05)
    
    
    from packages_imports import pydicom
    from packages_imports import pd  
    from packages_imports import tk
    
    root = tk.Tk()
    root.title('FixPatientID-Mass')

    
    canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
    canvas.pack()
    
    
    frame = tk.Frame(root, bg= BG)
    frame.place(relx=0.01,rely=0.01,relwidth =0.98, relheight=0.98)
    
    label0 = tk.Label(frame, text = "Fix-Patient-ID-Mass", 
                     bg=BG,font=(".VnCooperH", 30), fg ="#FF4E50")
    label0.place(relx=0.05,rely=0.001,relwidth =0.9, relheight=0.2)
    
    label1 = tk.Label(frame, text = "Note: Extract DICOM information into the Excel file 'PatientList.xlsx'using tool Dicom-Info \n and change the first row header to 'SN' and add one collumn 'NewPatientID'\n and copy the file to another folder", 
                     bg=BG,font=("Arial", 10), fg ="black")
    label1.place(relx=0.05,rely=0.2,relwidth =0.9, relheight=0.15)
    
    label5 = tk.Label(frame, text = "Please input the path of the folder containing the modified Excel file 'PatientList':", 
                     bg=BG,font=("Arial", 12), fg ="black")
    label5.place(relx=0.05,rely=0.34,relwidth =0.9, relheight=0.1)
    
    path_dicoms = tk.Entry(frame, bg='white',font=("Arial", 11))
    path_dicoms.place(relx=0.1,rely=0.45,relwidth =0.8, relheight=0.1)
    
    button = tk.Button(frame, text="Process",font=("Arial", 11), bg = buttonBG,command=lambda: info_function(path_dicoms.get()))
    button.place(relx=0.35,rely=0.6,relwidth =0.3, relheight=0.1)
    
    root.mainloop()
    