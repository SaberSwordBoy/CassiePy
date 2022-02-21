import scapy.all as scapy
import rich
from rich import print
from rich.console import Console

NAME = "netscraper"
DESCRIPTION = "Scan local IP addresses, prints online IPs and MAC addesses"

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=0.25, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def run():
    """Scans IP Range 0-256"""
    console = Console()
    print("IP" + "\t\t\t" + "MAC")
    for i in range(0, 256):
        try:
            curr_ip = "192.168.1." + str(i)
            with console.status(f"Scanning {curr_ip}", spinner="point") as status:
                scan_result = scan(curr_ip)
            if scan_result:
                print('[green]'+ scan_result[0]['ip'] + "[/green]"+ "\t\t[blue]" + scan_result[0]['mac']+'[/blue]')
        except KeyboardInterrupt:
            exit()

