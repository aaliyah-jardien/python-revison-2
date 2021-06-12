from datetime import date, timedelta
# from tkinter import *

# WINDOW FEATURES
# window = Tk()
# window.title("Calculate your age")
# window.geometry("500x500")
# window.config(bg="aqua")

dob = date(1996, 3, 13)
age = (date.today() - dob)//timedelta(days=365.245)
print(age)

# LABELS
# date = Label(window, text="Which day were you born?", command="")


# window.mainloop()
