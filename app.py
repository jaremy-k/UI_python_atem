import eel
import PyATEMMax as ate
import json

debug = False
switcher = ate.ATEMMax()
afk = False

eel.init("web")

switcher.connect('192.168.10.245')

@eel.expose
def init():
    if (debug):
        return [2, 1, 0]
    else:
        return [switcher.previewInput[0].videoSource.value-1, switcher.programInput[0].videoSource.value-1, 0]

@eel.expose
def saveSettings(switcher1_ip, switcher2_ip, pp_linking):
    data = None;
    with open('web/config.JSON') as json_file:
        data = json.load(json_file)
    data["Switcher 1"] = switcher1_ip
    data["Switcher 2"] = switcher2_ip
    data["propresenter_linking"] = pp_linking
    json_string = json.dumps(data)
    with open('web/config.JSON', 'w') as outfile:
        outfile.write(json_string)


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


@eel.expose
def setMixState(x):
    if switcher.connected == False:
        switcher.connect(x)
    switcher.setTransitionPosition(0, int(x))

@eel.expose
def beginAFK(x):
    if switcher.connected == False:
        switcher.connect(x)
    print(int(x))

try:
    eel.start("index.html", port=8080)
except Exception:
    eel.start("index.html", mode='default', port=8080)
