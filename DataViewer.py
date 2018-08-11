'''
Author: Tanner S Eastmond
Date: 8/11/2018
Version: 1.0
Purpose: This class is a data viewer for Pandas DataFrames that allows the user
    to view, filter, and calculate summary statistics for each column.
'''

import pandas as pd
import tkinter as tk

class DataViewer:
    '''
    This class is a data viewer for Pandas DataFrames that allows the user
    to view, filter, and calculate summary statistics for each column.

    Parameters
    ----------
    df  - A Pandas DataFrame object.
    '''

    def __init__(self, df):
        # Get the DataFrame and the base widget.
        self.df = df
        self.root = tk.Tk()

        # Run the window settings.
        self.Window()

        # Make the menu bar.
        self.TopMenu()

        # Make the scroll bar.
        self.Scroll()

        # Display the data.
        self.DataView()

        # Loop for the tkinter window.
        self.root.mainloop()

    def Window(self):
        '''
        Pull up the window and change settings there.
        '''
        # Define the title.
        self.root.title('Panda\'s DataFrame Viewer')

        # Set the minimum size.
        self.root.minsize(width=600, height=400)

        # Set the colors.
        self.root.configure(background='black')

    def TopMenu(self):
        '''
        Set up the top menu with settings and filters.
        '''
        # Initialize the menu.
        menubar = tk.Menu()

        # Create a pulldown filter menu, and add it to the menu bar.
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Test', command=self.Hello)
        menubar.add_cascade(label='Filter', menu=filemenu)

        # Create the settings menu.
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_separator()
        editmenu.add_command(label='Exit', command=self.root.quit)
        menubar.add_cascade(label='Settings', menu=editmenu)

        # Create the help menu.
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label='About', command=self.Hello)
        menubar.add_cascade(label='Help', menu=helpmenu)

        # Display the menu.
        self.root.config(menu=menubar)

    def Hello(self):
        print('Hello')

    def Scroll(self):
        '''
        Set up the scroll bar.
        '''
        # Initialize the scroll bar.
        scrollbar = tk.Scrollbar(self.root, orient='vertical')
        scrollbar.grid(column=len(self.df.columns), rowspan=100, sticky='ns')

    def DataView(self):
        '''
        Set up the view for the data itself.
        '''
        # Get the columns.
        cols = list(self.df.columns)
        colwidth = [0]*len(cols)

        # Make headers.
        for num, x in enumerate(cols):
            # Keep the column width.
            colwidth[num] = len(x)*2

            # Define a tkinter string variable.
            var = tk.StringVar()
            var.set(x)

            # Make the cell.
            b = tk.Entry(self.root, textvar=var, justify='center', bd=3,
                font=("Times", 10, "bold"), disabledbackground='white',
                disabledforeground='black', width=colwidth[num])
            b.grid(row=0, column=num)

            # Disable the text.
            b.config(state='readonly')

        # We will default to only seeing the first 100 rows, the user can get more.
        if len(self.df) >= 100:
            view = 100
        else:
            view = len(df)

        for num, x in enumerate(cols):
            for y in range(view):
                # Set up the tkinter string variable.
                var = tk.StringVar()

                # Get nan values right.
                if pd.isnull(self.df[x].iloc[y]):
                    var.set('nan')
                else:
                    var.set(self.df[x].iloc[y])

                # Set the right column.
                text = tk.Entry(self.root, textvar=var, justify='center', bd=3,
                    font=("Times", 11), disabledbackground='white',
                    disabledforeground='black', width=colwidth[num])
                text.grid(row=y+1, column=num)

                # Disable the text.
                text.configure(state='readonly')


df = pd.read_csv(r'C:\Users\tanne\OneDrive\Python\stocks\data\batch1.csv', encoding='latin')
df['ones'] = 1
DataViewer(df)
