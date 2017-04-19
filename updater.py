import glob, os
from appJar import gui

scriptDir = os.path.dirname(os.path.realpath(__file__))

#We read the user settings before starting the app.
def setAppFolder():
    global folder
    try:
        prefs_file = open("prefs.txt")
    except OSError as err:
        # Esto queda pendiente de revisión, hasta ahora funciona bien si es que el archivo ha sido creado previamente.
        print("No preference file found, attempting to create it...")
        app.infoBox("Choose App folder", "There is no App Folder set, please select the folder where you AppImages are.")
        folder = app.directoryBox(title="Select you App Folder", dirName="~/")
        folder = folder.split('\n')[0]
        new_prefs_file = "prefs.txt"
        write_prefs = open(new_prefs_file, 'w')
        write_prefs.write(folder)
        os.chdir(folder)
    else:
        folder = prefs_file.read()
        folder = folder.split('\n')[0]
        os.chdir(folder)

# Function to handle the election of a Radio Check
def choose(rb):
    global selected
    selected = app.getRadioButton(rb)

def press(btn):
    print("updated")

# We build our GUI and do some config
app = gui()
app.setTitle("Application Updater")
app.setResizable(False)
setAppFolder()

#For every App in the folder, fill a list of Radio Button
if (glob.glob("*.AppImage") == []):
    app.addLabel("welcome", "We couldn't find any AppImage in this folder. Please run the program again.")
    os.remove(scriptDir+"/prefs.txt")
else:
    #Adding a Label with Text
    app.addLabel("welcome", "This little script allow you to update your AppImages in ~/Apps\nSelect the Application that you want to update:")
    for file in glob.glob("*.AppImage"):
        f = file.split('-')[0].split('.')[0]
        app.addRadioButton("application", f)
    #This button trigger the update process
    app.addButton("Update", press, 4, 0)
    #Bind the Radio Buttons to the function Choose
    app.setRadioButtonFunction("application", choose)
    selected = [app.getRadioButton("application")]

#Run the app
app.go()
