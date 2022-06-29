# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 09:55:25 2021

@author: Khoa Tran
"""


HEIGHT = 350
WIDTH = 800

BG = "#FFFBD2"
buttonBG = "#D3D3D3"

def ChangeExtension():


    def info_function(path_dicoms):
              
        
        filename = os.listdir(path_dicoms)
        dicom_paths = [path_dicoms + "\\" + s for s in filename]
        
        for s in dicom_paths:
          base = os.path.splitext(s)[0]
          newname = base +".dcm"
          os.rename(s,newname)
        a = str(len(dicom_paths)) +  " DICOM files extension changed to '*.DCM'"
        label2 = tk.Label(frame, text = a,bg=BG,font=("Arial", 11), fg ="black")
        label2.place(relx=0.05,rely=0.75,relwidth =0.9, relheight=0.2)
    
    from packages_imports import os
    from packages_imports import tk
    
    root = tk.Tk()
    root.title('DICOM Files Extension -> *.DCM')
  
    
    canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
    canvas.pack()
    
    
    
    frame = tk.Frame(root, bg= BG)
    frame.place(relx=0.01,rely=0.01,relwidth =0.98, relheight=0.98)
    
    label0 = tk.Label(frame, text = "Extension->.DCM", 
                     bg=BG,font=(".VnCooperH", 30), fg ="#FF4E50")
    label0.place(relx=0.05,rely=0.001,relwidth =0.9, relheight=0.2)
    
    label1 = tk.Label(frame, text = "Path to folder of DICOM files without the '*.DCM' extention:", 
                     bg=BG,font=("Arial", 12), fg ="black")
    label1.place(relx=0.05,rely=0.25,relwidth =0.9, relheight=0.1)
    
    path_dicoms = tk.Entry(frame, bg='white',font=("Arial", 11))
    path_dicoms.place(relx=0.1,rely=0.39,relwidth =0.8, relheight=0.15)
    
    
    button = tk.Button(frame, text="Process",font=("Arial", 13), bg =buttonBG,command=lambda: info_function(path_dicoms.get()))
    button.place(relx=0.35,rely=0.6,relwidth =0.3, relheight=0.13)
    
    root.mainloop()
    

 