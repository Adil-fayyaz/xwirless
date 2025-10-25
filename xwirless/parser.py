"""
Wi-Fi parser module with Pydantic models.
"""

import re
import logging
from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field, validator

logger = logging.getLogger(__name__)

class WiFiNetwork(BaseModel):
    """Wi-Fi network information model."""
    
    bssid: str = Field(..., description="MAC address of the access point")
    ssid: str = Field(..., description="Network name")
    channel: int = Field(..., description="Wi-Fi channel")
    frequency: float = Field(..., description="Frequency in GHz")
    signal_level: int = Field(..., description="Signal level in dBm")
    quality: str = Field(..., description="Signal quality")
    encryption: str = Field(default="Open", description="Encryption type")
    cipher: Optional[str] = Field(default=None, description="Cipher suite")
    authentication: Optional[str] = Field(default=None, description="Authentication method")
    mode: str = Field(default="Master", description="AP mode")
    protocol: str = Field(default="IEEE 802.11", description="Protocol version")
    
    @validator('bssid')
    def validate_bssid(cls, v):
        """Validate MAC address format."""
        mac_pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
        if not re.match(mac_pattern, v):
            raise ValueError('Invalid MAC address format')
        return v.upper().replace('-', ':')
    
    @validator('signal_level')
    def validate_signal_level(cls, v):
        """Validate signal level range."""
        if v > 0 or v < -100:
            logger.warning(f"Unusual signal level: {v} dBm")
        return v

class ScanResult(BaseModel):
    """Complete scan result model."""
    
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    interface: str = Field(..., description="Network interface used")
    networks: List[WiFiNetwork] = Field(default_factory=list)
    total_networks: int = Field(default=0)
    scan_duration: Optional[float] = Field(default=None, description="Scan duration in seconds")
    
    def __init__(self, **data):
        super().__init__(**data)
        self.total_networks = len(self.networks)

class WiFiParser:
    """Parser for iwlist scan output."""
    
    def __init__(self):
        self.networks: List[WiFiNetwork] = []
    
    def parse_scan_output(self, output: str, interface: str) -> ScanResult:
        """Parse iwlist scan output into structured data."""
        logger.info("Parsing scan output...")
        
        networks = []
        cells = self._split_cells(output)
        
        for cell in cells:
            try:
                network = self._parse_cell(cell)
                if network:
                    networks.append(network)
            except Exception as e:
                logger.warning(f"Failed to parse cell: {e}")
                continue
        
        logger.info(f"Parsed {len(networks)} networks")
        
        return ScanResult(
            interface=interface,
            networks=networks,
            timestamp=datetime.utcnow()
        )
    
    def _split_cells(self, output: str) -> List[str]:
        """Split output into individual cell blocks."""
        # Split by "Cell XX - Address:"
        pattern = r'Cell \d+ - Address:'
        cells = re.split(pattern, output)
        
        # Remove empty first element and reconstruct cells
        if cells and not cells[0].strip():
            cells = cells[1:]
        
        # Reconstruct cell blocks
        reconstructed_cells = []
        cell_addresses = re.findall(pattern, output)
        
        for i, cell_content in enumerate(cells):
            if i < len(cell_addresses):
                reconstructed_cells.append(cell_addresses[i] + cell_content)
        
        return reconstructed_cells
    
    def _parse_cell(self, cell: str) -> Optional[WiFiNetwork]:
        """Parse individual cell data."""
        try:
            # Extract BSSID
            bssid_match = re.search(r'Address: ([0-9A-Fa-f:]{17})', cell)
            if not bssid_match:
                return None
            bssid = bssid_match.group(1)
            
            # Extract SSID
            ssid_match = re.search(r'ESSID:"([^"]*)"', cell)
            ssid = ssid_match.group(1) if ssid_match else "Hidden"
            
            # Extract channel and frequency
            channel_match = re.search(r'Channel (\d+)', cell)
            channel = int(channel_match.group(1)) if channel_match else 0
            
            freq_match = re.search(r'(\d+\.\d+) GHz', cell)
            frequency = float(freq_match.group(1)) if freq_match else 0.0
            
            # Extract signal level
            signal_match = re.search(r'Signal level=(-?\d+) dBm', cell)
            signal_level = int(signal_match.group(1)) if signal_match else -100
            
            # Extract quality
            quality_match = re.search(r'Quality=(\d+/\d+)', cell)
            quality = quality_match.group(1) if quality_match else "0/70"
            
            # Determine encryption
            encryption = "Open"
            cipher = None
            authentication = None
            
            if "Encryption key:on" in cell:
                if "WPA2" in cell or "rsn_ie" in cell:
                    encryption = "WPA2"
                elif "WPA" in cell:
                    encryption = "WPA"
                elif "WEP" in cell:
                    encryption = "WEP"
                elif "WPA3" in cell:
                    encryption = "WPA3"
                
                # Extract cipher information
                if "CCMP" in cell:
                    cipher = "CCMP"
                elif "TKIP" in cell:
                    cipher = "TKIP"
                
                # Extract authentication
                if "PSK" in cell:
                    authentication = "PSK"
                elif "EAP" in cell:
                    authentication = "EAP"
            
            # Extract protocol
            protocol_match = re.search(r'Protocol:(IEEE 802\.11[a-z]*)', cell)
            protocol = protocol_match.group(1) if protocol_match else "IEEE 802.11"
            
            return WiFiNetwork(
                bssid=bssid,
                ssid=ssid,
                channel=channel,
                frequency=frequency,
                signal_level=signal_level,
                quality=quality,
                encryption=encryption,
                cipher=cipher,
                authentication=authentication,
                mode="Master",
                protocol=protocol
            )
            
        except Exception as e:
            logger.error(f"Error parsing cell: {e}")
            return None