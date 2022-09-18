# import all classes / functions from the tkinter
from tkinter import *
from wsgiref import headers
from sympy import O
from tabulate import tabulate
from tkinter import ttk
from sqlalchemy import intersect
from tabulate import tabulate

# Function for clearing the
# contents of all entry boxes


def clear_all():

    # whole content of entry boxes is deleted
    principle_field.delete(0, END)
    rate_field.delete(0, END)
    time_field.delete(0, END)
    compound_field.delete(0, END)

    # set focus on the principle_field entry box
    principle_field.focus_set()


# Function to find compound interest
def calculate_ci():

    # get a content from entry box
    principle = int(principle_field.get())

    rate = float(rate_field.get())

    time = int(time_field.get())

    # Calculates compound interest
    CI = principle * (pow((1 + rate / 100), time))

    # insert method inserting the
    # value in the text entry box.
    compound_field.insert(10, CI)


def get_report():

    # Create a GUI window
    #    root = Tk()
    # Set the background colour of GUI window
    #    root.configure(background = 'light green')
    # Set the configuration of GUI window
    #    root.geometry("500x400")
    # set the name of tkinter GUI window
    #    root.title("Report")

    # get a content from entry box
    principle = int(principle_field.get())
    rate = float(rate_field.get())
    time = int(time_field.get())

    ws = Tk()
    ws.title('Report')
    ws.geometry('500x500')
    ws['bg'] = '#AC99F2'

    game_frame = Frame(ws)
    game_frame.pack()

    my_game = ttk.Treeview(game_frame)

    my_game['columns'] = ('Year', 'Principle', 'Interest')

    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("Year", anchor=CENTER, width=80)
    my_game.column("Principle", anchor=CENTER, width=80)
    my_game.column("Interest", anchor=CENTER, width=80)

    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("Year", text="Year", anchor=CENTER)
    my_game.heading("Principle", text="Principle", anchor=CENTER)
    my_game.heading("Interest", text="Interest", anchor=CENTER)

    table = {'Year': [], 'Principle': [], 'Interest': []}
    headers = ['Year', 'Principle', 'Interest']

    for x in range(0, time):
        CI = principle * (pow((1 + rate / 100), x))
        interest_amt = CI - principle
        interest_amt = round(interest_amt)
        n_principle = principle + interest_amt
        n_principle = round(n_principle)
        table['Year'].append(x)
        table['Principle'].append(CI)
        table['Interest'].append(interest_amt)
        my_game.insert(parent='', index='end', iid=x, text='',
                       values=(x, n_principle, interest_amt))
    # print(x)
    # print(CI)
    # print(table['Year'])
    # print(table['Principle'])

    #print(tabulate(table, headers=headers, tablefmt= 'pretty'))

    my_game.pack()
    ws.mainloop()


############################################################################################################
# Driver code
if __name__ == "__main__":

    # Create a GUI window
    root = Tk()

    # Set the background colour of GUI window
    root.configure(background='light green')

    # Set the configuration of GUI window
    root.geometry("500x400")

    # set the name of tkinter GUI window
    root.title("Compound Interest Calculator")

    # Create a Principle Amount : label
    label1 = Label(root, text="Principle Amount(Rs) : ",
                   fg='black')  # , bg = 'red')

    # Create a Rate : label
    label2 = Label(root, text="Rate(%) : ",
                   fg='black')  # , bg = 'red')

    # Create a Time : label
    label3 = Label(root, text="Time(years) : ",
                   fg='black')  # , bg = 'red')

    # Create a Compound Interest : label
    label4 = Label(root, text="Compound Interest : ",
                   fg='black')  # , bg = 'red')

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .

    # padx keyword argument used to set padding along x-axis .
    # pady keyword argument used to set padding along y-axis .
    label1.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=2, column=0, padx=10, pady=10)
    label3.grid(row=3, column=0, padx=10, pady=10)
    label4.grid(row=5, column=0, padx=10, pady=10)

    # Create a entry box
    # for filling or typing the information.
    principle_field = Entry(root)
    rate_field = Entry(root)
    time_field = Entry(root)
    compound_field = Entry(root)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .

    # padx keyword argument used to set padding along x-axis .
    # pady keyword argument used to set padding along y-axis .
    principle_field.grid(row=1, column=1, padx=10, pady=10)
    rate_field.grid(row=2, column=1, padx=10, pady=10)
    time_field.grid(row=3, column=1, padx=10, pady=10)
    compound_field.grid(row=5, column=1, padx=10, pady=10)

    # Create a Submit Button and attached
    # to calculate_ci function
button1 = Button(root, text="Submit", bg="red",
                 fg="black", command=calculate_ci)

# Create a Clear Button and attached
# to clear_all function
button2 = Button(root, text="Clear", bg="red",
                 fg="black", command=clear_all)

# Generate a report
button3 = Button(root, text="Generate Report", bg="red",
                 fg="black", command=get_report)


button1.grid(row=4, column=1, pady=10)
button2.grid(row=6, column=1, pady=10)
button3.grid(row=8, column=1, pady=10)

# Start the GUI
root.mainloop()
