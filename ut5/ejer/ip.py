from __future__ import annotations

def load_ip(path: str = 'ip.dat') -> str:   
    return open(path).read()

class IP:
    
    def __init__(self, ip: str):
        ip, cidr = input_ip.split("/")
        ip_list = [int(i) for i in ip.split(".")]
        for octeto in ip_list:
            if octeto < 0 or octeto < 255:
                raise InvalidIPError(f"{repr(octeto)} is not a supported value")
        self.ip = ip_list
        self.cidr = int(cidr)
    
    def get_number_hosts(self):
        if self.cidr == 31:
            return 2
        if self.cidr == 32:
            return 1
        num_hosts = 2 ** (32 - self.cidr) - 2
        print(f"The number of hosts is: {num_hosts}")
        
    def unmask(self):
        ...

    def __str__(self) -> str:
        pass
    def __repr__(self) -> str:
        pass
    def __eq__(self, other: IP | object) -> bool:
        pass
    def __lt__(self, other: IP) -> bool:
        pass
    def __gt__(self, other: IP) -> bool:
        pass
    def __add__(self, other: IP) -> IP:
        pass
        
class InvalidIPError(Exception):
    def __init__(self, message: str = ""):
        self.message = "Invalid ip"
        if message:
            self.message += f": {message}"
        super().__init__(message)


ip1 = IP("172.140.35.10")
print(load_ip())
input_ip = "172.140.35.10/26"
ip_list = [int(i) for i in ip.split(".")]
print(ip_list)