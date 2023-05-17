from __future__ import annotations

'''Manipulación de IPs en hosts sobre redes de ordenadores'''


class Host:
    IPV4_BITS = 32
    # ↓ Contiene: [0, 8, 16, 24, 32]
    IPV4_SLICES = list(range(0, IPV4_BITS + 1, 8))

    def __init__(self, *args: str | int, mask: int):
        '''
        Constructor de un Host
        ======================
        - Si el primer argumento de args es un string, se supondrá que es una IP en formato
          de cadena de texto. Ejemplo: '192.168.1.5'
        - Si args es una tupla indica que vienen una serie de octetos de la dirección. Se
          rellenarán los octetos faltantes (si es que faltan) con ceros. Ejemplo: (192, 168, 1, 5)
        - Si la máscara está fuera de rango habrá que elevar una excepción de dirección IP
          indicando en el mensaje: "Mask is out of range". Ejemplo: mask=33
        - Si nos pasan un número de octetos distinto de 4, habrá que elevar una excepción de
          dirección IP con el mensaje: "Only 4 octets are allowed"
        - Hay que crear los atributos "ip_octets" (tupla) y mask (entero).
          Ejemplo:
            - ip_octets = (192, 168, 1, 5)
            - mask = 24
        '''
        items = list(args)
        if isinstance(items[0], str):
            if len(items) > 4:
                raise IPAddressError("IP address is invalid: Only 4 octets are allowed")
            self.ip_octets = tuple(int(i) for i in items[0].split('.'))
        
        if isinstance(items[0], int):
            self.ip_octets = tuple(items[:4])
            if len(items) < 4:
                zeros = ['0'] * (4 - len(items))
                zeros_int = [int(i) for i in zeros]
                self.ip_octets = tuple(items + zeros_int)
            if len(items) > 4:
                raise IPAddressError("IP address is invalid: Only 4 octets are allowed")
        if mask < 0 or mask > Host.IPV4_BITS:
            raise IPAddressError("IP address is invalid: Mask is out of range")
        self.mask = mask

    @property
    def ip(self) -> str:
        '''Devuelve la IP del host en formato string.
        Ejemplo: "192.168.1.5"'''
        return '.'.join(str(i) for i in self.ip_octets)

    @property
    def bip(self) -> str:
        '''Devuelve la IP en formato binario. Ojo que cada octeto debe tener 8 bits.
        Ejemplo: "11000000101010000000000100000101"'''
        return ''.join(f'{int(octet):08b}' for octet in self.ip_octets)

    @property
    def addr_bmask(self) -> str:
        '''Devuelve la parte de la dirección que representa la máscara (en binario).
        Ejemplo: "110000001010100000000001"'''
        return self.bip[:self.mask]

    @property
    def addr_bhost(self) -> str:
        '''Devuelve la parte de la dirección que representa el host (en binario).
        Ejemplo: "00000101"'''
        return self.bip[self.mask:]


    @property
    def has_network_addr(self) -> bool:
        '''Indica si la dirección IP corresponde con la dirección de red.
        En una dirección de red, la parte de host de la IP tiene todos los bits a 0.
        Ejemplo: "192.168.1.0"'''
        nh_index  = self.mask // 8
        return self.ip_octets[nh_index] == 0

    @property
    def has_broadcast_addr(self) -> bool:
        '''Indica si la dirección IP corresponde con la dirección de broadcast.
        En una dirección de broadcast, la parte de host de la IP tiene todos los bits a 1.
        Ejemplo: "192.168.1.255"'''
        nh_index  = self.mask // 8
        return self.ip_octets[nh_index] == 255

    @property
    def nclass(self):
        '''Devuelve la clase de la red: A, B o C.
        → Ver https://bit.ly/42Pgm2k'''
        if self.mask <= 8:
            return "A"
        if 9 <= self.mask <= 16:
            return "B"
        if 17 <= self.mask <= 24:
            return "C"

    @property
    def addr_host_size(self) -> int:
        '''Devuelve el número de bits que ocupa la parte de host en la dirección'''
        return Host.IPV4_BITS - self.mask

    @property
    def num_hosts(self) -> int:
        '''Devuelve el número de hosts que pueden haber en la red.
        Para calcular la cantidad de hosts por red, se usa la fórmula 2^n - 2
        donde n corresponde a la cantidad de bits para hosts.'''
        return 2 ** (Host.IPV4_BITS - self.mask) - 2

    def ping(self, host: Host) -> bool:
        '''Indica si un host puede hacer ping a otro host.
        Para que dos hosts puedan hacer ping deben estar en la misma red.'''
        return self.mask == host.mask

    def __repr__(self):
        '''Devuelve la representación del host en formato.
        Ejemplo: "192.168.1.5/24"'''
        buffer = ".".join(str(i) for i in self.ip_octets)
        return f'{buffer}/{self.mask}'

    def __eq__(self, other: Host | object):
        '''Indica si dos hosts tienen la misma dirección IP (incluyendo máscara)'''
        if isinstance(other, Host):
            return self.ip_octets == other.ip_octets and self.mask == other.mask
        return False

    def __iter__(self):
        '''Devuelve el iterador para el Host'''
        return NetworkIter(self)

    @classmethod
    def from_bip(cls, bip: str, mask: int) -> Host:
        '''Crea un host a partir de una dirección IP binaria y una máscara.
        - Por ejemplo: bip='10010100101000111101010101110101' y mask=8 debería crear el host:
          148.163.213.117/8
        - Si se pasan más de 32 bits hay que lanzar una excepción de dirección incorrecta
          indicando en el mensaje: "Binary address is too long"
        '''
        if len(bip) > 32:
            raise IPAddressError("IP address is invalid: Binary address is too long")
        splited_bip = ".".join(bip[i:i+8] for i in range(0, len(bip), 8))
        ip = '.'.join(str(int(octet,2)) for octet in splited_bip.split('.'))
        return Host(ip,mask=mask)        


