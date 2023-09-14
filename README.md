# PortScanner

A simple python port scanner which used to scanner open ports in a specific target.
 
## Installation

You can install PortLens using `pip`:

```bash
pip install port-lens
```

## Basic Usage

To perform a basic port scan, you can use PortLens with the following command:

```bash
port-lens scan <hostname> <start_port> <end_port>

```

## Scan Common Ports
If you want to scan common ports, you can omit the <start_port> and <end_port>:



```bash
port-lens scan example.com

```

## Display Help

To display the help message and see all available options, use:

```bash
port-lens --help
```

## Output
PortLens will display the results of the port scan, including open ports and their associated services. You will receive an informative report like this:
```mathematica
Scanning example.com from port 1 - 1000:

Open Ports:
    80 HTTP
    443 HTTPS
    ...

Scan completed in 2.34 seconds.
```

## Contributing
Contributions are welcome! If you encounter any issues, have feature requests, or want to contribute to the development of PortLens, please check our contribution guidelines.

## License
This project is licensed under the MIT License.

Happy scanning with PortLens! If you have any questions or need further assistance, please feel free to me.


