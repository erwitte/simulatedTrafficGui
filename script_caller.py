import os
import subprocess


class ScriptCaller:

    def __init__(self):
        self.script = os.path.expanduser("~/Schreibtisch/alles/PycharmProjects/simulatedTraffic/main.py")

    def start_script(self):
        subprocess.run(["python", str(self.script)])
