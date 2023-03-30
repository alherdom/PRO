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
        self.users_info = {}
        self.groups_info = {}
        self.__ip = "172.18.99.202/31"
        self.load = 0

    @staticmethod
    def get_os_categories() -> list[str]:
        return ["Multitask", "Multiuser", "Multiprocess"]

    def calculate_mask(self):
        cidr = int(self.__ip.split("/")[-1])
        subnet_mask = []
        binary_mask = ""
        ones_ceros = ("1" * cidr) + ("0" * (32 - cidr))
        for i, bit in enumerate(ones_ceros, start=1):
            binary_mask += bit
            if i % 8 == 0 and i != 32:
                binary_mask += "."
        for octet in binary_mask.split("."):
            decimal_num = 0
            for i, bit in enumerate(octet[::-1]):
                decimal_num += int(bit) * 2**i
            subnet_mask.append(str(decimal_num))
        print(".".join(subnet_mask))

    def add_user(self, name: str, password: str) -> tuple:
        if name in self.users_info:
            return False, "Error"
        self.users_info[name] = password
        return True, "User added"

    def del_user(self, name: str, password: str) -> tuple:
        if name not in self.users_info and password not in self.users_info:
            return False, "Error"
        del self.users_info[name]
        return True, "User deleted"

    def add_group(self, group: str, description: str) -> tuple:
        if group in self.groups_info:
            return False, "Error"
        self.groups_info[group] = description
        return True, "Group added"

    def del_group(self, group: str) -> tuple:
        if group not in self.groups_info:
            return False, "Error"
        del self.groups_info[group]
        return True, "Group deleted"

    def get_users(self):
        return self.users_info["names"]

    def get_groups(self):
        return self.users_info["groups"]

    def get_passwords(self):
        return self.users_info["passwords"]

    def switch_boot(self):
        self.booted = not self.booted

    def update(self):
        self.updated = not self.updated

    def upgrade(self):
        self.upgraded = not self.upgraded

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


linux = OS("linux", "21.0", "stallman", "monolithic hybrid", "system file", "xorg")
linux.calculate_mask()
print(linux.get_os_categories())
linux.add_user("alejandro", "123456")
linux.add_user("pepe", "654321")
linux.add_user("alejandro", "123456")
linux.add_user("raquel", "222222")
linux.add_group("admins")
linux.add_group("lp")
linux.add_group("scanner")
print(linux.get_users())
print(linux.get_groups())
print(linux.get_passwords())
linux.del_user("pepe", "654321")
print(linux.get_users())
