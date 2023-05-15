class OS:
    graphical_interface = True
    ip = "172.18.99.202/16"

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
        self.processes = []
        self.ip = OS.ip
        self.cidr = int(self.ip.split("/")[-1])
        self.load = 0

    @staticmethod
    def get_os_categories() -> list[str]:
        return ["Multitask", "Multiuser", "Multiprocess"]

    @staticmethod
    def audit(method):
        def wrapper(self, *args, **kwargs):
            print(
                f"Operation System {self.name} version {self.version} running {method.__name__}"
            )
            return method(self, *args, **kwargs)

        return wrapper

    @audit
    def get_subnet_mask(self) -> str:
        subnet_mask = []
        bin_subnet_mask = ("1" * self.cidr) + ("0" * (32 - self.cidr))
        for i in range(0, 32, 8):
            decimal_num = int(bin_subnet_mask[i : i + 8], 2)
            subnet_mask.append(str(decimal_num))
        return ".".join(subnet_mask)

    @audit
    def get_wildcard_mask(self) -> str:
        wildcard_mask = []
        bin_wildcard_mask = ("0" * self.cidr) + ("1" * (32 - self.cidr))
        for i in range(0, 32, 8):
            decimal_num = int(bin_wildcard_mask[i : i + 8], 2)
            wildcard_mask.append(str(decimal_num))
        return ".".join(wildcard_mask)

    @audit
    def get_number_hosts(self):
        if self.cidr == 31:
            return 2
        if self.cidr == 32:
            return 1
        num_hosts = 2 ** (32 - self.cidr) - 2
        print(f"The number of hosts is: {num_hosts}")

    @audit
    def get_type_mask(self):
        if self.cidr <= 8:
            return "The mask type is: A"
        if 9 <= self.cidr <= 16:
            return "The mask type is: B"
        if 24 <= self.cidr <= 32:
            return "The mask type is: C"

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

    def execute_process(self, *processes: str):
        for process in processes:
            if process not in self.processes:
                self.processes.append(process)

    def kill_process(self, processes: list):
        for process in processes:
            if process in self.processes:
                self.processes.remove(process)

    def show_processes(self) -> list:
        return self.processes

    def get_os_info(self):
        return f"{self.name} version {self.version}"

    def get_users(self) -> list:
        return list(self.users_info.keys())

    def get_groups(self) -> dict:
        return self.groups_info

    def get_passwords(self) -> dict:
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


linux = OS("Linux Mint", "21.0", "Stallman", "monolithic hybrid", "system file", "xorg")
print(linux.get_os_info())
print(linux.get_subnet_mask())
print(linux.get_wildcard_mask())
linux.get_number_hosts()
print(linux.get_os_categories())
print(linux.get_type_mask())
linux.add_user("Alejandro", "123456")
linux.add_user("Pepe", "654321")
linux.add_user("Alejandro", "123456")
linux.add_user("Raquel", "222222")
linux.add_group("admins", "manage the system")
linux.add_group("lp", "control the printer")
linux.add_group("scanner", "control the scanner")
print(linux.get_users())
print(linux.get_groups())
print(linux.get_passwords())
linux.del_user("Pepe", "654321")
print(linux.get_users())
print(linux.del_group("matraca"))
linux.del_group("scanner")
print(linux.get_groups())
linux.execute_process("firefox", "xeyes", "chrome")
print(linux.show_processes())
linux.kill_process(["firefox", "xeyes"])
print(linux.show_processes())
