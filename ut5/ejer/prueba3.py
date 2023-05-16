input_ip = '172.140.35.10/26'
ip, cidr = input_ip.split('/')
bits_in_octet = 8
bits_in_ip = bits_in_octet * 4
octets_ones = '.'.join(['1' * 8] * 4)
octets_ceros = '.'.join(['0' * 8] * 4) 

binary_ip = '.'.join(f'{int(octet):08b}' for octet in ip.split('.'))
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
    return '.'.join(f'{int(octet):08b}' for octet in octets.split('.'))

def get_number_hosts(cidr: int):
        return 2 ** (32 - cidr) if cidr in (31, 32) else 2 ** (32 - cidr) - 2

def from_mask_to_cidr(mask: str | list):
    if isinstance(mask, str):
        return decimal_2_binary(mask).count('1')
        
def highest_cidr(ip1: str, ip2: str):
    common_ip = ""
    binary_ip1 = decimal_2_binary(ip1)
    binary_ip2 = decimal_2_binary(ip2)
    for bit1, bit2 in zip(binary_ip1, binary_ip2):
        if bit1 != bit2:
            return len(common_ip.replace('.',''))
        common_ip += bit1

def get_type_mask(cidr: int):
        if cidr <= 8:
            return "A"
        if 9 <= cidr <= 16:
            return "B"
        if 17 <= cidr <= 24:
            return "C"
        if 25 <= cidr <= 32:
            return "D"
        
                    
# print(binary_ip)
# print(cidr)
# print(ip)
# print(decimal_id_red)
# print(binary_ip)
# print(decimal_broadcast)
# print(binary_broadcast)
# print(decimal_mask)
# print(decimal_2_binary('172.140.35.10'))
# print(decimal_2_binary('172.140.35.63'))
# print(highest_cidr('172.140.35.10','172.140.35.63'))
# print(from_mask_to_cidr('255.255.255.192'))
print(get_number_hosts(26))
print(get_type_mask(17))