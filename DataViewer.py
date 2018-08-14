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
        self.df = df.reset_index()
        self.root = tk.Tk()

        # Get the columns and widths
        self.cols = list(self.df.columns)
        self.colwidth = [0]*len(self.cols)

        # Set the scaling factors and height of the base frame.
        self.min_height = 600 #self.root.winfo_screenheight() - 50
        self.min_width = 400 #self.root.winfo_screenwidth()

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
        self.root.minsize(width=self.min_width, height=self.min_height)

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

    def ScrollHelp(self, event):
        '''
        Configure the scroll bar.
        '''
        # Size the canvas and the scroll bar.
        if self.orient == 'vertical':
            self.canvas.configure(scrollregion=self.canvas.bbox('all'), width=min(self.min_width-23, self.canvas.bbox('all')[2]), height=self.min_height-23)
        else:
            self.canvas.configure(scrollregion=self.canvas.bbox('all'), width=min(self.min_width-23, self.canvas.bbox('all')[2]), height=self.min_height-23)

    def Scroll(self):
        '''
        Set up the scroll bar.
        '''
        # Define the new frame.
        myframe = tk.Frame(self.root, relief='groove', width=58, height=200, bd=1)
        myframe.place(x=0, y=0)
        myframe.grid(row=0, column=0, sticky='ewns')

        # Set up the canvas for the scroll bar.
        self.canvas = tk.Canvas(myframe)
        self.frame = tk.Frame(self.canvas)
        self.frame.grid(row=0, column=0, sticky='ewns')

        # Get a vertical scroll bar.
        self.orient = 'vertical'
        myscrollbar = tk.Scrollbar(myframe, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side='right',fill='y')
        self.canvas.pack(side='left', fill='both', expand='yes')
        self.canvas.create_window((0,0),window=self.frame,anchor='nw')
        self.frame.bind("<Configure>", self.ScrollHelp)

        # Get a horizontal scroll bar.
        self.orient = 'horizontal'
        myscrollbar1 = tk.Scrollbar(myframe, orient='horizontal', command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=myscrollbar1.set)

        myscrollbar1.pack(side='bottom',fill='x')
        self.canvas.pack(side='top', fill='both', expand='yes')
        self.canvas.create_window((0,0),window=self.frame,anchor='nw')
        self.frame.bind("<Configure>", self.ScrollHelp)
        
    def DataView(self):
        '''
        Set up the view for the data itself.
        '''
        # Make headers.
        for num, x in enumerate(self.cols):
            # Keep the column width, which will be twice the length of the label or the minimum of 50 and the longest string.
            self.colwidth[num] = max(len(x)*2, min(50, self.df[x].astype(str).str.len().max()))

            # Define a tkinter string variable.
            var = tk.StringVar()
            var.set(x)

            # Make the cell.
            b = tk.Entry(self.frame, textvar=var, justify='center', bd=1,
                font=("Times", 10, "bold"), disabledbackground='white',
                disabledforeground='black', width=self.colwidth[num])
            b.grid(row=0, column=num)

            # Disable the text.
            b.config(state='readonly')

        # We will default to only seeing the first 100 rows, the user can get more.
        if len(self.df) >= 100:
            view = 100
        else:
            view = len(self.df)

        for num, x in enumerate(self.cols):
            for y in range(view):
                # Set up the tkinter string variable.
                var = tk.StringVar()

                # Get nan values right.
                if pd.isnull(self.df[x].iloc[y]):
                    var.set('nan')
                else:
                    var.set(self.df[x].iloc[y])

                # Set the right column.
                text = tk.Entry(self.frame, textvar=var, justify='center', bd=1,
                    font=("Times", 11), disabledbackground='white',
                    disabledforeground='black', width=self.colwidth[num])
                text.grid(row=y+1, column=num)

                # Disable the text.
                text.configure(state='readonly')

        # Reset the size of our canvas.
        # print(self.colwidth, sum(self.colwidth)+20)
        #self.canvas.configure(width=sum(self.colwidth)+20, height=200)


df = pd.read_csv(r'C:\Users\tanne\OneDrive\Python\stocks\data\batch4.csv', encoding='latin')
df['ones'] = 1
df['test_col'] = 'Tanner Scott Eastmond'
DataViewer(df)
