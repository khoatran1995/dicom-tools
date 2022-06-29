# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:11:42 2021

@author: Khoa Tran
"""

HEIGHT = 500
WIDTH = 800

BG = "#FFFBD2"
buttonBG = "#D3D3D3"

def PatientID2Filename():


    def info_function(path_dicoms):
              
        
        filename = os.listdir(path_dicoms)
        dicom_paths = [path_dicoms + "\\" + s for s in filename]
        
        
        for s in dicom_paths:
          a = pydicom.dcmread(s, force = True)
          newname = path_dicoms+ "\\" + a.PatientID +".dcm"
          if os.path.isfile(newname) == True :
              dupname = path_dicoms+ "\\" + a.PatientID + "dup1.dcm"
              if os.path.isfile(dupname) == True :
                 dupname = path_dicoms+ "\\" + a.PatientID +"dup2.dcm"
                 if os.path.isfile(dupname) == True :
                    dupname = path_dicoms+ "\\" + a.PatientID +"dup3.dcm"
                    if os.path.isfile(dupname) == True :
                        dupname = path_dicoms+ "\\" + a.PatientID +"dup3.dcm"
                        os.rename(s,dupname)
                    else:
                        os.rename(s,dupname)
                 else:   
                    os.rename(s,dupname)
              else:   
                 os.rename(s,dupname)     
          else:
              os.rename(s,newname)
        a = str(len(dicom_paths)) +  " DICOM files were changed the file name to its PatientID.\n The files with 'dup' at the end are the duplicate PatientIDs. \n Using FixPatientID to fix the PatientIDs."
        b = "You should change all DICOM files to another name (eg. whatever) \n before rerun this tool for the renamed DICOM files. \n Otherwise, they could be not correct."
        label2 = tk.Label(frame, text = a,bg=BG,font=("Arial", 11), fg ="black")
        label2.place(relx=0.05,rely=0.61,relwidth =0.9, relheight=0.2)
        label3 = tk.Label(frame, text = b,bg=BG,font=("Arial", 11), fg ="black")
        label3.place(relx=0.05,rely=0.80,relwidth =0.9, relheight=0.13)
    
    from packages_imports import pydicom
    from packages_imports import os
    from packages_imports import tk
    
    root = tk.Tk()
    root.title('PatientID->Filename')
  
    
    canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
    canvas.pack()
    
    
    
    frame = tk.Frame(root, bg= BG)
    frame.place(relx=0.01,rely=0.01,relwidth =0.98, relheight=0.98)
    
    label0 = tk.Label(frame, text = "PatientID->Filename", 
                     bg=BG,font=(".VnCooperH", 30), fg ="#FF4E50")
    label0.place(relx=0.05,rely=0.001,relwidth =0.9, relheight=0.2)
    
    label1 = tk.Label(frame, text = "Please input the path to the DICOM folder\n (this folder should only have DICOM files with '*.dcm' extension)", 
                     bg=BG,font=("Arial", 12), fg ="black")
    label1.place(relx=0.05,rely=0.2,relwidth =0.9, relheight=0.1)
    
    path_dicoms = tk.Entry(frame, bg='white',font=("Arial", 11))
    path_dicoms.place(relx=0.1,rely=0.35,relwidth =0.8, relheight=0.1)
    
    
    button = tk.Button(frame, text="Process",font=("Arial", 11), bg =buttonBG,command=lambda: info_function(path_dicoms.get()))
    button.place(relx=0.425,rely=0.50,relwidth =0.2, relheight=0.1)
    
    root.mainloop()
    
    


 
