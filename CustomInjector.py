from asarPy import extract_asar
from os import listdir
import os.path
print("Welcome to the SlackAttack v1.1 custom injector!\nPlease enter the location of the JS code you would like to inject:\n")
location = input()
with open(location, 'r') as jsfile:
  js = "\n" + jsfile.read()
homedir = os.path.expanduser("~")
verDir = homedir + "\\AppData\\Local\\slack"
verArray = []
for f in listdir(verDir):
    split = f.split('-')
    if split[0] == 'app' and f != "app-release.ico":
        verArray.append(split[1])
maxVer = max(verArray)
appFile = verDir + "\\app-" + maxVer + "\\resources\\app.asar"
extractFolder =  verDir + "\\app-" + maxVer + "\\resources\\"
os.system("taskkill /IM slack.exe /F")
extract_asar(appFile, extractFolder + "app")
file = open(extractFolder + "app\\" + "dist\\main-preload-entry-point.bundle.js", 'a')
file.write(js)
file.close()
os.system("del /f " + appFile)
print("Injection successful.")
