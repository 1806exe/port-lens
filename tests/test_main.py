"""
    Author: 1806exe
    Email: 1806exe@gmail.com
    GitHub: https://www.github.com/1806exe
"""

import pytest
from io import StringIO
import sys
import os

# Import the code you want to test
from port_lens.main import main  # Replace 'your_code_file' with the actual filename

def test_main(monkeypatch, capsys):
    args = ['google.com', '20', '30']  # Modify the arguments here
    monkeypatch.setattr(sys, 'argv', ['script_name'] + args)
    monkeypatch.setattr(os, 'system', lambda x: None)  # Mock the os.system function

    try:
        main()
        captured = capsys.readouterr()
        assert "Scanning completed" in captured.out  # Check for a completion message
    except SystemExit as e:
        assert e.code == 0

if __name__ == "__main__":
    pytest.main()
