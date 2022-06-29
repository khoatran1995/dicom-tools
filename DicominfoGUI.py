# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 20:26:34 2021

@author: Khoa Tran
"""
HEIGHT = 400
WIDTH = 700


BG = "#FFFBD2"
buttonBG = "#D3D3D3"


def Dicominfo():


    def info_function(path_dicoms):
        filename = os.listdir(path_dicoms)
        dicom_paths = [path_dicoms + "\\"+s for s in filename]

        info_data = pd.DataFrame(columns = ['PatientID', 'Name', 'YOB','Gender','CXRDate','CXRTime','StudyID','FilePath']) 
    
        for s in dicom_paths:
           a = pydicom.dcmread(s,force=True)
           info_data = info_data.append({'PatientID':a.PatientID, 'Name':a.PatientName,'YOB':a.PatientBirthDate,'CXRDate':a.StudyDate,'CXRTime':a.StudyTime,'Gender':a.PatientSex, 'StudyID':a.StudyID,'FilePath': s},ignore_index=True)
        output_folder = path_dicoms + "\\"  + "PatientList.xlsx"
        info_data.to_excel(output_folder)
        a = "Data of " + str(len(info_data)) + " DICOM files were exported to the 'PatientList.xlsx' file at:\n " + path_dicoms
        b = "If you want to rerun this tool with this folder, please remove the file 'PatientList.xlsx' \n from the it and click 'Process' again"
        label2 = tk.Label(frame, text = a,bg=BG,font=("Arial", 12), fg ="black")
        label2.place(relx=0.05,rely=0.65,relwidth =0.9, relheight=0.1)
        label3 = tk.Label(frame, text = b,bg=BG,font=("Arial", 12), fg ="black")
        label3.place(relx=0.05,rely=0.75,relwidth =0.9, relheight=0.12)
    
    from packages_imports import pydicom
    from packages_imports import os
    from packages_imports import pd  
    from packages_imports import tk
    
    root = tk.Tk()
    root.title('Dicom-Info')

    
    canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
    canvas.pack()
    
    
    frame = tk.Frame(root, bg= BG)
    frame.place(relx=0.01,rely=0.01,relwidth =0.98, relheight=0.98)
    
    label0 = tk.Label(frame, text = "DICOM-INFO", 
                     bg=BG,font=(".VnCooperH", 30), fg ="#FF4E50")
    label0.place(relx=0.05,rely=0.001,relwidth =0.9, relheight=0.2)
    
    label1 = tk.Label(frame, text = "Please input the path to the DICOM folder\n (this folder should only have DICOM files with '*.dcm' extension)", 
                     bg=BG,font=("Arial", 12), fg ="black")
    label1.place(relx=0.05,rely=0.2,relwidth =0.9, relheight=0.1)
    
    path_dicoms = tk.Entry(frame, bg='white',font=("Arial", 11))
    path_dicoms.place(relx=0.1,rely=0.35,relwidth =0.8, relheight=0.1)
    
    
    button = tk.Button(frame, text="Process",font=("Arial", 11), bg = buttonBG,command=lambda: info_function(path_dicoms.get()))
    button.place(relx=0.425,rely=0.50,relwidth =0.2, relheight=0.1)
    
    root.mainloop()