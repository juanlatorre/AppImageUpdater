import glob, os
from appJar import gui

# Function to handle the election of a Radio Check
def choose(rb):
    selected[0] = app.getRadioButton(rb)

def press(name):
    if (name=="Change App Folder"):
        print("Folder changed")

    if (name=="Update"):
        print("Beginning updating process of",selected[0])
        app.setStatusbar(updating, 0)

    if (name=="Exit"):
        app.stop()

# We build our GUI and do some config
app = gui()
app.setTitle("Application Updater")
app.setResizable(False)
app.setLocation(0,0)

#Adding a Label with Text
app.addLabel("welcome", "This little script allow you to update your AppImages in ~/Apps\nSelect the Application that you want to update:")
#Focus on Apps Folder
os.chdir("/home/unnamed_query/Apps")
#For every App in the folder, fill a list of Radio Button
for file in glob.glob("*.AppImage"):
    #appList.append(file)
    f = file.split('-')[0].split('.')[0]
    app.addRadioButton("application", f)

#Bind the Radio Buttons to the function Choose
app.setRadioButtonFunction("application", choose)
selected = [app.getRadioButton("application")]

#This button trigger the update process
app.addButtons(["Change App Folder", "Update", "Exit"], press, 5, 0, 5)

#Run the app
app.go()
