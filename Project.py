from tkinter import *
from PIL import Image, ImageTk

#git add
#git commit -m"comment"
#git push

# DATA_FILE_LOCATION = "C:/users/google drive/machine_data.json"

# file = open(DATA_FILE_LOCATION, "r")

# file = open(DATA_FILE_LOCATION, "w")

# data.read()
# data = {
#     "machine_1": 
#             {
#                 "mountain": 
#                 {
#                     "amount": 5, 
#                     "sold":4
#                 },
#                 "drpepper":
#                 {
#                     "amount": 5,
#                     "sold": 4,
#                     "price": 1.5
#                 } 
#             }
#         }

# data["machine_1"]["mountain"]["sold"] = 4


# read data
    # open json file
    # read data
    # close json file

# write data
    # open json file
    # write data
    # close json file
    # read data

# class for the screen
class Screen(Frame):
    
    
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="black")
        self.setupGUI()
        

    # the setup
    def setupGUI(self):
        self.Level1()
        # BackGround in progress
        # Mason's file
        #bg = PhotoImage(file = "C:/Users/angry/Desktop/csc132/Project Buttons/La_tech.gif")
        # Reese's file
        bg = PhotoImage(file = "C:/Users/reese/OneDrive/Desktop/mygitfolder/La_tech.gif")
        self.label= Label(self, image=bg)
        self.label.image = bg
        self.label.place(x=0,y=0,relheight=1, relwidth=1)
        self.pack(fill=BOTH, expand=1)
        # variable for assigning the image

        # Mason's file
        #img = PhotoImage(file = "C:/Users/angry/Desktop/csc132/Project Buttons/dew.gif")
        # Reese's file
        img = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/dew.gif")
        # the setup for the button itself, assigning the image on top of it
        self.button = Button(self, bg="white", image=img,borderwidth=0, command=lambda: self.StockPage())
        self.button.image = img
        # shove it in a cell
        self.button.place(x=300, y=200)                                       # Change to fix RPI display

        # Mason's file
        #Simg = PhotoImage(file="C:/Users/angry/Desktop/csc132/Project Buttons/SettingIcon.png")
        # Reese's file
        Simg = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/SettingIcon.png")
        self.SettingIcon = Button(self, image=Simg, borderwidth=0,command=lambda: self.SettingsPage())
        self.SettingIcon.image = Simg
        self.SettingIcon.place(x=0, y=0)
        
        # Mason's file
        #InfoButtonPicture = PhotoImage(file="C:/Users/angry/Desktop/csc132/Project Buttons/Info_Button.png")
        # Reese's file
        InfoButtonPicture = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/info_Button.png")
        self.InfoButton = Button(self, image=InfoButtonPicture, borderwidth=0,command=lambda: self.InfoPage())
        self.InfoButton.image = InfoButtonPicture
        self.InfoButton.place(x=0, y=600, relheight=0.2, relwidth=0.2)
        Chart = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/Chart.png")
        self.ChartButton = Button(self, image=Chart, borderwidth=0, command=lambda: self.ChartPage())
        self.ChartButton.image = Chart
        self.ChartButton.place(x=640, y=0, relheight=0.2, relwidth=0.2)
        


    # This function creates the info page. 
    # It clears the screen of all vending options and displays the info menu.
    def InfoPage(self):
        # Clears all vending options.
        self.Level1()
        # The contents of the info menu (WIP)
        self.BackButton = Button(self, text="Click here to go back", bg="white", command=lambda: self.setupGUI() )
        self.BackButton.place(x=350, y =100)
        textimg = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/Info_Tech.png")
        self.Text = Label(self, image= textimg, borderwidth=0)
        self.Text.image = textimg
        self.Text.place(x=0, y=0, relheight=1, relwidth=1)
        
        


    # Controls the Chart page after you click the chart button
    def ChartPage(self):
        # Cleans the Board
        self.Level1()
        # packs the background image
        self.label.pack(fill=BOTH, expand=1)
        # Re intializes the Back Button
        self.BackButton = Button(self, text = "Go Back", command= lambda: self.setupGUI())
        self.BackButton.place(x= 100, y=100)

    
    # This function creates the settings page. 
    # It clears the screen of all vending options and displays the options menu.
    # To enter the settings menu, an prompt will pop up asking for a password. Correct password results in entering options, while failed denies access.
    def SettingsPage(self):
        # Clears all vending options
        self.Level1()
        # The contents of the options menu (WIP)
        self.label.pack(fill=BOTH, expand=1)
        self.BackButton = Button(self, text="Click here to go back", bg="white", command=lambda: self.setupGUI() )
        self.BackButton.place(x=350, y =100)
        self.pack(fill=BOTH, expand=1)
        
    def StockPage(self):
        # Clears all vending options
        self.Level1()
        self.label.pack(fill=BOTH, expand=1)
        self.Mountaindew()

    # Clean up Function, Wipes the Screen
    def Level1(self):
        try:
            self.SettingIcon.destroy()
            self.InfoButton.destroy()
            self.button.destroy()
            self.label.forget()
        except:
            pass
        try:
            self.BackButton.destroy()
        except:
            pass
        try:
            self.ChartButton.destroy()
        except:
            pass
        try:
            self.label5.destroy()
        except:
            pass


    # Controls the Animation on the Stock page of the Mountain Dew
    def Mountaindew(self):
        img = Image.open(r"C:/Users/reese/OneDrive/Desktop/mygitfolder/dew.gif")
        framesTotal = img.n_frames

        play_back_delay = 30
        animation = []
        self.label5 = Label(self)
        def loadGif():
            for x in range(framesTotal):
                frame = ImageTk.PhotoImage(img.copy())
                animation.append(frame)
                img.seek(x)


        def update(ind):
            frame = animation[ind]
            self.label5.configure(image=frame)
    
            ind += 1
            if ind == framesTotal:
                ind = 0

            self.after(play_back_delay, update, ind)
        # the setup for the button itself, assigning the image on top of it
        self.label5 = Label(self)
        self.label5.place(x=350, y = 300)
        loadGif()
        update(0)
        self.BackButton = Button(self, text="click here", command= lambda: self.setupGUI())
        self.BackButton.place(x=250, y=100)


############################# Main Function ########################################################################################################
window = Tk()
window.geometry("{}x{}".format(800, 800))
s = Screen(window)
s.mainloop()
