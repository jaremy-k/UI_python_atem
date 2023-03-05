import eel
import PyATEMMax as ate
import json

debug = False
afk = False

switcher1 = ate.ATEMMax()
switcher2 = ate.ATEMMax()
eel.init("web")

def getSettingsFromJson():
    data = None
    with open('web/config.JSON') as json_file:
        data = json.load(json_file)
    return data

@eel.expose
def init():
    if debug:
        return [2, 1, 0, 1]
    else:
        return [switcher1.previewInput[0].videoSource.value-1,
                switcher1.programInput[0].videoSource.value-1,
                0,
                switcher2.programInput[0].videoSource.value
                ]

@eel.expose
def saveSettings(switcher1_ip, switcher2_ip, pp_linking):
    global settings
    try:
        data = None
        with open('web/config.JSON') as json_file:
            data = json.load(json_file)
        data["Switcher 1"] = switcher1_ip
        data["Switcher 2"] = switcher2_ip
        data["propresenter_linking"] = pp_linking
        json_string = json.dumps(data)
        with open('web/config.JSON', 'w') as outfile:
            outfile.write(json_string)
        settings = getSettingsFromJson()
    except Exception:
        print("config.json is not founded")


# Switcher 1 functions
@eel.expose
def setProgram(x):
    if not switcher1.connected:
        switcher1.connect(settings['Switcher 1'])
    switcher1.setProgramInputVideoSource(0, int(x)+1)
    return

@eel.expose
def setPreview(x):
    if not switcher1.connected:
        switcher1.connect(settings['Switcher 1'])
    switcher1.setPreviewInputVideoSource(0, int(x)+1)


@eel.expose
def setMixState(x):
    if not switcher1.connected:
        switcher1.connect(settings['Switcher 1'])
    switcher1.setTransitionPosition(0, int(x))

# Switcher 2 functions
@eel.expose
def setProgramPC(x):
    if not switcher2.connected:
        switcher2.connect(settings['Switcher 2'])
    switcher2.setProgramInputVideoSource(0, int(x)+1)
    return

@eel.expose
def beginAFK(x):
    if not switcher2.connected:
        switcher2.connect(settings['Switcher 2'])
    print(int(x))

# Main

settings = getSettingsFromJson()

if not debug:
    # switcher1.connect(settings['Switcher 1'])
    switcher2.connect(settings['Switcher 2'])

try:
    eel.start("index.html", port=5700)
except Exception:
    eel.start("index.html", mode='default', port=5700)
