#----------------------------------------------------------------------------------------------------------------------------------
#Gilbert I. Guzman -- K-12 Engineering Outreach.
#score.py -- Scoreboard for West Texas FIRST® LEGO® League Challenge Championship.
#El Paso, TX -- January 11th, 2025. 
#----------------------------------------------------------------------------------------------------------------------------------
#Import Warnings: Allows Hiding of Warning Messages.
import warnings
#Import Openpyxl: Allows Reading/Writing to Excel Files.
import openpyxl
#Import pandas: Allows Data Manipulation & Analysis.
import pandas as pd
#Import tk from tkinter, Allows Creation of GUIs.
import tkinter as tk
#Import ttk from tkinter, Allows The use of Themed Widgets.
from tkinter import ttk
#Import PhotoImage from tkinter, Allows use of images in the GUI.
from tkinter import PhotoImage
#----------------------------------------------------------------------------------------------------------------------------------
#Hide User Warnings for depricated library.
warnings.simplefilter("ignore", UserWarning, append=True)

#readExcel: Reads the excel file, where all the computations are already coded. We just read and display.
def readExcel():
    #Path to the excel file we are using for scoring. 
    filePath = "fll-challenge-submerged-robot-game-excel-scorer.xlsm"
    #Read the "Score Entry & Standings" Excel Sheet, which is stored in the file as the 3rd sheet. 
    df = pd.read_excel(filePath, sheet_name=2)

    #*****Number of Participants*****
    #The code will get from where the calculations start (4) until the end. 
    #Our tournament has 40 participants, so we use the range. [4:44].
        #IF YOU NEED MORE, E.G. 50 Participants, adjust accordingly. [4:54].
        #DO NOT EDIT THE 16, 19, 20, ETC.
    #********************************

    #Get the RANK column.
    rankCol = df.iloc[4:44, 16]
    #Get the TEAM column.
    teamCol = df.iloc[4:44, 19]
    #Get the HIGHEST column.
    highestCol = df.iloc[4:44, 20]
    #Get the SECOND BEST column.
    secondBestCol = df.iloc[4:44, 21]
    #Get the LOWEST column.
    lowestCol = df.iloc[4:44, 22]

    #Create a new DataFrame that contains all of the data we took from the excel sheet. 
    formattedDataFrame = pd.DataFrame({
        'RANK': rankCol.values,
        'TEAM': teamCol.values,
        'highest': highestCol.values,
        '2nd best': secondBestCol.values,
        'lowest': lowestCol.values
    })
    #return the final formatted data frame.
    return formattedDataFrame

#updateDisplay: Allows the display to refresh with new data. 
def updateDisplay():
    #Read the excel file. 
    df = readExcel()
    #For (i), Clear the existing rows so we can update. 
    for i in tree.get_children():
        tree.delete(i)
    #For (index), get the row and insert the data into it for the appropriate one. 
    for index, row in df.iterrows():
        #Also assign the even and odd tags so the colors are correct. 
        tree.insert("", "end", values=(row['RANK'], row['TEAM'], row['highest'], row['2nd best'], row['lowest']), tags=('even' if index % 2 == 0 else 'odd',))
    #Apply the row styles (Aka the colors) for all the rows.
    applyRowStyles()
    #Refresh all the values on the display every 5 seconds. 
    root.after(5000, updateDisplay)

#applyRowStyles: Allows for the applying of the top 3 colors and the orange and white colors to the rows.
def applyRowStyles():
    #Apply orange and white row colors. 
    tree.tag_configure('even', background='white')
    tree.tag_configure('odd', background='darkorange')

    #Get all indexes, from tree.
    for i, item in enumerate(tree.get_children()):
        #Use modulus to get even and odds.
        if i % 2 == 0:
            tree.item(item, tags=('even',))
        else:
            tree.item(item, tags=('odd',))

    #Apply gold, yellow, and lightyellow colors for top 3.
    tree.tag_configure('first', background='gold') 
    tree.tag_configure('second', background='yellow') 
    tree.tag_configure('third', background='lightyellow')

    #Apply the top 3 places tag colors.
    for item in tree.get_children():
        rank = tree.item(item, 'values')[0] 
        if rank == '1st': 
            tree.item(item, tags=('first',)) 
        elif rank == '2nd': 
            tree.item(item, tags=('second',)) 
        elif rank == '3rd': 
            tree.item(item, tags=('third',))

