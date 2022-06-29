# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:47:53 2021

@author: Khoa Tran
"""

HEIGHT = 500
WIDTH = 700

BG = "#FFFBD2"
buttonBG = "#D3D3D3"


def FixPatientName():


    def info_function(path_dicoms,old_name,new_ID):
        DC = pydicom.dcmread(str(path_dicoms) + "\\" + str(old_name) + ".dcm")
        DC.PatientName = new_ID
        DC.save_as(path_dicoms + "\\" + str(old_name) + ".dcm")
        a = "This file PatientName were changed: " + str(old_name)
        b = "You can continue to change other file PatientName\n without restart the application"
        label2 = tk.Label(frame, text = a,bg=BG,font=("Arial", 13), fg ="black")
        label2.place(relx=0.05,rely=0.73,relwidth =0.9, relheight=0.08)
        label3 = tk.Label(frame, text = b,bg=BG,font=("Arial", 13), fg ="black")
        label3.place(relx=0.05,rely=0.8,relwidth =0.9, relheight=0.13)
    
    from packages_imports import pydicom
    from packages_imports import tk
    
    root = tk.Tk()
    root.title('FixPatientName')

    
    
    canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
    canvas.pack()
    
    
    
    frame = tk.Frame(root, bg= BG)
    frame.place(relx=0.01,rely=0.01,relwidth =0.98, relheight=0.98)
    
    label0 = tk.Label(frame, text = "Fix-Patient-Name", 
                     bg=BG,font=(".VnCooperH", 30), fg ="#FF4E50")
    label0.place(relx=0.05,rely=0.001,relwidth =0.9, relheight=0.15)
    
    label1 = tk.Label(frame, text = "Please input the path to the DICOM folder\n (this folder should only have DICOM files with '*.dcm' extension)", 
                     bg=BG,font=("Arial", 12), fg ="black")
    label1.place(relx=0.05,rely=0.17,relwidth =0.9, relheight=0.075)
    
    path_dicoms = tk.Entry(frame, bg='white',font=("Arial", 11))
    path_dicoms.place(relx=0.1,rely=0.3,relwidth =0.8, relheight=0.05)
    
    
    old_name = tk.Label(frame, text = "File name \n (do not include '*.dcm' extension):", 
                     bg=BG,font=("Arial", 12), fg ="black")
    old_name.place(relx=0.05,rely=0.4,relwidth =0.4, relheight=0.12)

    old_name = tk.Entry(frame, bg='white',font=("Arial", 11))
    old_name.place(relx=0.1,rely=0.55,relwidth =0.3, relheight=0.05)
    
    new_ID = tk.Label(frame, text = "New PatientName:", 
                     bg=BG,font=("Arial", 12), fg ="black")
    new_ID.place(relx=0.55,rely=0.4,relwidth =0.4, relheight=0.12)

    new_ID = tk.Entry(frame, bg='white',font=("Arial", 11))
    new_ID.place(relx=0.6,rely=0.55,relwidth =0.3, relheight=0.05)
    
    button2 = tk.Button(frame, text="Process",font=("Arial", 12), bg =buttonBG,command=lambda: info_function(path_dicoms.get(),old_name.get(),new_ID.get()))
    button2.place(relx=0.4,rely=0.65,relwidth =0.2, relheight=0.08)
    
    
    root.mainloop()


