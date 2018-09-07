import threading
import datetime
import scan


class myThread(threading.Thread):
    def __init__(self, ip, start_ip, end_ip):
        threading.Thread.__init__(self)
        self.ip = ip
        self.start_ip = start_ip
        self.end_ip = end_ip

    def run(self):
        scan.scan_for_devices(self.ip, self.start_ip, self.end_ip)


def get_avail_hosts():
    ip, subnet = scan.get_adapters()
    avail_host = int((2 ** (32 - int(subnet))))
    # print(avail_host)
    avail = int(avail_host / 4)
    # print(avail)

    start_end_ip = []
    value = 0
    count = 0
    while value < (avail_host-2):
        start_ip = count * avail
        end_ip = start_ip + (avail - 1)
        if end_ip > avail_host-1:
            end_ip = avail_host-1
        start_end_ip.append((start_ip, end_ip))
        count = count + 1
        value = end_ip

    print(start_end_ip)
    return ip, start_end_ip


if __name__ == "__main__":
    threads = []
    count = 0
    ip, start_end_ips = get_avail_hosts()

    print("\nStart Time: " + str(datetime.datetime.now()))
    print("Scanning for available devices in network...")
    print("Available Networks:")

    for start_end_ip in start_end_ips:
        thread_name = "Thread " + str(count + 1)
        thread = myThread(ip, start_end_ip[0], start_end_ip[1])
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

    print("Exiting Main Thread")
    print("Scan ended.")
    print("End Time: " + str(datetime.datetime.now()))
