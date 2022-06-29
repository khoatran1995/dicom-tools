# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 10:40:23 2021

@author: Khoa Tran
"""
mainHEIGHT = 600
mainWIDTH = 350

HEIGHT = 500
WIDTH = 800

BG = "#FFFBD2"
buttonBG = "#D3D3D3"


def DicominfoGUI():
    os.system('DicominfoGUI.py')

from packages_imports import os


from packages_imports import tk


from DicominfoGUI import Dicominfo

from PatientID2Filename import PatientID2Filename

from FixPatientID import FixPatientID

from FixPatientName import FixPatientName

from FixPatientIDMass import FixPatientIDMass

from FixPatientNameMass import FixPatientNameMass

from ChangeExtensionMass import ChangeExtension

root = tk.Tk()
root.title('Dicom-Tools')

canvas = tk.Canvas(root, height = mainHEIGHT, width = mainWIDTH)
canvas.pack()



frame = tk.Frame(root, bg= BG)
frame.place(relx=0.01,rely=0.01,relwidth =0.99, relheight=0.99)

label0 = tk.Label(frame, text = "DICOM-TOOLS", 
                 bg=BG,font=(".VnCooperH", 25), fg ="#FF4E50")
label0.place(relx=0.05,rely=0.0001,relwidth =0.9, relheight=0.10)

label4 = tk.Label(frame, text = "Written by Khoa Tran, 8/2021\n Email: tukhoatran95@gmail.com", bg=BG,
                  font=("Arial", 8), fg ="black")
label4.place(relx=0.2,rely=0.925,relwidth =0.6, relheight=0.075)

button1 = tk.Button(frame, text="Extracting information",font=("Arial", 11), 
                    bg =buttonBG,command=lambda: Dicominfo())
button1.place(relx=0.05,rely=0.13,relwidth =0.9, relheight=0.075)

button2 = tk.Button(frame, text="Change DICOM filename to PatientID",font=("Arial", 11), 
                    bg = buttonBG, command=lambda: PatientID2Filename())
button2.place(relx=0.05, rely=0.25,relwidth =0.9, relheight=0.075)

button3 = tk.Button(frame, text="Modify PatientID 1 by 1",font=("Arial", 11),
                    bg =buttonBG,command=lambda: FixPatientID())
button3.place(relx=0.05,rely=0.37,relwidth =0.9, relheight=0.075)

button4 = tk.Button(frame, text="Modify PatientID Mass",font=("Arial", 11),
                    bg = buttonBG,command=lambda: FixPatientIDMass())
button4.place(relx=0.05,rely=0.49,relwidth =0.9, relheight=0.075)

button5 = tk.Button(frame, text="Modify PatientName 1 by 1",font=("Arial", 11),
                    bg = buttonBG,command=lambda: FixPatientName())
button5.place(relx=0.05,rely=0.61,relwidth =0.9, relheight=0.075)

button7 = tk.Button(frame, text="Modify PatientName Mass",font=("Arial", 11),
                    bg = buttonBG,command=lambda: FixPatientNameMass())
button7.place(relx=0.05,rely=0.73,relwidth =0.9, relheight=0.075)

button6 = tk.Button(frame, text="Correct DICOM files extension",font=("Arial", 11),
                    bg = buttonBG,command=lambda: ChangeExtension())
button6.place(relx=0.05,rely=0.85,relwidth =0.9, relheight=0.075)

root.mainloop()