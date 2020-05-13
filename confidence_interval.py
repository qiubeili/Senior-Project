import tkinter
import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

#dictionary for z star values
interval = {
    1: 1.282,
    2: 1.440,
    3: 1.645,
    4: 1.960,
    5: 2.576,
    6: 2.807,
    7: 3.291,
}

#function to calculate the confidence interval + display on app
def calculate_interval():
    #obtain inputs from sample mean, standard deviation, and sample size
    sm = sample_mean_input.get()
    sd = standard_deviation_input.get()
    ss = sample_size_input.get()
    #do math
    error = float(sd)/math.sqrt(float(ss))
    #calculate the z star value
    for x in interval:
        x = i.get()
        z_star= interval[x]
    #do more math
    new_interval = float(z_star) * error
    #setting string display
    string_to_display = "Confidence Interval:  " + sm + " \u00B1 " + str(new_interval)
    var_1.set(string_to_display)
#function to graph out confidence interval calculated
def graphing():
    graph = tkinter.Toplevel()

    sm = sample_mean_input.get()
    sd = standard_deviation_input.get()
    ss = sample_size_input.get()
    error = float(sd)/math.sqrt(float(ss))

    for x in interval:
        x = i.get()
        z_star= interval[x]

    new_interval = float(z_star) * error
    #graphing part
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    x = np.linspace(float(sm) - 3 * float(sd), float(sm) + 3 * float(sd), 10000)
    nVals = [norm.pdf(i,float(sm),float(sd)) for i in x]
    ax.plot(x,nVals)
    x1 = float(sm) - new_interval
    x2 = float(sm) + new_interval
    ax.fill_between(x,nVals,color = '#111111',where = (x > x1) & (x < x2))

    canvas = FigureCanvasTkAgg(fig, master= graph)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, graph)
    toolbar.update()

    button = tkinter.Button(master=graph, text="Quit", command=graph.destroy)

    button.pack(side=tkinter.BOTTOM)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


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
graph_button = tkinter.Button(frame_button, text = 'Show Graph', command = graphing)

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
calculate_button.grid(row=4, column = 0)
graph_button.grid(row=4, column = 1)

#answer orientation
answer.grid(row=5)

#frame orientation
frame_labels.grid(column = 0, row = 0)
frame_choice.grid(column = 0, row = 1)
frame_button.grid(column = 0, row = 2)
frame_answer.grid(column = 0, row = 3)

root.mainloop()
