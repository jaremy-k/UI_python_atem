import eel
import PyATEMMax as ate
import json
import time
from typing import Dict, Any

debug = True
activeProgram = 1
activePreview = 1

def getSettingsFromJson():
    data = None
    with open('web/config.JSON') as json_file:
        data = json.load(json_file)
    return data

def onReceive(params: Dict[Any, Any]) -> None:
    global activePreview
    global activeProgram
    if (params['cmd']=='PrgI'):
        activeProgram = int(switcher1.programInput[0].videoSource.value)
        eel.setProgram(int(switcher1.programInput[0].videoSource.value) - 1)
    if (params['cmd']=='PrvI'):
        activePreview = int(switcher1.programInput[0].videoSource.value)
        eel.setPreview(int(switcher1.previewInput[0].videoSource.value) - 1)

# Switcher 1 functions
@eel.expose
def setProgram(x):
    # if not switcher1.connected:
    #     switcher1.connect(settings['Switcher 1'])
    # switcher1.setProgramInputVideoSource(0, int(x) + 1)
    print("Program: ", int(x)+1)

@eel.expose
def swap():
    if not switcher1.connected:
        switcher1.connect(settings['Switcher 1'])
    switcher1.setProgramInputVideoSource(0, int(activePreview))
    switcher1.setPreviewInputVideoSource(0, int(activeProgram))
    
@eel.expose
def smoothSwap():
    startTime = time.time()
    while (time.time() - startTime < 1.5):
        time.sleep(0.05)
        setMixState(int( (time.time() - startTime) / 1.5 * 10000 ))
        
@eel.expose
def setPreview(x):
    # if not switcher1.connected:
    #     switcher1.connect(settings['Switcher 1'])
    # switcher1.setPreviewInputVideoSource(0, int(x) + 1)
    print("Preview: ", int(x)+1)

@eel.expose
def setMixState(x):
    print(x)
    # if not switcher1.connected:
    #     switcher1.connect(settings['Switcher 1'])
    # switcher1.setTransitionPosition(0, int(x))

switcher1 = ate.ATEMMax()
switcher2 = ate.ATEMMax()

eel.init("web")

settings = getSettingsFromJson()

if not debug:
    switcher1.connect(settings['Switcher 1'])
    switcher2.connect(settings['Switcher 2'])

    switcher1.registerEvent(switcher1.atem.events.receive, onReceive)
    switcher2.registerEvent(switcher2.atem.events.receive, onReceive)

try:
    eel.start("index.html", port=5700)
except Exception:
    eel.start("index.html", mode='default', port=5700)