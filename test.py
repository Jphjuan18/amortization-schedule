from tkinter import *
from tkinter import ttk
from sqlalchemy import intersect
from sympy import O
from tabulate import tabulate 
 
ws  = Tk()
ws.title('Report')
ws.geometry('500x500')
ws['bg'] = '#AC99F2'

game_frame = Frame(ws)
game_frame.pack()

my_game = ttk.Treeview(game_frame)

my_game['columns'] = ('Year', 'Principle', 'Interest')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("Year",anchor=CENTER, width=80)
my_game.column("Principle",anchor=CENTER,width=80)
my_game.column("Interest",anchor=CENTER,width=80)

my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("Year",text="Year",anchor=CENTER)
my_game.heading("Principle",text="Principle",anchor=CENTER)
my_game.heading("Interest",text="Interest",anchor=CENTER)

#my_game.insert(parent='',index='end',iid=0,text='',
#values=('1','Ninja'))
#my_game.insert(parent='',index='end',iid=1,text='',
#values=('2','Ranger'))

 
principle = 10000
rate = 2
time = 5
   
#table = [["Year",0,1],["Principle",10000,10200],
  

table = {'Year': [], 'Principle':[], 'Interest':[]}
headers = ['Year', 'Principle', 'Interest']


#print(time)
for x in range(0,time):
    CI = principle * (pow((1 + rate / 100), x))   
    interest_amt = CI - principle
    interest_amt = round(interest_amt)
    n_principle = principle + interest_amt 
    n_principle = round(n_principle)
    table['Year'].append(x)
    table['Principle'].append(CI)
    table['Interest'].append(interest_amt)
    my_game.insert(parent='',index='end',iid=x,text='',
    values=(x,n_principle,interest_amt))
    # print(x)
    # print(CI)
    # print(table['Year'])
    # print(table['Principle'])
  

print(tabulate(table, headers=headers, tablefmt= 'pretty'))

my_game.pack()
ws.mainloop()