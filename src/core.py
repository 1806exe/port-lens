import socket
import sys
import os
import time
import argparse

flag = 0

os.system('clear')      # clear the console window

line = '+' * 80

description = line + '''\n\nA Simple port scanner that works!! (c) digitz.org Example usage: 
python port_scanner.py example.com 1 1000
The above example will scan the host \'example.com\' from port 1 to 1000
To scan most common ports, use: python port_scanner.py example.com\n\n''' + line + "\n"


parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('host', metavar='H', help='Host name you want to scan')
parser.add_argument('startport', metavar='P1', nargs='?', help='Start scan from this point.')
parser.add_argument('endport', metavar='P2', nargs='?', help='Scan until this port')

args = parser.parse_args()

host = args.host        # the host used to scanned for open port
ip = socket.gethostbyname(host)     # get the ip address of the HOST!


# check if start port and end port defined else scan most common port!
if args.startport and args.endport:
    start_port = int(args.startport)
    end_port = int(args.endport)
else:
    # else scan most common port
    flag = 1

open_ports = []

# Dictionary contains most common port!
common_ports = {

    '21': 'FTP',
    '22': 'SSH',
    '23': 'TELNET',
    '25': 'SMTP',
    '53': 'DNS',
    '69': 'TFTP',
    '80': 'HTTP',
    '109': 'POP2',
    '110': 'POP3',
    '123': 'NTP',
    '137': 'NETBIOS-NS',
    '138': 'NETBIOS-DGM',
    '139': 'NETBIOS-SSN',
    '143': 'IMAP',
    '156': 'SQL-SERVER',
    '389': 'LDAP',
    '443': 'HTTPS',
    '546': 'DHCP-CLIENT',
    '547': 'DHCP-SERVER',
    '995': 'POP3-SSL',
    '993': 'IMAP-SSL',
    '2086': 'WHM/CPANEL',
    '2087': 'WHM/CPANEL',
    '2082': 'CPANEL',
    '2083': 'CPANEL',
    '3306': 'MYSQL',
    '8443': 'PLESK',
    '10000': 'VIRTUALMIN/WEBMIN'
}

# get time at which the scan was started
starting_time = time.time()
print('-' * 40)
print('\tSimple Port Scanner..!!')
print('-' * 40)

# starting ...

if flag:
    print('Scanning from most common ports on %s ' % (host,))   # means user did not provide any ports as argument
else:
    print('Scanning %s from port %s - %s: ' % (host, start_port, end_port))

print('Scanning start at %s' % (time.strftime("%I:%M:%S %p")))


# the devil function LOL!!
def check_port(host, port, result=1):

    try:
        # establish TCP connection
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        # set time out
        socket.setdefaulttimeout(0.5)

        # connect to the socket
        i = socket.create_connection(host, port)
        if i == 0:
            # this means the connection is closed:
            result = i
        sock.close()

    except Exception as e:

        print('Error!', e)

    return result


# Checks for the service name corresponding to a port.
def check_services(port):
    port = str(port)    # simple, convert int into string format

    # check if port is in common port dic
    if port in common_ports:
        # return the service name
        return common_ports[port]
    else:

        return 0
try:
    print('Scanning in progress..')
    print('Connecting to port')

    if flag:
        for p in sorted(common_ports):
            sys.stdout.flush()
            p = int(p)

            print(p)
            response = check_port(host, p)
            if response == 0:
                open_ports.append(p)
                # clear the port number displayed
                sys.stdout.write('\b' * len(str(p)))

    else:

        # user did not provide any port range so now we need to scan for that range!
        for p in range(start_port, end_port + 1):
            sys.stdout.flush()
            print(p)

            response = check_port(host, p)
            if response == 0:
                open_ports.append(p)        # append to the list of open port
                # clear the port number displayed
                sys.stdout.write('\b' * len(str(p)))

    print("\nScanning completed at %s" % (time.strftime("%I:%M:%S %p")))
    ending_time = time.time()

    # calculate the total time used to scanning the host.
    total_time = ending_time - starting_time

    print('*' * 40)
    print('\tScanning Report..')
    print('*' * 40)

    if total_time == 60:
        total_time = str(round(total_time, 2))
        print('Scan took %s Seconds' % total_time)

    else:
        total_time = total_time / 60
        print('Scan took %s minutes' % total_time)

    # means there are open ports available
    if open_ports:

        print('Open Ports')

        for j in sorted(open_ports):
            service = check_services(j)
            if not service:         # means the services not in our dictionary
                service = 'Unknown Service'
            print('\t%s %s' % (j, service))

    else:
        # no open port found
        print('Sorry!! no open port found.')

except KeyboardInterrupt:
    print('You press ctrl + c. Exiting..')
    sys.exit(1)
