import tkinter
import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

#function to calculate the confidence interval + display on app
def calculate_interval():
    #obtain inputs from sample mean, standard deviation, and sample size
    sm = sample_mean_input.get()
    sd = standard_deviation_input.get()
    ss = sample_size_input.get()
    #do math
    error = float(sd)/math.sqrt(float(ss))
    #calculate the z star value
    if(i.get() == 1):
        z_star = 1.282
    if(i.get() == 2):
        z_star = 1.440
    if(i.get() == 3):
        z_star = 1.645
    if(i.get() == 4):
        z_star = 1.960
    if(i.get() == 5):
        z_star = 2.576
    if(i.get() == 6):
        z_star = 2.807
    if(i.get() == 7):
        z_star = 3.291
    else:
        z_star = 1.96
    #do more math
    new_interval = z_star * error
    #setting string display
    string_to_display = "The Confidence Interval is " + sm + " \u00B1" + str(new_interval)
    var_1.set(string_to_display)

#basic setup
root = tkinter.Tk()
root.title("Confidence Interval Calculator")

#variables used
var_1 = tkinter.StringVar()
i= tkinter.IntVar()

#frames to group stuff
frame_labels = tkinter.Frame(root) #sample mean, standard deviation, and sample size
frame_choice = tkinter.Frame(root) #confidence interval choices
frame_button = tkinter.Frame(root) #calculate button
frame_answer = tkinter.Frame(root) #answer

#entry for sample mean, standard deviation, and sample size (label + input)
sample_mean = tkinter.Label(frame_labels, text = 'Sample Mean',).grid(row = 0)
standard_deviation = tkinter.Label(frame_labels, text = 'Standard Deviation').grid(row=1)
sample_size = tkinter.Label(frame_labels, text = 'Sample Size').grid(row=2)
sample_mean_input = tkinter.Entry(frame_labels)
standard_deviation_input = tkinter.Entry(frame_labels)
sample_size_input = tkinter.Entry(frame_labels)

#confidence interval choices between 80-99.9%
interval_1 = tkinter.Radiobutton(frame_choice, text = "80%", value = 1, variable = i)
interval_2 = tkinter.Radiobutton(frame_choice, text = "85%", value = 2, variable = i)
interval_3 = tkinter.Radiobutton(frame_choice, text = "90%", value = 3, variable = i)
interval_4 = tkinter.Radiobutton(frame_choice, text = "95%", value = 4, variable = i)
interval_5 = tkinter.Radiobutton(frame_choice, text = "99%", value = 5, variable = i)
interval_6 = tkinter.Radiobutton(frame_choice, text = "99.5%", value = 6, variable = i)
interval_7 = tkinter.Radiobutton(frame_choice, text = "99.9%", value = 7, variable = i)

#calculate button
calculate_button = tkinter.Button(frame_button, text = 'Calculate', command = calculate_interval)

#The confidence interval is....
answer = tkinter.Label(frame_answer, textvariable = var_1)

#input orientation
sample_mean_input.grid(row = 0, column = 1)
standard_deviation_input.grid(row = 1, column = 1)
sample_size_input.grid(row = 2, column = 1)

#interval orientation
interval_1.grid(row=3, column = 0)
interval_2.grid(row=3, column = 1)
interval_3.grid(row=3, column = 2)
interval_4.grid(row=3, column = 3)
interval_5.grid(row=3, column = 4)
interval_6.grid(row=3, column = 5)
interval_7.grid(row=3, column = 6)

#calculate button orientation
calculate_button.grid(row=4)

#answer orientation
answer.grid(row=5)

#frame orientation
frame_labels.grid(column = 0, row = 0)
frame_choice.grid(column = 0, row = 1)
frame_button.grid(column = 0, row = 2)
frame_answer.grid(column = 0, row = 3)

root.mainloop()
