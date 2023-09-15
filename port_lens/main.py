import socket
import sys
import os
import time
import argparse

__version__ = "0.4"


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    clear_screen()

    line = '+' * 80

    description = line + '''\n\nA Simple port scanner that works!! (c) digitz.org Example usage: 
    python port_scanner.py example.com 1 1000
    The above example will scan the host 'example.com' from port 1 to 1000
    To scan most common ports, use: python port_scanner.py example.com\n\n''' + line + "\n"

    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('host', metavar='H', help='Host name you want to scan')
    parser.add_argument('startport', metavar='P1', nargs='?', help='Start scan from this point.')
    parser.add_argument('endport', metavar='P2', nargs='?', help='Scan until this port')

    args = parser.parse_args()

    host = args.host
    ip = socket.gethostbyname(host)

    if args.startport and args.endport:
        start_port = int(args.startport)
        end_port = int(args.endport)
    else:
        start_port = 20
        end_port = 1000

    open_ports = []

    common_ports = {
        21: 'FTP',
        22: 'SSH',
        # ... (other common ports) ...
        10000: 'VIRTUALMIN/WEBMIN'
    }

    starting_time = time.time()
    print('-' * 40)
    print('\tSimple Port Scanner..!!')
    print('-' * 40)

    print(f'Scanning {host} from port {start_port} - {end_port}: ')
    print(f'Scanning start at {time.strftime("%I:%M:%S %p")}')

    def check_port(host, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            sock.close()
            return result
        except Exception as e:
            print('Error!', e)
            return 1

    def check_services(port):
        if port in common_ports:
            return common_ports[port]
        else:
            return 'Unknown Service'

    try:
        print('Scanning in progress..')
        print('Connecting to port')

        for p in range(start_port, end_port + 1):
            sys.stdout.flush()
            print(p)
            response = check_port(host, p)
            if response == 0:
                open_ports.append(p)
                sys.stdout.write('\b' * len(str(p)))

        print("\nScanning completed at {time.strftime('%I:%M:%S %p')}")
        ending_time = time.time()
        total_time = ending_time - starting_time

        print('*' * 40)
        print('\tScanning Report..')
        print('*' * 40)

        if total_time < 60:
            print(f'Scan took {total_time:.2f} seconds')
        else:
            total_time = total_time / 60
            print(f'Scan took {total_time:.2f} minutes')

        if open_ports:
            print('Open Ports')
            for j in sorted(open_ports):
                service = check_services(j)
                print(f'\t{j} {service}')
        else:
            print('No open ports found.')

    except KeyboardInterrupt:
        print('You pressed Ctrl + C. Exiting..')
        sys.exit(1)
