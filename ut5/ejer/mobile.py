OPERATION_CONSUMPTION_BATTERY = 1
ON_CONSUMPTION_BATTERY = 5
OFF_CONSUMPTION_BATTERY = 2


class MobilePhone:
    def __init__(
        self, manufacturer: str, screen_size: float, num_cores: int, battery: int
    ):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = ["Whatsapp", "YouTube", "Twitter"]
        self.status = False
        self.battery = battery

    def switch_power(self):
        if self.status:
            self.battery -= OFF_CONSUMPTION_BATTERY
        else:
            self.battery -= ON_CONSUMPTION_BATTERY
        self.status = not self.status

    def install_apps(self, *apps: str):
        for app in apps:
            if app not in self.apps:
                self.apps.append(app)
            else:
                print("The app has been install")

    def uninstall_apps(self, apps: list):
        for app in apps:
            if app in self.apps:
                self.apps.remove(app)
            else:
                print("The app has been unistall")

    def battery_recharge(self, battery):
        to_charge = min(battery, self.battery + battery)
        self.battery = to_charge

    def show_installed_apps(self):
        print(self.apps)

    def last_installed_app(self):
        return self.apps[-1]


iphone = MobilePhone("Apple", 6.4, 8, 3000)
iphone.install_apps("Tiktok")
iphone.show_installed_apps()
print(iphone.last_installed_app())
