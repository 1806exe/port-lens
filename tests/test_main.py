import pytest
from unittest.mock import patch
from io import StringIO
import port_scanner  # Assuming your code is in a module named port_scanner

# Define a test case for the port scanning function
def test_scan_ports():
    open_ports = port_scanner.scan_ports("example.com", 1, 1000)
    assert isinstance(open_ports, list)

# Define a test case for the port scanner's argument parsing
def test_argument_parsing():
    with patch("sys.argv", ["port_scanner.py", "example.com", "1", "1000"]):
        args = port_scanner.parse_arguments()
        assert args.host == "example.com"
        assert args.startport == "1"
        assert args.endport == "1000"

# Define a test case for the port scanner's display functions
def test_display_functions(capsys):
    port_scanner.display_banner()
    out, _ = capsys.readouterr()
    assert "Simple Port Scanner" in out

# Define a test case for the port scanner's port checking function
def test_check_port():
    result = port_scanner.check_port("example.com", 80)
    assert isinstance(result, int)

# Define a test case for the port scanner's service checking function
def test_check_services():
    service = port_scanner.check_services(80)
    assert isinstance(service, str)

# Define a test case for the port scanner's main function (example of testing user input)
def test_main_function(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["port_scanner.py", "example.com", "1", "1000"])
    
    with patch("time.sleep"):
        port_scanner.main()
        out, _ = capsys.readouterr()
        assert "Scanning completed" in out

if __name__ == "__main__":
    pytest.main()
