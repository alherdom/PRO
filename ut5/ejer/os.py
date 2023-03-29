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
        self.ip = "172.18.99.202/14"
        self.load = 0

    def switch_boot(self):
        self.booted = not self.booted

    def update(self):
        self.updated = not self.updated

    def upgrade(self):
        self.upgraded = not self.upgraded

    # 172.18.99.202/16
    def mask_calculator(self):
        cidr = int(self.ip.split("/")[-1])
        ones = "1" * cidr
        ceros = "0" * (32 - cidr)
        mask = ""
        binary_mask = ones + ceros
        for i, bit in enumerate(binary_mask, start=1):
            mask += bit
            if i % 8 == 0 and i != 0:
                mask += "."      
        print(mask)
        


    def add_users(self, name: str, password: str):
        names = self.users_info["names"]
        passwords = self.users_info["passwords"]
        if name in names:
            return False, "Error"
        names.append(name)
        passwords.append(password)

    def add_groups(self, group: str):
        groups = self.users_info["groups"]
        if group in groups:
            return False, "Error"
        groups.append(group)

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


linux = OS("linux", "1.0", "canonical", "monolítico híbrido", "system_file", "xorg")
linux.mask_calculator()
