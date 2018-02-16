import socket
import textwrap
import struct

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t   '
DATA_TAB_2 = '\t\t   '
DATA_TAB_3 = '\t\t\t   '
DATA_TAB_4 = '\t\t\t\t   '

def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, ether_proto,data = ethernet_frame(raw_data)
        print('\nEthernet Frame')
        print(TAB_1 + 'Destination:{}, Source:{}, Protocol:{}'.format(dest_mac,src_mac,ether_proto))

        #8 for IPv4
        if ether_proto == 8:
            (version, header_lenght,ttl, proto, src, target,data) = ipv4_packet(data)
            print(TAB_1+'IPv4 Packet: ')
            print(TAB_2+'Version: {}, Header Lenght: {},TTL: {}'.format(version, header_lenght,ttl))
            print(TAB_2+'Protocol: {}, Source: {},Target: {}'.format(proto, src,target))



#Unpack Enthernet Frame
def ethernet_frame(data):
    dest_mac,src_mac,proto = struct.unpack('! 6s 6s H',data[:14])
    return get_mac_addr(dest_mac),get_mac_addr(src_mac),socket.htons(proto),data[14:]

#Return Properly formatted  MAC address (ie AA:BB:CC:DD:EE)

def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format,bytes_addr)
    byte = ':'.join(bytes_str).upper()
    return byte

#Unpacks ipv4
def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_lenght = (version_header_length & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', )
    return  version, header_lenght,ttl, proto, ipv4(src), ipv4(target),data[header_lenght:]

#Returns Properly formatted IPv4 Address
def ipv4(addr):
    ipv4_addr = '.'.join(map(str, addr))
    return ipv4_addr


#Unpack ICMP packet (Internet Control Message Protocol)

def icmp_packet(data):
    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]

#Unpacks TCP Segment
def tcp_segment(data):
    (src_port, dest_port,sequence, acknowledgement, offset_reserved_flags) = struct.unpack('! H H L L H',data[14:])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1

    return src_port, dest_port,sequence, acknowledgement, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data[offset:]

#Unpack UDP segment
def udp_segment(data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', data[8:])
    return src_port, dest_port, size, data[8:]

#Formats Multi-line data
def format_multi_line(prefix, string, size = 80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])


main()








