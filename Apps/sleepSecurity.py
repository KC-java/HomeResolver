from Apps.app import App


class SleepSecurity(App):
    def __init__(self):
        App.__init__(self, "Sleep Security")

    def update(self, sys):
        if not sys.sensors["Sleep Sensor"].value:
            App.app_print("[Sleep Security] [Doors] Doors closed requested")
            return [{"device": "Doors", "target": "closed"}], [[0, 9, 10]], [], [], [], []
        return [], [], [], [], [], []
