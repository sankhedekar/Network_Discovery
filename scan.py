import ifaddr
import socket
import errno


def is_connected(host_ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(3)
        result = s.connect_ex((host_ip, 80))
        # print(result)
        if result == 0:
            print(host_ip)
        # msg = errno.errorcode[result]
        s.close()

    except Exception as e:
        pass


def get_adapters():
    adapters = ifaddr.get_adapters()
    count = 0
    networks = []
    for adapter in adapters:
        for ip in adapter.ips:
            count = count + 1
            networks.append((str(count), str(adapter.nice_name), str(ip.ip), str(ip.network_prefix)))

    print(adapters)
    print(networks)

    print("Available network adapters: ")
    for network in networks:
        print(' - '.join(network))

    number = input("\nSelect network adapter to scan: ")
    for network in networks:
        if str(network[0]) == str(number):
            print("You selected: ", ' - '.join(network))
            return network[2], network[3]

    print("Network adapter not available.")
    return 0, 0


def scan_for_devices(ip, start_ip, end_ip):
    nw = ip.split(".")
    nw.pop(-1)
    nw_addr = ".".join(nw)

    for i in range(start_ip, end_ip):
        host_ip = nw_addr + "." + str(i)
        is_connected(host_ip)