class IPAddressError(Exception):
    '''Clase que representa un error en la dirección IP.
    - Mensaje por defecto: IP address is invalid
    - Si pasamos un mensaje: IP address is invalid: <message>'''
    def __init__(self, message: str = ''):
        base_message = "IP address is invalid"
        if message:
            base_message += f': {message}'
        super().__init__(base_message)


class NetworkIter:
    def __init__(self, host: Host):
        self.host = host
        self.counter = 0
        # En self.host_bip_segments tendremos todas las combinaciones binarias para la parte
        # de host de la dirección. Por ejemplo, para una IP con máscara 24, tenemos 8 bits
        # para el host, por tanto en self.host_bip_segments tendremos:
        # [[0, 0, 0, 0, 0, 0, 0, 0],
        #  [0, 0, 0, 0, 0, 0, 0, 1],
        #  [0, 0, 0, 0, 0, 0, 1, 0],
        #  [0, 0, 0, 0, 0, 0, 1, 1],
        #  [0, 0, 0, 0, 0, 1, 0, 0],
        #  ...
        #  [1, 1, 1, 1, 1, 1, 1, 0],
        #  [1, 1, 1, 1, 1, 1, 1, 1]]
        # ¡Ojo que es un generador!
        self.host_bip_segments = NetworkIter.comb((0, 1), self.host.addr_host_size)

    def __next__(self):
        '''Genera el siguiente host dentro de la subred en la que se encuentra el host original.
        - Hay que dejar fuera el host que representa la red.
        - Hay que dejar fuera el host que representa el broadcast.
        '''
        self.counter += 1


    @staticmethod
    def comb(values, n):
        '''Genera todas las combinaciones de "values" de tamaño "n"'''

        def comb_helper(items, k=0):
            if k == n:
                yield items.copy()
            else:
                for v in values:
                    items[k] = v
                    yield from comb_helper(items, k + 1)

        return comb_helper([None] * n)