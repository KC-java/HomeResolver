from Apps.app import App


class BatteryBackupManagement(App):
    # Request optional charging when close to lowest
    # Offer to supply when close to highest
    def __init__(self, charge_cutoff_rate, discharge_cutoff_rate):
        self.charge_cutoff_rate = charge_cutoff_rate
        self.discharge_cutoff_rate = discharge_cutoff_rate
        App.__init__(self, "Battery Backup Management")

    def update(self, sys):
        if sys.sensors["Power Rate"].get_value() <= self.charge_cutoff_rate:
            App.app_print(
                "[Battery Backup Management] [Battery Backup] Charging requested")
            # charge
            return [{"device": "Battery Backup", "target": "charging"}], [[sys.devices["Battery Backup"].get_resource_usage("charging", {})["charging_rate"], 300, 1]], [], [], [], []
        elif sys.sensors["Power Rate"].get_value() >= self.discharge_cutoff_rate:
            pwr_cons = sys.sensors["Power Meter"].get_value()
            sys.devices["Battery Backup"].variables["consumption"] = pwr_cons
            App.app_print(
                "[Battery Backup Management] [Battery Backup] Supplying requested")
            # discharge
            return [{"device": "Battery Backup", "target": "supplying"}], [[-pwr_cons, 300, 1]], [0], [], [], []
        return [], [], [], [], [], []
