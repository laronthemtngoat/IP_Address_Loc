import socket
import subprocess
import csv
from tempfile import NamedTemporaryFile
import shutil

data_pairs = {}


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def get_ip_config():
    process = subprocess.check_output("ipconfig", encoding='oem')
    return process


def get_host_name():
    h_name = subprocess.check_output("hostname", encoding='oem')
    return h_name


# associates machine and IP address. replaces IP address with current IP whenever this is run.
def add_pairs():
    data_pairs[host_name] = ip_address


def create_table():
    html = """<html><table border="1"><tr><th>Computer Name</th><th>IP Address</th></tr>"""
    for machine, ip in iter(data_pairs.items()):
        html += "<tr><td>{}</td>".format(machine)
        html += "<td>{}</td>".format(ip)
        html += "</tr>"
    html += "</table></html>"
    return html


# assigns computer name to variable
host_name = str(get_host_name()).rstrip('\n')
# assigns IPV4 address to variable
ip_address = get_ip_address()
# adds computer name, ip address pair to dictionary
add_pairs()
# creates table with dictionary pairs
web_page = create_table()

# creates table in html document; file path may change
file_ = open('IPLog.htm', 'w')
file_.write(web_page)
file_.close()

