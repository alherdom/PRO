class OS:
    graphical_interface = True

    def __init__(
        self,
        name: str,
        version: str,
        developer: str,
        kernel_type: str,
        system_file: str,
        xserver: str,
    ):
        self.name = name
        self.version = version
        self.developer = developer
        self.system_file = system_file
        self.kernel_type = kernel_type
        self.booted = False
        self.updated = False
        self.upgraded = False
        self.xserver = xserver
        self.users_info = {"names": [], "passwords": [], "groups": []}
        self.ip = "172.18.99.202"
        self.load = 0

    def switch_boot(self):
        self.booted = not self.booted

    def update(self):
        self.updated = not self.updated

    def upgrade(self):
        self.upgraded = not self.upgraded

    # 172.18.99.202/16
    @property
    def mask_calculator(self, ip: str, cidr: str) -> list:
        num_of_octet, rest = divmod(int(cidr), 8)
        defatult_octet = "255."
        mask = defatult_octet * num_of_octet
        return mask

    def create_user(self, name: str, password: str, group: str):
        names = self.users_info["names"]
        if name in names:
            return False, "Error"
        names.append(name)


    def if_updated(self):
        pass

    def if_upgraded(self):
        pass

    def delete_user(self, name: str):
        pass

    def intall_aplication(self):
        pass

    def uninstall_aplication(self):
        pass

    def start_service(self):
        pass

    def stop_service(self):
        pass
