"""
Wi-Fi scanner module using system tools.
"""

import subprocess
import logging
from typing import List, Optional, Dict, Any
from pathlib import Path

logger = logging.getLogger(__name__)

class WiFiScanner:
    """Wi-Fi scanner using safe system tools."""
    
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.interface = None
    
    def detect_interface(self) -> Optional[str]:
        """Auto-detect available wireless interface."""
        if self.dry_run:
            logger.info("DRY-RUN: Would detect wireless interface")
            return "wlan0"  # Mock interface for dry run
        
        try:
            # Try nmcli first (NetworkManager)
            result = subprocess.run(
                ["nmcli", "device", "status"], 
                capture_output=True, 
                text=True, 
                timeout=10
            )
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if 'wifi' in line.lower() and 'connected' in line.lower():
                        interface = line.split()[0]
                        logger.info(f"Detected interface via nmcli: {interface}")
                        return interface
            
            # Fallback to iwconfig
            result = subprocess.run(
                ["iwconfig"], 
                capture_output=True, 
                text=True, 
                timeout=10
            )
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if 'IEEE 802.11' in line:
                        interface = line.split()[0]
                        logger.info(f"Detected interface via iwconfig: {interface}")
                        return interface
            
            # Fallback to ip link
            result = subprocess.run(
                ["ip", "link", "show"], 
                capture_output=True, 
                text=True, 
                timeout=10
            )
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if 'wlan' in line or 'wifi' in line:
                        interface = line.split(':')[1].strip().split(':')[0]
                        logger.info(f"Detected interface via ip link: {interface}")
                        return interface
                        
        except (subprocess.TimeoutExpired, FileNotFoundError) as e:
            logger.error(f"Error detecting interface: {e}")
        
        return None
    
    def scan_networks(self, interface: Optional[str] = None) -> str:
        """Scan for Wi-Fi networks."""
        if not interface:
            interface = self.detect_interface()
        
        if not interface:
            raise RuntimeError("No wireless interface detected")
        
        self.interface = interface
        
        if self.dry_run:
            logger.info(f"DRY-RUN: Would scan networks on {interface}")
            return self._get_mock_scan_output()
        
        try:
            # Use iwlist for scanning
            result = subprocess.run(
                ["iwlist", interface, "scanning"], 
                capture_output=True, 
                text=True, 
                timeout=30
            )
            
            if result.returncode != 0:
                logger.error(f"iwlist failed: {result.stderr}")
                raise RuntimeError(f"Scan failed: {result.stderr}")
            
            logger.info(f"Successfully scanned networks on {interface}")
            return result.stdout
            
        except subprocess.TimeoutExpired:
            logger.error("Scan timeout - interface may be busy")
            raise RuntimeError("Scan timeout")
        except FileNotFoundError:
            logger.error("iwlist not found - install wireless-tools")
            raise RuntimeError("iwlist command not available")
    
    def scan_from_file(self, file_path: str) -> str:
        """Load scan data from file (sandbox mode)."""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Sample file not found: {file_path}")
        
        logger.info(f"Loading scan data from file: {file_path}")
        return path.read_text(encoding='utf-8')
    
    def _get_mock_scan_output(self) -> str:
        """Return mock scan output for dry-run mode."""
        return """
Cell 01 - Address: 00:11:22:33:44:55
                    ESSID:"TestNetwork1"
                    Protocol:IEEE 802.11bgn
                    Mode:Master
                    Frequency:2.437 GHz (Channel 6)
                    Encryption key:on
                    Bit Rates:54 Mb/s
                    Extra:rsn_ie=30140100000fac040100000fac040100000fac020000
                    IE: IEEE 802.11i/WPA2 Version 1
                        Group Cipher : CCMP
                        Pairwise Ciphers (1) : CCMP
                        Authentication Suites (1) : PSK
                    Quality=70/70  Signal level=-30 dBm  
                    Extra:fm=0001

Cell 02 - Address: aa:bb:cc:dd:ee:ff
                    ESSID:"OpenNetwork"
                    Protocol:IEEE 802.11bgn
                    Mode:Master
                    Frequency:2.462 GHz (Channel 11)
                    Encryption key:off
                    Bit Rates:54 Mb/s
                    Quality=50/70  Signal level=-45 dBm
"""