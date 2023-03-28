class OS:
    def __init__(
        self,
        name: str,
        version: str,
        developer: str,
        kernel_type: str,
        system_file: str,
        ip: str,
        xserver: str,
    ) -> None:
        self.name = name
        self.version = version
        self.developer = developer
        self.system_file = system_file
        self.kernel_type = kernel_type
        self.booted = False
        self.updated = False
        self.upgraded = False
        self.ip = "172.18.99.202"
        self.xserver = xserver
        self.users_info = {}
        
    def switch_boot(self):
        self.booted = not self.booted
    
    def update(self):
        self.updated = not self.updated      
        
    def upgrade(self):
        self.upgraded = not self.upgraded  
        
    def get_ip(self) -> str:
        return self.ip
    
    # Esto puede ser un decorador?
    def check_info_users(self, name: str, password: str) -> tuple[bool, str]:
        
        for name, password in self.users_info.items():          
            if name in self.users_info and password in self.users_info:
                return False, "Error, usuario o contraseña ya existen, pruebe a modificarlos"
        return True, "Parámetros correctos, el usuario o contraseña no existan"
    
    
    def modify_users(self, name: str) -> tuple[bool, str]:
        error, message = self 
        
        
        return True, "Usuario modificado"
    

        
        
    def if_updated(self):
        
    def if_upgraded(self):
        
    def create_user(self, name: str, password: str) -> tuple:
            self.users_info[name] = password
            return (True,'Se crea el usuario')
        else:
            return (False,'Erro usuario o contraseña ya existen')

    def delete_user(self, name: str):

    def intall_aplication(self):
        
    def uninstall_aplication(self):
        
    def start_service(self):
        
    def stop_service(self):
        
    