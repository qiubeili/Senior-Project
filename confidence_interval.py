import tkinter
import math
from scipy.stats import norm
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

#dictionary for z star values
interval_num_to_value = {
    1: 1.282,
    2: 1.440,
    3: 1.645,
    4: 1.960,
    5: 2.576,
    6: 2.807,
    7: 3.291,
}

#function to calculate the confidence interval + display on app
def calculate_interval(sample_mean, standard_deviation, sample_size, interval):
    #obtain inputs from sample mean, standard deviation, and sample size
    sample_mean_value = sample_mean_input.get()
    standard_deviation_value = standard_deviation_input.get()
    sample_size_value = sample_size_input.get()
    interval = interval_var.get()
    if (not (sample_mean_value and standard_deviation_value and sample_size_value and interval)):
        return None
    #do math
    error = float(standard_deviation_value)/math.sqrt(float(sample_size_value))
    #get the z star value
    z_star = interval_num_to_value[interval]
    #do more math
    new_interval = float(z_star) * error
    return {
        'sample_mean': sample_mean_value,
        'standard_deviation': standard_deviation_value,
        'interval': new_interval
    }

class graphing:
    def __init__(self):
        self.graph = None

    def reset_graph(self):
        if self.graph is None:
            return
        self.graph.destroy()
        # This is important for the if condition to work in update_graph
        self.graph = None
    def close_graph(self):
        if self.graph is None:
            return
        self.graph.destroy()
        # This is important for the if condition to work in update_graph
        self.graph = None

    def update_graph(self, result):
        if (self.graph is not None):
            graph.reset_graph()
        else:
            self.graph = tkinter.Toplevel()

        sample_mean_value = result.get('sample_mean')
        new_interval = result.get('interval')
        standard_deviation_value = result.get('standard_deviation')

        #graphing part
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        x = np.linspace(float(sample_mean_value) - 3 * float(standard_deviation_value), float(sample_mean_value) + 3 * float(standard_deviation_value), 10000)
        nVals = [norm.pdf(i,float(sample_mean_value),float(standard_deviation_value)) for i in x]
        ax.plot(x,nVals)
        x1 = float(sample_mean_value) - new_interval
        x2 = float(sample_mean_value) + new_interval
        ax.fill_between(x,nVals,color = '#111111',where = (x > x1) & (x < x2))

        canvas = FigureCanvasTkAgg(fig, master= self.graph)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, self.graph)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

graph = graphing()

def update_result_label(result):
    #setting string display
    string_to_display = "Confidence Interval: {sample_mean} \u00B1 {interval}".format(**result)
    confidence_interval_var.set(string_to_display)

def clear_result_label():
    confidence_interval_var.set("")

def handle_values_changed(*args):
    sample_mean = sample_mean_input.get()
    standard_deviation = standard_deviation_input.get()
    sample_size = sample_size_input.get()
    interval = interval_var.get()
    result = calculate_interval(sample_mean, standard_deviation, sample_size, interval)
    if (result is not None):
        update_result_label(result)
        graph.update_graph(result)
    else:
        clear_result_label()
        graph.close_graph()

#basic setup
root = tkinter.Tk()
root.title("Confidence Interval Calculator")

#variables used
confidence_interval_var = tkinter.StringVar()
interval_var= tkinter.IntVar()
interval_var.trace('w', handle_values_changed)

#frames to group stuff
frame_labels = tkinter.Frame(root) #sample mean, standard deviation, and sample size
frame_choice = tkinter.Frame(root) #confidence interval choices
frame_button = tkinter.Frame(root) #calculate button
frame_answer = tkinter.Frame(root) #answer

#entry for sample mean, standard deviation, and sample size (label + input)
sample_mean = tkinter.Label(frame_labels, text = 'Sample Mean',).grid(row = 0)
standard_deviation = tkinter.Label(frame_labels, text = 'Standard Deviation').grid(row=1)
sample_size = tkinter.Label(frame_labels, text = 'Sample Size').grid(row=2)
sample_mean_input_var = tkinter.StringVar()
sample_mean_input_var.trace('w', handle_values_changed)
sample_mean_input = tkinter.Entry(frame_labels, textvariable=sample_mean_input_var)
standard_deviation_input_var = tkinter.StringVar()
standard_deviation_input_var.trace('w', handle_values_changed)
standard_deviation_input = tkinter.Entry(frame_labels, textvariable=standard_deviation_input_var)
sample_size_input_var = tkinter.StringVar()
sample_size_input_var.trace('w', handle_values_changed)
sample_size_input = tkinter.Entry(frame_labels, textvariable=sample_size_input_var)

#confidence interval choices between 80-99.9%
interval_1 = tkinter.Radiobutton(frame_choice, text = "80%", value = 1, variable = interval_var)
interval_2 = tkinter.Radiobutton(frame_choice, text = "85%", value = 2, variable = interval_var)
interval_3 = tkinter.Radiobutton(frame_choice, text = "90%", value = 3, variable = interval_var)
interval_4 = tkinter.Radiobutton(frame_choice, text = "95%", value = 4, variable = interval_var)
interval_5 = tkinter.Radiobutton(frame_choice, text = "99%", value = 5, variable = interval_var)
interval_6 = tkinter.Radiobutton(frame_choice, text = "99.5%", value = 6, variable = interval_var)
interval_7 = tkinter.Radiobutton(frame_choice, text = "99.9%", value = 7, variable = interval_var)

#The confidence interval is....
answer = tkinter.Label(frame_answer, textvariable = confidence_interval_var)

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

#answer orientation
answer.grid(row=4)

#frame orientation
frame_labels.grid(column = 0, row = 0)
frame_choice.grid(column = 0, row = 1)
frame_button.grid(column = 0, row = 2)
frame_answer.grid(column = 0, row = 3)

root.mainloop()
