import glob, os
from appJar import gui

# Function to handle the election of a Radio Check
def choose(rb):
    selected[0] = app.getRadioButton(rb)

def update(btn):
    print("Beginning updating process of",selected[0])
    app.setStatusbar(updating, 0)

# We build our GUI
app = gui()

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

#Messages for statusbar
wait = "waiting for user to choose an application..."
updating = "updating the selected application..."

#Statusbar for easy debuggin'.
app.addStatusbar(fields=1)
app.setStatusbar(wait, 0)
#This button trigger the update process
app.addButton("Update", update)
#Run the app
app.go()
