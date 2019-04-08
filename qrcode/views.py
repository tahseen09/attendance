from django.shortcuts import render
from django.http import HttpResponse
from . models import students
import subprocess
from MyQR import myqr
import os
import csv
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import datetime, time
from . models import students

# Create your views here.
def index(request):
    if request.method == "POST":
        roll = request.POST.get("roll")
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        semester = request.POST.get("semester")
        s = students(roll = roll, name=name, subject=subject, semester=semester)
        s.save()
        version, level, qr_name = myqr.run(
        str(name),
        version = 1,
        level = 'H',
        #you can use any picture in the background including gif
        #picture = 'a.jpg',
        colorized = True,
        contrast = 1.0,
        brightness = 1.0,
        save_name = roll+'.jpg',
        save_dir = os.getcwd()
        )
        msg = "Student is registered."
        return render(request,"index.html",{'msg':msg})
    else:
        return render(request,"index.html")

def present(request):
    x = subprocess.check_output(['python', 'present.py'])
    name = x.decode("utf-8")
    name = name[0:len(name)-1]
    
    ans = students.objects.get(name__iexact=name)
    
    semester = ans.semester
    subject = ans.subject
    roll = ans.roll
    path = subject+".csv"
    with open(path,'a') as file:
        writer = csv.writer(file)
        if os.stat(path).st_size == 0:
            writer.writerow(["Timestamp","Name","Roll","Semester"])
        writer.writerow([datetime.datetime.now(),name,roll,semester])
    file.close()
    return HttpResponse(name)