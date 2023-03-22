OPERATION_CONSUMPTION_BATTERY = 1
ON_CONSUMPTION_BATTERY = 5
OFF_CONSUMPTION_BATTERY = 2

class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = ["Whatsapp","YouTube","Twitter"]
        self.status = False
        self.battery = 100
        
    def switch_power(self):
        if self.status:
            self.battery -= OFF_CONSUMPTION_BATTERY
        else:
            self.battery -= ON_CONSUMPTION_BATTERY
        self.status = not self.status
    
    def install_app(self, *apps: str ):
        for app in apps:
            if app not in self.apps:
                self.apps.append(app)
            else:
                print("The app has been install")
        
    def uninstall_app(self, apps: list):
        if apps in self.apps:
            self.apps.remove(apps)
        else:
            print("The app has been unistall")
            
    def battery_recharge(self, battery):
        to_charge = min(100, self.battery + battery)
        self.battery = to_charge
        
iphone = MobilePhone("Apple",6.4,8)   
iphone.
