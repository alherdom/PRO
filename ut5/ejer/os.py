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
        self.users_info = {"name": "", "info": {}}
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

    # Esto puede ser un decorador...
    def check_info_users(self, name: str, password: str) -> tuple[bool, str]:
        for name, password in self.users_info.items():
            if name in self.users_info and password in self.users_info:
                return (
                    False,
                    "Error, usuario o contraseña ya existen, pruebe a modificarlos",
                )
        return True, "Parámetros correctos, el usuario o contraseña no existan"

    def modify_users(self, name: str, new_password: str, new_group: str):
        if name not in self.users_info:
            return False, "Error"
        values = self.users_info[name]
        password, group = values

    def create_user(self, name: str, password: str, group: str):
        if name in self.users_info:
            return False, "Error"
        self.users_info[name] = [password, group]
        pass

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
