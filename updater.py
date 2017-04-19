import glob, os
from appJar import gui

#Setting the default AppFolder:
#folder = "/home/unnamed_query/Apps"

#We read the user settings before starting the app.
def setAppFolder():
    global folder
    try:
        prefs_file = open("prefs.txt")
    except OSError as err:
        # Esto queda pendiente de revisión, hasta ahora funciona bien si es que el archivo ha sido creado previamente.
        print("There are no prefs, attempting to create it...")
        app.infoBox("Choose App folder", "There is no App Folder set, please select the folder where you AppImages are.")
        folder = app.directoryBox(title="Select you App Folder", dirName="~/")
        new_prefs_file = "prefs.txt"
        write_prefs = open(new_prefs_file, 'w')
        write_prefs.write(folder)
    else:
        folder = prefs_file.read()
        folder = folder.split('\n')[0]
        os.chdir(folder)

#We open a dialog to choose the folder, then we call setAppFolder.
def changeAppFolder():
    print("changed")

# Function to handle the election of a Radio Check
def choose(rb):
    global selected
    selected = app.getRadioButton(rb)

def press(name):
    if (name=="Change App Folder"):
        changeAppFolder()

    if (name=="Update"):
        print("Beginning updating process of",selected[0])

    if (name=="Exit"):
        app.stop()

# We build our GUI and do some config
app = gui()
app.setTitle("Application Updater")
app.setResizable(False)
setAppFolder()

#Adding a Label with Text
app.addLabel("welcome", "This little script allow you to update your AppImages in ~/Apps\nSelect the Application that you want to update:")

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
