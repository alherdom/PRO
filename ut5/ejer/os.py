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
        self.__ip = "172.18.99.202/16"
        self.load = 0

    @staticmethod
    def get_os_categories() -> list[str]:
        return ["Multitask", "Multiuser", "Multiprocess"]

    @staticmethod
    def audit(method):
        def wrapper(self, *args, **kwargs):
            print(f"Operation System {self.name} running {method.__name__}!")
            return method(self, *args, **kwargs)

        return wrapper

    @audit
    def calc_mask(self) -> str:
        cidr = int(self.__ip.split("/")[-1])
        subnet_mask = []
        binary_mask = ""
        number_of_zeros = 32 - cidr
        ones_zeros = ("1" * cidr) + ("0" * number_of_zeros)
        for i, bit in enumerate(ones_zeros, start=1):
            binary_mask += bit
            if i % 8 == 0 and i != 32:
                binary_mask += "."
        for octet in binary_mask.split("."):
            decimal_num = 0
            for i, bit in enumerate(octet[::-1]):
                decimal_num += int(bit) * 2**i
            subnet_mask.append(str(decimal_num))
        return ".".join(subnet_mask)

    @audit
    def calc_num_hosts(self):
        cidr = int(self.__ip.split("/")[-1])
        if cidr > 30:
            return 0
        number_of_zeros = 32 - cidr
        ones_of_host = "1" * number_of_zeros
        num_hosts = -1
        for i, bit in enumerate(ones_of_host[::-1]):
            num_hosts += int(bit) * 2**i
        print(f"The number of hosts is: {num_hosts}")

    @audit
    def get_type_mask(self):
        cidr = int(self.__ip.split("/")[-1])
        if cidr <= 8:
            return "The mask type is: A"
        if 9 <= cidr <= 16:
            return "The mask type is: B"
        if 24 <= cidr <= 32:
            return "The mask type is: C"

    # método que compruebe si existe el usuario/grupo/contraseña?

    def add_user(self, name: str, password: str) -> tuple:
        if name in self.users_info:
            return False, "❌ Error"
        self.users_info[name] = password
        return True, "✅ User added"

    def del_user(self, name: str, password: str) -> tuple:
        if name not in self.users_info and password not in self.users_info:
            return False, "❌ Error"
        del self.users_info[name]
        return True, "✅ User deleted"

    def add_group(self, group: str, description: str) -> tuple:
        if group in self.groups_info:
            return False, "❌ Error"
        self.groups_info[group] = description
        return True, "Group added"

    def del_group(self, group: str) -> tuple:
        if group not in self.groups_info:
            return False, "❌ Error"
        del self.groups_info[group]
        return True, "✅ Group deleted"

    def get_users(self):
        return list(self.users_info.keys())

    def get_groups(self):
        return self.groups_info

    def get_passwords(self):
        return self.users_info

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

    def intall_aplication(self):
        pass

    def uninstall_aplication(self):
        pass

    def start_service(self):
        pass

    def stop_service(self):
        pass

        self.processes = []
        
    def add_process(self, process):
        self.processes.append(process)
        print(f"Added process '{process}'")
        
    def remove_process(self, process):
        if process in self.processes:
            self.processes.remove(process)
            print(f"Removed process '{process}'")
        else:
            print(f"Process '{process}' not found")
            
    def list_processes(self):
        print("Running processes:")
        for process in self.processes:
            print(process)
            
    def get_os_info(self):
        return f"{self.name} version {self.version}"

linux = OS("linux", "21.0", "stallman", "monolithic hybrid", "system file", "xorg")
print(linux.calc_mask())
linux.calc_num_hosts()
print(linux.get_os_categories())
print(linux.get_type_mask())
linux.add_user("alejandro", "123456")
linux.add_user("pepe", "654321")
linux.add_user("alejandro", "123456")
linux.add_user("raquel", "222222")
linux.add_group("admins", "manage the system")
linux.add_group("lp", "control the printer")
linux.add_group("scanner", "control the scanner")
print(linux.get_users())
print(linux.get_groups())
print(linux.get_passwords())
linux.del_user("pepe", "654321")
print(linux.get_users())
print(linux.del_group("matraca"))
linux.del_group("scanner")
print(linux.get_groups())