#autoScroll: Allows for automatic scrolling of leaderboard to the bottom. 
def autoScroll():
    #Scroll down only 1 row at a time.
    tree.yview_scroll(1, "units")
    #if end is reached, reset to the bottom and autoscroll again.
    if tree.yview()[1] == 1.0:
        root.after(3000, resetScroll)
    else:
        root.after(1000, autoScroll)

#resetScroll: Allows for the reseting of the scroll to the top.
def resetScroll():
    #reset tags to default for all rows, removes colors so we can reassign.
    for item in tree.get_children():
        tree.item(item, tags=('default',))
    #Move view of tree to start.
    tree.yview_moveto(0)
    #Apply the row styles with new information.
    applyRowStyles()
    #After 3 seconds, scroll again. 
    root.after(3000, autoScroll)

#Create the GUI Window, name it the correct name.
root = tk.Tk()
root.title("FIRST® LEGO® League Challenge Standings")

#Create an outerframe, just a normal border so the scoreboard can sit in.
outerFrame = ttk.Frame(root)
outerFrame.pack(pady=20, fill='both', expand=True)

#Create a imageFrame for the images, it just holds the UTEP® and First® Logo.
imageFrame = ttk.Frame(outerFrame)
imageFrame.pack()

#*****EDIT FOR DIFFERENT EVENTS*****
#Add the first image, which is for the school. 
#Place a .png you want to into the folder and then rename it to match here.
logo1 = PhotoImage(file="UTEP_Flat_Logo_Orange.png")
#Place logo. 
logo_label1 = ttk.Label(imageFrame, image=logo1)
logo_label1.pack(side='left', padx=10)
#***********************************

#Add the second image, which is for the Program. 
logo2 = PhotoImage(file="fd_fll_submerged_challenge_social_template_tw_post_619278859.png")
#Place logo. 
logo_label2 = ttk.Label(imageFrame, image=logo2)
logo_label2.pack(side='left', padx=10)

#Condigure the tree styles, basically just text and size information, as well as the sizes for the rows.
style = ttk.Style()
style.configure("Treeview", font=("Helvetica", 25), rowheight=50)
style.configure("Treeview.Heading", font=("Helvetica", 25, "bold"))
style.map("Treeview", background=[('selected', 'lightgray')], foreground=[('selected', 'black')])
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

#Add border for the Treeview widget, which allows for better readability.
border_frame = ttk.Frame(outerFrame, borderwidth=1, relief='solid')
border_frame.pack(fill='both', expand=True, padx=10, pady=10)

#Name the top of the tree, basically these are the labels at the top of the scoreboard table.
tree = ttk.Treeview(border_frame, columns=("RANK", "TEAM", "highest", "2nd best", "lowest"), show='headings', style="Treeview")
tree.heading("RANK", text="RANK")
tree.heading("TEAM", text="TEAM")
tree.heading("highest", text="Highest")
tree.heading("2nd best", text="2nd Best")
tree.heading("lowest", text="Lowest")

#Make the individual columns, but theres no lines yet. 
for col in tree["columns"]:
    tree.column(col, anchor="center", stretch=tk.YES, width=200)
    tree.heading(col, anchor="center")
tree.pack(side="left", fill='both', expand=True)

#Create Canvas widget to draw all the vertical lines. (Need 4 for the 5 columns we have).
canvas = tk.Canvas(border_frame, width=tree.winfo_width(), height=tree.winfo_height(), background="black")
canvas.place(relx=0.2, rely=0, relheight=1, anchor='n')

canvas2 = tk.Canvas(border_frame, width=tree.winfo_width(), height=tree.winfo_height(), background="black")
canvas2.place(relx=0.4, rely=0, relheight=1, anchor='n')

canvas3 = tk.Canvas(border_frame, width=tree.winfo_width(), height=tree.winfo_height(), background="black")
canvas3.place(relx=0.6, rely=0, relheight=1, anchor='n')

canvas4 = tk.Canvas(border_frame, width=tree.winfo_width(), height=tree.winfo_height(), background="black")
canvas4.place(relx=0.8, rely=0, relheight=1, anchor='n')

#Show the direction to scroll down.
scroll_direction = "down"

#Set the icon at the top to the UTEP logo.
root.iconphoto(True, logo1)

#Automatically maximize the window.
root.state('zoomed')

#Automatically update the display and use autoscroll.
updateDisplay()
root.after(3000, autoScroll)

#Run the main loop, so it stays open until we kill the code. 
root.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------
#END OF CODE. 