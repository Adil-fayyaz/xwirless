"""
X WIRELESS - Wi-Fi Audit & Inventory Tool
=========================================

A comprehensive Wi-Fi auditing and inventory tool designed EXCLUSIVELY for 
educational purposes and testing on owned networks with written authorization.

Author: Adil Fayyaz
License: MIT
Version: 1.0.0

⚠️  LEGAL WARNING: This tool is for educational purposes only.
   Only use on networks you own or have explicit written permission to test.
"""

__version__ = "1.0.0"
__author__ = "Adil Fayyaz"
__email__ = "adilfayyaz388@gmail.com"
__license__ = "MIT"

from .scanner import WiFiScanner
from .parser import WiFiParser
from .report import ReportGenerator
from .db import InventoryDB
from .safety import SafetyValidator

__all__ = [
    "WiFiScanner",
    "WiFiParser", 
    "ReportGenerator",
    "InventoryDB",
    "SafetyValidator",
    "__version__",
    "__author__",
    "__email__",
    "__license__"
]