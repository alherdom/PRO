import random


class OS:
    graphical_interface = True
    load = 0

    def __init__(self, name: str, version: str, developer: str, kernel_type: str, system_file: str, xserver: str):
        self.name = name
        self.version = version
        self.developer = developer
        self.system_file = system_file
        self.kernel_type = kernel_type
        self.booted = False
        self.updated = False
        self.upgraded = False
        self.xserver = xserver
        self.users_info = dict
        OS.load += 1

    def switch_boot(self):
        self.booted = not self.booted

    def update(self):
        self.updated = not self.updated

    def upgrade(self):
        self.upgraded = not self.upgraded

    @property
    def get_ip(self) -> str:
        first_num = str(random.randint(0, 255)) + "."
        second_num = str(random.randint(0, 255)) + "."
        third_num = str(random.randint(0, 255)) + "."
        fourth_num = str(random.randint(0, 255))
        return first_num + second_num + third_num + fourth_num

    # Esto puede ser un decorador?
    def check_info_users(self, name: str, password: str) -> tuple[bool, str]:
        for name, password in self.users_info.items():
            if name in self.users_info and password in self.users_info:
                return (
                    False,
                    "Error, usuario o contraseña ya existen, pruebe a modificarlos",
                )
        return True, "Parámetros correctos, el usuario o contraseña no existan"

    def modify_users(self, name: str) -> tuple[bool, str]:
        return True, "Usuario modificado"

    def create_user(self, name: str, password: str) -> tuple:
        self.users_info[name] = password
        return (True, "Se crea el usuario")
        return (False, "Erro usuario o contraseña ya existen")

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
