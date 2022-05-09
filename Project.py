from tkinter import *
from PIL import Image, ImageTk
import time
import json
import RPi.GPIO as GPIO
from twilio.rest import Client

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

# set up for json file which is connected to google drive
# download google drive for desktop and put the file path to the file "label.json" 
# Reese's json file
# Read the json and find the value of the Items to use for intital startup
##data_Open_Location = "/home/pi/mnt/gdmedia/Project/label.json"
##startingdata = open(data_Open_Location, "r")
##StartingInfo = json.loads(startingdata.read().replace("'", "\""))
##startingdata.close()
##print(StartingInfo["Machine 1"]["Stock"])
##stock1 = StartingInfo["Machine 1"]["Stock"] 

###################################### Screen Class ######################################################
# the window itself
# class for the screen
class Screen(Frame):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.IN, GPIO.PUD_DOWN)
    i = GPIO.input(20)
    if (i == True):
        stock = 1
        print("thing")
    else:
        print("lol")
        stock = 0
    print(stock)
    data_Open_Location = "/home/pi/mnt/gdmedia/Project/label.json"
    data = open(data_Open_Location, "w")
    info = {"Machine 1":
                        {
                            
                            "Stock": stock,
                            "Sold": 1- stock
                            
                        }}
    data.write(str(info))
    data.close()
    sold = 1-stock
    num = 0
    #stock = StartingInfo["Machine 1"]["Stock"]
    #sold = StartingInfo["Machine 1"]["Sold"]
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="black")
        self.setupGUI()
        

    # the setup
    def setupGUI(self):
        self.Level1()
        # BackGround in progress
        # Mason's file
        #bg = PhotoImage(file = "Project Buttons/La_tech.gif")
        # Reese's file
        bg = PhotoImage(file = "/home/pi/Freshman Expo Project/La_tech.gif")
        self.label= Label(self, image=bg)
        self.label.image = bg
        self.label.place(x=0,y=0,relheight=1, relwidth=1)
        self.pack(fill=BOTH, expand=1)
        # variable for assigning the image

        # Mason's file
        #img = PhotoImage(file = "Project Buttons/dew.gif")
        # Reese's file
        img = PhotoImage(file="/home/pi/Freshman Expo Project/dew.gif")
        # the setup for the button itself, assigning the image on top of it
        self.button = Button(self, bg="white", image=img,borderwidth=0, command=lambda: self.StockPage())
        self.button.image = img
        # shove it in a cell
        self.button.place(x=300, y=100)                                       # Change to fix RPI display

        # Mason's file
        #Simg = PhotoImage(file = "Project Buttons/SettingIcon.png")
        # Reese's file
        Simg = PhotoImage(file="/home/pi/Freshman Expo Project/SettingIcon.png")
        self.SettingIcon = Button(self, image=Simg, borderwidth=0,command=lambda: self.SettingsPage())
        self.SettingIcon.image = Simg
        self.SettingIcon.place(x=0, y=0, relheight=0.2, relwidth=0.17)
        
        # Mason's file
        #InfoButtonPicture = PhotoImage(file="Project Buttons/Info_Button.png")
        # Reese's file
        InfoButtonPicture = PhotoImage(file="/home/pi/Freshman Expo Project/Info_Button.png")
        self.InfoButton = Button(self, image=InfoButtonPicture, borderwidth=0,command=lambda: self.InfoPage())
        self.InfoButton.image = InfoButtonPicture
        self.InfoButton.place(x=0, y=375, relheight=0.212, relwidth=0.16)
        # Mason's file
        #Chart = PhotoImage(file="Project Buttons/chart.png")
        # Reese's file
        Chart = PhotoImage(file="/home/pi/Freshman Expo Project/Chart.png")
        self.ChartButton = Button(self, image=Chart, borderwidth=0, command=lambda: self.ChartPage())
        self.ChartButton.image = Chart
        self.ChartButton.place(x=640, y=0, relheight=0.21, relwidth=0.17)
        


    # This function creates the info page. 
    # It clears the screen of all vending options and displays the info menu.
    def InfoPage(self):
        # Clears all vending options.
        self.Level1()
        # Mason's file
        #textimg = PhotoImage(file="Project Buttons/Info_Tech.png")
        # Reese's file
        textimg = PhotoImage(file="/home/pi/Freshman Expo Project/Info_Tech.png")
        self.Text = Label(self, image= textimg, borderwidth=0)
        self.Text.image = textimg
        self.Text.place(x=0, y=0, relheight=1, relwidth=1)
        self.BackButton = Button(self, text="Home", bg="blue", command=lambda: self.setupGUI() )
        self.BackButton.place(x=200, y =400)

    # Controls the Chart page after you click the chart button
    def ChartPage(self):
        # Cleans the Board
        self.Level1()
        # packs the background image
        # Mason's file 
        #img = PhotoImage(file="Put your file path here")
        # Reese's File
        img = PhotoImage(file="/home/pi/Freshman Expo Project/Chart_page.png")
        self.label1 = Label(self, image=img)
        self.label1.image = img
        self.label1.place(x=0, y=0, relheight=1, relwidth=1)
        self.text1 = Label(self, text="Items Sold:", font=("Arial", 25), border=2)
        self.text1.place(x= 10, y=200, relheight=0.2, relwidth=0.3)

        # Re intializes the Back Button
        self.BackButton = Button(self, text = "Home", bg="blue", command= lambda: self.setupGUI())
        self.BackButton.place(x= 50, y=50)
        if (self.sold > 0):
            self.Block = Label(self, bg="cyan", borderwidth=0)
            self.Block.place(x = 375, y =265, relwidth=0.2, relheight=0.271)
            #if (self.sold>1):
             #   self.Block1 = Label(self, bg="cyan", borderwidth=0)
              #  self.Block1.place(x = 375, y =95, relwidth=0.2, relheight=0.4)
    def change(self):
        self.data = open(self.data_Open_Location, "w")
        info = {"Machine 1":
                        {
                            
                            "Stock": self.stock,
                            "Sold": 1- self.stock
                            
                        }}
        self.data.write(str(info))
        self.data.close()
        print(self.stock)
        self.Level1
        return


    
    # This function creates the settings page. 
    # It clears the screen of all vending options and displays the options menu.
    # To enter the settings menu, an prompt will pop up asking for a password. Correct password results in entering options, while failed denies access.
    def SettingsPage(self):
        # Clears all vending options
        self.Level1()
        # The contents of the options menu (WIP)
        # the back button
        self.label.pack(fill=BOTH, expand=1)
        self.BackButton = Button(self, text="Home", bg="blue", command=lambda: self.setupGUI() )
        self.BackButton.place(x=100, y=90)

        # a label asking for a password
        self.passlabel = Label(self, text="Enter password", font=("Arial", 20))
        self.passlabel.place(x=250, y=10)

        # entry space for password
        # password is "admin"
        # this can be changed in the main code
        self.passwordEntry = Label( width=35,font=("Arial", 20), bg = "white", borderwidth = 2)
        self.passwordEntry.place(x=100, y=50)

        # the confirm button
        # when clicked, determines if the entered password is correct or incorrect
        self.confirm = Button(self, text="Confirm", font=("Arial", 10), activebackground="green", command =lambda: self.PassConfirm() )
        self.confirm.place(x=555, y=90)
        # the key pad
        # 7
        self.seven = Button(self,text="7",font=("Arial", 22), activebackground="red", command = lambda:self.process("7"))
        self.seven.place(x=250, y=130)

        # 8
        self.eight = Button(self,text="8",font=("Arial", 22), activebackground="red", command = lambda:self.process("8"))
        self.eight.place(x=300,y=130)

        # 9
        self.nine = Button(self,text="9",font=("Arial", 22), activebackground="red", command = lambda:self.process("9"))
        self.nine.place(x=350,y=130)

        # Back
        self.back = Button(self,text="<-",font=("Arial", 22), activebackground="red", command = lambda:self.process("Back"))
        self.back.place(x=400, y=130)


        # 4
        self.four = Button(self,text="4",font=("Arial", 22), activebackground="red", command = lambda:self.process("4"))
        self.four.place(x=250,y=200)

        # 5
        self.five = Button(self,text="5",font=("Arial", 22), activebackground="red", command = lambda:self.process("5"))
        self.five.place(x=300,y=200)

        # 6
        self.six = Button(self,text="6",font=("Arial", 22), activebackground="red", command = lambda:self.process("6"))
        self.six.place(x=350,y=200)

        # 1
        self.one = Button(self,text="1",font=("Arial", 22), activebackground="red", command = lambda:self.process("1"))
        self.one.place(x=250,y=270)

        # 2
        self.two = Button(self,text="2",font=("Arial", 22), activebackground="red", command = lambda:self.process("2"))
        self.two.place(x=300,y=270)

        # 3
        self.three = Button(self,text="3",font=("Arial", 22), activebackground="red", command = lambda:self.process("3"))
        self.three.place(x=350,y=270)

        # 0
        self.zero = Button(self,text="0",font=("Arial", 22), activebackground="red", command=lambda:self.process("0"))
        self.zero.place(x=300, y=340)
                        
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
        
        # a cap on the password
        elif(len(pass_input) >= 8):
            strings = [str(integer) for integer in pass_input]
            a_string = "".join(strings)
            c_string = "".join(pass_conceal)
            conNoSpaces = c_string
            self.passwordEntry["text"] = conNoSpaces
        
        
        
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
        self.Level1()
        # Mason's file
        #bg = PhotoImage(file = "Project Buttons/La_tech.gif")
        # Reese's file
        bg = PhotoImage(file = "/home/pi/Freshman Expo Project/La_tech.gif")
        self.label= Label(self, image=bg)
        self.label.image = bg
        self.label.place(x=0,y=0,relheight=1, relwidth=1)
        self.pack(fill=BOTH, expand=1)
        
        # the request maintenance button
        self.reqMain = Button(self, bg="red", text="Request Maintenance",font=("Arial", 20), command = lambda: self.requestMain())
        self.reqMain.place(x=50, y=100)

        # Button connected to go back to home page
        self.BackButton = Button(self, bg = "blue", text = "Home", font=("Arial", 25), command= lambda: self.setupGUI())
        self.BackButton.place(x=500, y=100)

        # recalbrate button
        self.recalbrate = Button(self, bg = "white", text = "Recalibrate", font=("Arial", 25), command= lambda: self.Recalbrate())
        self.recalbrate.place(x=400, y=300)
        
    # Recalbrate the stock
    def Recalbrate(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(20, GPIO.IN, GPIO.PUD_DOWN)
        i = GPIO.input(20)
        if (i == True):
            self.stock = 1
            self.sold = 0
            self.change()
            return
        self.stock = 0
        self.sold = 1
        self.change()
        
    # this is where the code will go for sending a text message requesting for maintenance
    def requestMain(self):
        # twilio set up
        # download twilio
        account_sid = "AC6078307f4c950e4fa6fc3ed5375301ae"

        auth_token  = "3d66b86fd208c2b9c70f10628af90a58"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+13183444853",
            from_="+18623621556",
            body="Machine 1 needs assistance!")

        print(message.sid)
        

    # displays the entered password is incorrect
    # destroys itself after 3 seconds
    def PassFail(self):
            pass_input.clear()
            pass_conceal.clear()
            self.passwordEntry["text"] = ""
            incorrect = Label(text="Incorrect password. Try again")
            incorrect.place(x=250, y=100)
            incorrect.after(1000, lambda: incorrect.destroy())


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
            self.label5.forget()
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
        try:
            self.minus.destroy()
            self.confirm.destroy()
            self.more.destroy()
        except:
            pass
        try:
            self.text1.destroy()
        except:
            pass
        try:
            self.confirm.destroy()
            self.passwordEntry.destroy()
            self.passlabel.destroy()
            self.nine.destroy()
            self.eight.destroy()
            self.seven.destroy()
            self.six.destroy()
            self.five.destroy()
            self.four.destroy()
            self.three.destroy()
            self.two.destroy()
            self.one.destroy()
            self.zero.destroy()
            self.back.destroy()
            try:
                pass_input.clear()
                pass_conceal.clear()
            except:
                pass
        except:
            pass
        try:
            self.reqMain.destroy()
            self.recalbrate.destroy()
        except:
            pass

    # Controls the Animation on the Stock page of the Mountain Dew
    def Mountaindew(self):
        self.num = 0
        # Mason's file
        #img = Image.open(r"Project Buttons/dewspin.gif")
        # Reese's file
        img = Image.open(r"/home/pi/Freshman Expo Project/dew.gif")
        framesTotal = img.n_frames

        play_back_delay = 130
        animation = []
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
        self.label5.place(x=300, y = 100)
        loadGif()
        update(0)
        # Reese's file
        Plus = PhotoImage(file="/home/pi/Freshman Expo Project/Plus_Sign.png")                       ##### Change file path
        self.more = Button(self, image=Plus, borderwidth=0, command=lambda: self.StockChange(1))
        self.more.image = Plus
        self.more.place(x=440, y=320, relheight=0.2, relwidth=0.2)
        self.BackButton = Button(self, text="Back", font=("Arial",25),command= lambda: self.setupGUI())
        self.BackButton.place(x=330, y=30, relheight=0.1, relwidth=0.2)
        # Reese's File 
        Minus = PhotoImage(file="/home/pi/Freshman Expo Project/Minus_Sign.png")                      ##### Change File Path
        self.minus = Button(self, image=Minus, borderwidth=0, command=lambda: self.StockChange(-1))
        self.minus.image = Minus
        self.minus.place(x=223, y=320, relheight=0.2, relwidth=0.14)
        self.text1 = Label(self, bg="white", text=f"{self.num}", font=("Arial", 25),background="green")
        self.text1.place(x=320, y=320, relheight=0.2, relwidth=0.2)
        self.confirm = Button(self, text="Confirm", bg="green", font=("Arial", 25), command=lambda: self.Confirmed())
        self.confirm.place(x = 320, y = 430, relheight=0.1, relwidth=0.2)

    def StockChange(self, num1):
        if (self.num>0 and num1 == 1):
            return
        if (self.num==0 and num1 == -1):
            return
        num = self.num+num1
        self.num = num
        self.text1.configure(bg="white", text=f"{self.num}", font=("Arial",25) ,background="green")
        self.text1.place(x=320, y=320, relheight=0.2, relwidth=0.2)
    
    def Confirmed(self):
        Catch = self.stock - self.num
        if (Catch<0):
            label6 = Label(self,bg = "red", text = "Sold Out", font = ("Arial", 25))
            label6.place(x=60, y=200)
            label6.after(1000, lambda: label6.destroy())
            return
        if (self.num!= 0):
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(16, GPIO.OUT)
            GPIO.output(16, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)
        self.stock -=self.num
        self.sold = 2-self.stock
        self.change()
        self.num = 0
        self.setupGUI()





############################# Main Function ########################################################################################################
# this REQUIRES the list() function
# changing this will mean changing the code of the SettingsPage() function
password = ("0","0","0","0")
pass_input = []
pass_conceal = []





# basic tk stuff, just setting up the screen and constantly looping the class
window = Tk()
window.geometry("{}x{}".format(800, 480))
try:
    if count == 1:
        pass
except:
    window.attributes('-fullscreen', True)
window.bind("<Escape>", lambda event: Escape())
def Escape():
    window.attributes('-fullscreen', False)
    try:
        GPIO.cleanup()
    except:
        pass
    count = 1
s = Screen(window)
s.mainloop()
