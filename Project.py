from tkinter import *
from PIL import Image, ImageTk
import time
import json

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
    stock = 1
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="black")
        self.setupGUI()
        

    # the setup
    def setupGUI(self):
        self.Level1()
        # BackGround in progress
        # Mason's file
        bg = PhotoImage(file = "Project Buttons/La_tech.gif")
        # Reese's file
        #bg = PhotoImage(file = "C:/Users/reese/OneDrive/Desktop/mygitfolder/La_tech.gif")
        self.label= Label(self, image=bg)
        self.label.image = bg
        self.label.place(x=0,y=0,relheight=1, relwidth=1)
        self.pack(fill=BOTH, expand=1)
        # variable for assigning the image

        # Mason's file
        img = PhotoImage(file = "Project Buttons/dew.gif")
        # Reese's file
        #img = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/dew.gif")
        # the setup for the button itself, assigning the image on top of it
        self.button = Button(self, bg="white", image=img,borderwidth=0, command=lambda: self.StockPage())
        self.button.image = img
        # shove it in a cell
        self.button.place(x=300, y=200)                                       # Change to fix RPI display

        # Mason's file
        Simg = PhotoImage(file = "Project Buttons/SettingIcon.png")
        # Reese's file
        #Simg = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/SettingIcon.png")
        self.SettingIcon = Button(self, image=Simg, borderwidth=0,command=lambda: self.SettingsPage())
        self.SettingIcon.image = Simg
        self.SettingIcon.place(x=0, y=0)
        
        # Mason's file
        InfoButtonPicture = PhotoImage(file="Project Buttons/Info_Button.png")
        # Reese's file
        #InfoButtonPicture = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/info_Button.png")
        self.InfoButton = Button(self, image=InfoButtonPicture, borderwidth=0,command=lambda: self.InfoPage())
        self.InfoButton.image = InfoButtonPicture
        self.InfoButton.place(x=0, y=600, relheight=0.2, relwidth=0.2)
        # Mason's file
        Chart = PhotoImage(file="Project Buttons/chart.png")
        # Reese's file
        #Chart = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/Chart.png")
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
        # Mason's file
        textimg = PhotoImage(file="Project Buttons/Info_Tech.png")
        # Reese's file
        #textimg = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/Info_Tech.png")
        self.Text = Label(self, image= textimg, borderwidth=0)
        self.Text.image = textimg
        self.Text.place(x=0, y=0, relheight=1, relwidth=1)
        
        


    # Controls the Chart page after you click the chart button
    def ChartPage(self):
        # Cleans the Board
        self.Level1()
        # packs the background image
        # Mason's file 
        img = PhotoImage(file="Put your file path here")
        # Reese's File
        #img = PhotoImage(file="C:/Users/reese/OneDrive/Desktop/mygitfolder/Chart_page.png")
        self.label1 = Label(self, image=img)
        self.label1.image = img
        self.label1.place(x=0, y=0, relheight=1, relwidth=1)

        # Re intializes the Back Button
        self.BackButton = Button(self, text = "Go Back", command= lambda: self.change())
        self.BackButton.place(x= 100, y=100)
        if (self.stock > 0):
            print(self.stock)
            self.Block = Label(self, bg="cyan", borderwidth=0)
            self.Block.place(x = 300, y =417, relwidth=0.2, relheight=0.2)
            if (self.stock>1):
                self.Block1 = Label(self, bg="cyan", borderwidth=0)
                self.Block1.place(x = 300, y =260, relwidth=0.2, relheight=0.2)
    def change(self):
        self.stock = 2
        data = open(data_Open_Location, "w")
        info = {"Stock": self.stock, "bean":8}
        data.write(str(info))
        data.close()
        print(self.stock)
        self.Level1
        self.ChartPage()


    
    # This function creates the settings page. 
    # It clears the screen of all vending options and displays the options menu.
    # To enter the settings menu, an prompt will pop up asking for a password. Correct password results in entering options, while failed denies access.
    def SettingsPage(self):
        # Clears all vending options
        self.Level1()
        # The contents of the options menu (WIP)
        # the back button
        self.label.pack(fill=BOTH, expand=1)
        self.BackButton = Button(self, text="go back", command=lambda: self.setupGUI() )
        self.BackButton.place(x=100, y=350)

        # a label asking for a password
        self.passlabel = Label(self, text="Enter password", font=("Arial", 25))
        self.passlabel.place(x=250, y=200)

        # entry space for password
        # password is "admin"
        # this can be changed in the main code
        self.passwordEntry = Label(width=35,font=("Arial", 20))
        self.passwordEntry.place(x=100, y=300)

        # the confirm button
        # when clicked, determines if the entered password is correct or incorrect
        self.confirm = Button(self, text="Confirm", font=("Arial", 10), command =lambda: self.PassConfirm() )
        self.confirm.place(x=600, y=350)

        # the key pad
        # 7
        self.seven = Button(self,text="7",font=("Arial", 20), command = lambda:self.process("7"))
        self.seven.place(x=350, y=500)

        # 8
        self.eight = Button(self,text="8",font=("Arial", 20), command = lambda:self.process("8"))
        self.eight.place(x=300,y=500)

        # 9
        self.nine = Button(self,text="9",font=("Arial", 20), command = lambda:self.process("9"))
        self.nine.place(x=250,y=500)

        # Back
        self.back = Button(self,text="Back",font=("Arial", 20), command = lambda:self.process("Back"))
        self.back.place(x=400, y=500)


        # 4
        self.four = Button(self,text="4",font=("Arial", 20), command = lambda:self.process("4"))
        self.four.place(x=350,y=550)

        # 5
        self.five = Button(self,text="8",font=("Arial", 20), command = lambda:self.process("5"))
        self.five.place(x=300,y=550)

        # 6
        self.six = Button(self,text="6",font=("Arial", 20), command = lambda:self.process("6"))
        self.six.place(x=250,y=550)

        # 1
        self.one = Button(self,text="1",font=("Arial", 20), command = lambda:self.process("1"))
        self.one.place(x=350,y=600)

        # 2
        self.two = Button(self,text="2",font=("Arial", 20), command = lambda:self.process("2"))
        self.two.place(x=300,y=600)

        # 3
        self.three = Button(self,text="3",font=("Arial", 20), command = lambda:self.process("3"))
        self.three.place(x=250,y=600)

        # 0
        self.zero = Button(self,text="0",font=("Arial", 20), command=lambda:self.process("0"))
        self.zero.place(x=300, y=650)


        self.pack(fill=BOTH, expand=1)

    # function for processing what was input
    def process(self, buttonName):
        if(buttonName == "Back"):
            try:
                # lower the nums list by one
                del pass_input[-1]
                del pass_conceal[-1]
                # convert the integers in the nums list to a string
                strings = [str(integer) for integer in pass_input]
                # remove the spaces when displaying the list
                a_string = "".join(strings)
                c_string = "".join(pass_conceal)
                # if all numbers are deleted...
                if (len(pass_input) == 0):
                    # make the screen clear
                    self.passwordEntry["text"] = ""
                # otherwise...
                else:
                    # display the concealed password list with no spaces
                    conNoSpaces = c_string
                    self.passwordEntry["text"] = conNoSpaces
            except:
                self.passwordEntry["text"] = ""
                pass_input.clear()
        
        else:
            # add the button pressed to the nums list
            pass_input.append(buttonName)
            pass_conceal.append("*")
            # display * when presses to conceal the password
            self.passwordEntry["text"] += "*"
            
    
    # function for the confirm button to determine if the entered password is correct or not
    def PassConfirm(self):
        global pass_list
        counter = 0
        # puts each individual letter of the entered password into a list
        # this is used to make it easier when checking if the entered password is the same as the set password
        pass_list = pass_input
        try:
            for i in range(len(pass_list)):
                if pass_list[i] == password[i]:
                    counter += 1
                else:
                    self.PassFail()
                    counter = 0
            
            # this is 100% confirmation that the entered password matches the set password
            if counter == len(password):
                self.SettingsPage2()
            # displays that the entered password is false
            else:
                self.PassFail()
                counter = 0
        except:
            self.PassFail()
            

    # the next screen for the admin
    def SettingsPage2(self):
        print("Im in")

    # displays the entered password is incorrect
    # destroys itself after 3 seconds
    def PassFail(self):
            pass_input.clear()
            self.passwordEntry["text"] = ""
            incorrect = Label(text="Incorrect password. Try again")
            incorrect.place(x=100, y=320)
            incorrect.after(3000, lambda: incorrect.destroy())


        
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
        try:
            self.confirm.destroy()
            self.passwordEntry.destroy()
            self.passlabel.destroy()
        except:
            pass
        try:
            self.Block.destroy()
            self.label1.destroy()
            self.Block1.destroy()
        except:
            pass

    # Controls the Animation on the Stock page of the Mountain Dew
    def Mountaindew(self):
        # Mason's file
        img = Image.open(r"Project Buttons/dewspin.gif")
        # Reese's file
        #img = Image.open(r"C:/Users/reese/OneDrive/Desktop/mygitfolder/dew.gif")
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
# this REQUIRES the list() function
# changing this will mean changing the code of the SettingsPage() function
password = ("0","0","0","0")
pass_input = []
pass_conceal = []
# set up for json file which is connected to google drive
# download google drive for desktop and put the file path to the file "label.json" 
# Reese's json file
#data_Open_Location = "G:/My Drive/Project/label.json"
#startingdata = open(data_Open_Location, "w")
#StartingInfo = {"Stock": 1, "bean":5}
#startingdata.write(str(StartingInfo))
#startingdata.close()



window = Tk()
window.geometry("{}x{}".format(800, 800))
s = Screen(window)
s.mainloop()
