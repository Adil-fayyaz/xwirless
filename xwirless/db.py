"""
Database module for inventory management.
"""

import json
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path

from .parser import ScanResult, WiFiNetwork

logger = logging.getLogger(__name__)

class InventoryDB:
    """Lightweight JSON-based inventory database."""
    
    def __init__(self, db_path: str = "xwirless_inventory.json"):
        self.db_path = Path(db_path)
        self.data = self._load_database()
    
    def _load_database(self) -> Dict[str, Any]:
        """Load database from file."""
        if self.db_path.exists():
            try:
                with open(self.db_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error loading database: {e}")
                return self._create_empty_db()
        else:
            return self._create_empty_db()
    
    def _create_empty_db(self) -> Dict[str, Any]:
        """Create empty database structure."""
        return {
            "version": "1.0",
            "created_at": datetime.utcnow().isoformat(),
            "last_updated": datetime.utcnow().isoformat(),
            "scans": [],
            "networks": {},
            "statistics": {
                "total_scans": 0,
                "unique_networks": 0,
                "last_scan_date": None
            }
        }
    
    def save_scan(self, scan_result: ScanResult) -> str:
        """Save scan result to database."""
        scan_id = f"scan_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"
        
        scan_data = {
            "id": scan_id,
            "timestamp": scan_result.timestamp.isoformat(),
            "interface": scan_result.interface,
            "total_networks": scan_result.total_networks,
            "scan_duration": scan_result.scan_duration,
            "networks": [network.dict() for network in scan_result.networks]
        }
        
        # Add to scans list
        self.data["scans"].append(scan_data)
        
        # Update networks inventory
        for network in scan_result.networks:
            bssid = network.bssid
            if bssid not in self.data["networks"]:
                self.data["networks"][bssid] = {
                    "first_seen": scan_result.timestamp.isoformat(),
                    "last_seen": scan_result.timestamp.isoformat(),
                    "ssid_history": [],
                    "signal_history": [],
                    "encryption_history": [],
                    "total_scans": 0
                }
            
            # Update network data
            network_data = self.data["networks"][bssid]
            network_data["last_seen"] = scan_result.timestamp.isoformat()
            network_data["total_scans"] += 1
            
            # Track SSID changes
            if network.ssid not in network_data["ssid_history"]:
                network_data["ssid_history"].append(network.ssid)
            
            # Track signal level
            network_data["signal_history"].append({
                "timestamp": scan_result.timestamp.isoformat(),
                "signal_level": network.signal_level,
                "quality": network.quality
            })
            
            # Track encryption changes
            if network.encryption not in network_data["encryption_history"]:
                network_data["encryption_history"].append(network.encryption)
        
        # Update statistics
        self.data["statistics"]["total_scans"] = len(self.data["scans"])
        self.data["statistics"]["unique_networks"] = len(self.data["networks"])
        self.data["statistics"]["last_scan_date"] = scan_result.timestamp.isoformat()
        self.data["last_updated"] = datetime.utcnow().isoformat()
        
        # Save to file
        self._save_database()
        
        logger.info(f"Scan saved with ID: {scan_id}")
        return scan_id
    
    def get_scan(self, scan_id: str) -> Optional[Dict[str, Any]]:
        """Get scan by ID."""
        for scan in self.data["scans"]:
            if scan["id"] == scan_id:
                return scan
        return None
    
    def get_all_scans(self) -> List[Dict[str, Any]]:
        """Get all scans."""
        return self.data["scans"]
    
    def get_network_history(self, bssid: str) -> Optional[Dict[str, Any]]:
        """Get network history by BSSID."""
        return self.data["networks"].get(bssid)
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get database statistics."""
        return self.data["statistics"]
    
    def compare_scans(self, scan_id_1: str, scan_id_2: str) -> Dict[str, Any]:
        """Compare two scans and highlight differences."""
        scan1 = self.get_scan(scan_id_1)
        scan2 = self.get_scan(scan_id_2)
        
        if not scan1 or not scan2:
            raise ValueError("One or both scan IDs not found")
        
        # Extract networks
        networks1 = {net["bssid"]: net for net in scan1["networks"]}
        networks2 = {net["bssid"]: net for net in scan2["networks"]}
        
        # Find differences
        bssids1 = set(networks1.keys())
        bssids2 = set(networks2.keys())
        
        new_networks = bssids2 - bssids1
        disappeared_networks = bssids1 - bssids2
        common_networks = bssids1 & bssids2
        
        # Check for changes in common networks
        changed_networks = []
        for bssid in common_networks:
            net1 = networks1[bssid]
            net2 = networks2[bssid]
            
            changes = []
            if net1["ssid"] != net2["ssid"]:
                changes.append(f"SSID: {net1['ssid']} → {net2['ssid']}")
            if net1["signal_level"] != net2["signal_level"]:
                changes.append(f"Signal: {net1['signal_level']} → {net2['signal_level']} dBm")
            if net1["encryption"] != net2["encryption"]:
                changes.append(f"Encryption: {net1['encryption']} → {net2['encryption']}")
            if net1["channel"] != net2["channel"]:
                changes.append(f"Channel: {net1['channel']} → {net2['channel']}")
            
            if changes:
                changed_networks.append({
                    "bssid": bssid,
                    "changes": changes
                })
        
        return {
            "scan1": scan_id_1,
            "scan2": scan_id_2,
            "scan1_timestamp": scan1["timestamp"],
            "scan2_timestamp": scan2["timestamp"],
            "new_networks": list(new_networks),
            "disappeared_networks": list(disappeared_networks),
            "changed_networks": changed_networks,
            "summary": {
                "total_new": len(new_networks),
                "total_disappeared": len(disappeared_networks),
                "total_changed": len(changed_networks)
            }
        }
    
    def _save_database(self) -> None:
        """Save database to file."""
        try:
            with open(self.db_path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            logger.debug(f"Database saved to: {self.db_path}")
        except Exception as e:
            logger.error(f"Error saving database: {e}")
            raise