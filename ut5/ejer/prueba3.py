input_ip = '172.140.35.10/26'
ip, cidr = input_ip.split('/')
bits_in_octet = 8
bits_in_ip = bits_in_octet * 4
octets_ones = '.'.join(['1' * 8] * 4)
octets_ceros = '.'.join(['0' * 8] * 4) 

binary_ip = '.'.join([f'{int(octet):08b}' for octet in ip.split('.')])
nsh_index = int(cidr) + (int(cidr) // 8)
network_part = binary_ip[:nsh_index]
host_part = binary_ip[nsh_index:]
binary_id_red = network_part + '0'
decimal_id_red = '.'.join(str(int(octet,2)) for octet in binary_id_red.split('.'))
binary_broadcast = network_part + octets_ones[nsh_index:]
decimal_broadcast = '.'.join(str(int(octet,2)) for octet in binary_broadcast.split('.'))
binary_mask = octets_ones[:nsh_index] + octets_ceros[nsh_index:]
decimal_mask = '.'.join(str(int(octet,2)) for octet in binary_mask.split('.'))

def nh_index(cidr: int):
    return cidr + (cidr // bits_in_octet)

def binary_2_decimal(octets: str):
    return '.'.join(str(int(octet,2)) for octet in octets.split('.'))
    
def decimal_2_binary(octets: str):
    return '.'.join([f'{int(octet):08b}' for octet in octets.split('.')])

def get_number_hosts(cidr: int):
        if cidr in (31, 32):
            return 2 ** (32 - cidr)
        return 2 ** (32 - cidr) - 2
        
print(binary_ip)
print(cidr)
print(ip)
print(decimal_id_red)
print(decimal_broadcast)
print(decimal_mask)