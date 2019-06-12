"""
init.py
author: Colby Reyes
Date Created: 11JUN2019
%% file initializes the environment (variables, modules, and GUI) for inStructR app
%% modules used: pandas, tkinter, pillow/PIL, turtle
"""
from cImage import *
from cImage import filedialog
from PIL import *
from tkinter import *
from turtle import *
#import pandas as p

#x = p.DataFrame()
#print(x)

print("Hello")

# initialize GUI display framework



# initialize startup screen options
select = input("Select set of saved instructions from library? (Y/n) ")
s = select.upper()
if s[1] == "Y":
    print("Fetching inStructR library...")
    select_saved = True
else:
    print("Preparing to build a new set of instructions...")
    select_saved = False


# initialize instruction set to be displayed (default instructions if saved set is not chosen)
if select_saved == False:
    from dfltData import *
    
