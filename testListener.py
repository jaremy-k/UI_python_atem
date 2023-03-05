import PyATEMMax as ate
from typing import Dict, Any
import argparse
import time
import eel

eel.init("obs")

def onReceive(params: Dict[Any, Any]) -> None:
    if (params['cmd']=='PrgI'):
        eel.hideText(int(switcher1.programInput[0].videoSource.value) == 2 or int(switcher2.programInput[0].videoSource.value) == 2)
        print(f"Program1 viewport is changed to {switcher1.programInput[0].videoSource.value}")
        print(f"Program2 viewport is changed to {switcher2.programInput[0].videoSource.value}")

switcher1 = ate.ATEMMax()
switcher2 = ate.ATEMMax()

switcher1.connect('192.168.10.240')
switcher2.connect('192.168.10.245')

switcher1.registerEvent(switcher1.atem.events.receive, onReceive)
switcher2.registerEvent(switcher2.atem.events.receive, onReceive)

eel.start("index.html", port=8080)