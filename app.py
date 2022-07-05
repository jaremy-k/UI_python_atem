import eel
import PyATEMMax as ate

switcher = ate.ATEMMax()

eel.init("web")

switcher.connect('192.168.10.240')

@eel.expose
def connect(x):
    switcher.connect(x)
    print(x)
    return True

@eel.expose
def setProgram(x):
    if switcher.connected == False:
        switcher.connect(x)
    switcher.setProgramInputVideoSource(0, int(x)+1)
    return

@eel.expose
def setPreview(x):
    if switcher.connected == False:
        switcher.connect(x)
    switcher.setPreviewInputVideoSource(0, int(x)+1)


eel.start("index.html", mode='default')