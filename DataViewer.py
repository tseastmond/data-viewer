'''
Author: Tanner S Eastmond
Date: 8/11/2018
Version: 1.0
Purpose: This class is a data viewer for Pandas DataFrames that allows the user
    to view, filter, and calculate summary statistics for each column.
'''
import pandas as pd
from tkinter import *

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
        self.root = Tk()

        # Get the columns and widths
        self.cols = list(self.df.columns)
        self.colwidth = [0]*len(self.cols)

        # Set the scaling factors and height of the base frame and the text box parameters.
        self.min_height = 200 #self.root.winfo_screenheight() - 50
        self.min_width = 200 #self.root.winfo_screenwidth()
        self.before_space = 1
        self.hspace = 1.3
        self.rows = 100

        # Run the window settings.
        self.Window()

        # Make the menu bar.
        self.TopMenu()

        # Make the scroll bar.
        self.Scroll()

        # Display the data.
        self.DataView()

        # Loop for the tkinter window.
        while True:
            self.root.update_idletasks()
            self.root.update()
        #self.root.mainloop()

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
        menubar = Menu()

        # Create a pulldown filter menu, and add it to the menu bar.
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Test', command=self.Hello)
        menubar.add_cascade(label='Filter', menu=filemenu)

        # Create the settings menu.
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_separator()
        editmenu.add_command(label='Exit', command=self.root.quit)
        menubar.add_cascade(label='Settings', menu=editmenu)

        # Create the help menu.
        helpmenu = Menu(menubar, tearoff=0)
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
            self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        else:
            self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def Scroll(self):
        '''
        Set up the scroll bar.
        '''
        # Define the new frame.
        myframe = Frame(bd=1, relief=SUNKEN)
        myframe.pack(fill=BOTH, padx=5, pady=5, expand=TRUE)

        # Set up the canvas for the scroll bar.
        self.canvas = Canvas(myframe)
        self.frame = Frame(self.canvas)

        # Get a vertical scroll bar.
        self.orient = 'vertical'
        myscrollbar = Scrollbar(myframe, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side='right',fill='y')
        self.canvas.pack(side='left', fill='both', expand='yes')
        self.canvas.create_window((0,0),window=self.frame,anchor='nw')
        self.frame.bind("<Configure>", self.ScrollHelp)

        # Get a horizontal scroll bar.
        self.orient = 'horizontal'
        myscrollbar1 = Scrollbar(myframe, orient='horizontal', command=self.canvas.xview)
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

            # Define the box and set the options.
            text1 = Text(self.frame)
            text1.tag_configure('center', justify='center', spacing1=self.before_space)
            text1.insert(INSERT, x)
            text1.config(font=('Times', 12, 'bold'), width=self.colwidth[num], height=self.hspace, wrap=NONE, state=DISABLED)
            text1.tag_add('center', '1.0', 'end')
            text1.grid(row=0, column=num, sticky=E+W)

        # We will default to only seeing the first 100 rows, the user can get more.
        if len(self.df) >= self.rows:
            view = self.rows
        else:
            view = len(self.df)

        for num, x in enumerate(self.cols):
            for y in range(view):
                # Get nan values right.
                if pd.isnull(self.df[x].iloc[y]):
                    var = 'nan'
                else:
                    var = self.df[x].iloc[y]

                # Define the box and set the options.
                text2 = Text(self.frame)
                text2.tag_configure('center', justify='left', spacing1=self.before_space)
                text2.insert(INSERT, var)
                text2.config(font=('Times', 12), width=self.colwidth[num], height=self.hspace, wrap=NONE, state=DISABLED)
                text2.tag_add('center', '1.0', 'end')
                text2.grid(row=y+1, column=num, sticky=E+W)


df = pd.read_csv(r'C:\Users\tanne\OneDrive\Python\stocks\data\batch4.csv', encoding='latin')
#df = df[df.columns[0:1]]
df['ones'] = 1
df['test_col'] = 'Tanner Scott Eastmond'
DataViewer(df)
