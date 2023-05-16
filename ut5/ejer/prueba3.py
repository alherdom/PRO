input_ip = "172.140.35.10/26"
ip, cidr = input_ip.split("/")
ip_list = [int(i) for i in ip.split(".")]
octets_ones = '.'.join(['1' * 8] * 4)
octets_ceros = '.'.join(['0' * 8] * 4) 

binary_ip = ".".join([f'{int(octet):08b}' for octet in ip_list])
nh_index = int(cidr) + (int(cidr) // 8)
network_part = binary_ip[:nh_index]
host_part = binary_ip[nh_index:]
binary_broadcast = network_part + octets_ones[nh_index:]
decimal_broadcast = '.'.join(str(int(octet,2)) for octet in binary_broadcast.split('.'))
binary_mask = octets_ones[:nh_index] + octets_ceros[nh_index:]
decimal_mask = '.'.join(str(int(octet,2)) for octet in binary_mask.split('.'))
print(ip_list)
print(ip)
print(cidr)
print(binary_ip)
print(binary_broadcast)
print(decimal_broadcast)
print(binary_mask)
print(decimal_mask)