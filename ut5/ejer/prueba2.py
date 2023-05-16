# class IP:
#     def __init__(self, ip: str, cidr: str):
#         for oct in ip.split("."):
#             if int(oct) < 0 or int(oct) > 255:
#                 raise RangeError('Valor fuera de rango')
            
#         self.ip = ip
#         self.cidr = cidr.strip('/')

#     @property
#     def binary_ip(self):
#         return ".".join([f'{int(octeto):08b}' for octeto in self.ip.split(".")]) 
    
#     @property
#     def mask(self):
#         cidr = int(self.cidr)
#         mask = []
#         for octeto in self.binary_ip.split("."):
#             if cidr >= len(octeto) :
#                 mask.append('1'*8)
#                 cidr -= 8
#             else: 
#                 mask.append(f'{"1"*cidr}{"0"*(8-cidr)}')
#         return ".".join(mask)
    
#     @property
#     def broadcasting(self):
#         host_part = self.binary_ip[self.mask.find('0'):]
#         return self.binary_ip[:self.mask.find("0")] + host_part.replace('0','1')
    
#     @property
#     def red(self):
#         host_part = self.binary_ip[self.mask.find('0'):]
#         return self.binary_ip[:self.mask.find("0")] + host_part.replace('1','0')
    
#     @staticmethod
#     def binary2dec(binary):
#         return ".".join([str(int(octeto,2)) for octeto in binary.split(".")])
    
#     def __eq__(self,other):
#         return self.binary_ip == other.binary_ip
    
#     def __lt__(self,other):
#         return self.cidr < other.cidr
    
#     def __gt__(self,other):
#         return self.cidr > other.cidr
    
#     def __repr__(self):
#         return f'Binary: {self.binary_ip}\nRealIP: {self.ip}\nBD {self.broadcasting} {IP.binary2dec(self.broadcasting)}\nIDRED {self.red} {IP.binary2dec(self.red)}'
    
#     def __iter__(self):
#         return IPIterator(self)

# class IPIterator:
#     def __init__(self, ip):
#         self.ip = ip.ip.split(".")
#         self.pointer = 0
    
#     def __next__(self):
#         if self.pointer > len(self.ip) - 1:
#             raise StopIteration
#         current_oct = self.ip[self.pointer]
#         self.pointer += 1
#         return current_oct

# class RangeError(Exception):
#     def __init__(self,message):
#         self.message = message
#         super().__init__(self.message)

# ip1 = IP('-1.80.5.125','/27')

# for oct in ip1:
#     print(oct)

# numero_decimal = 29

# modulos = []
# while numero_decimal != 0:
#     # se almacena el módulo en el orden correcto
#     modulos.insert(0, numero_decimal % 2)
#     numero_decimal //= 2

# print(modulos)

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
        self.cidr = cidr
    
    def unmask(self):
        ...
        
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