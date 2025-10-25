"""
Utility functions and helpers.
"""

import logging
import logging.handlers
import os
import sys
from typing import Dict, Any, Optional, List
from datetime import datetime
from pathlib import Path

from . import __version__, __author__

def setup_logging(level: str = "INFO", log_file: Optional[str] = None) -> None:
    """Setup logging configuration."""
    log_level = getattr(logging, level.upper(), logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Setup console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    
    # Setup root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.addHandler(console_handler)
    
    # Setup file handler if specified
    if log_file:
        file_handler = logging.handlers.RotatingFileHandler(
            log_file, 
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

def get_version_info() -> Dict[str, Any]:
    """Get version and author information."""
    return {
        "version": __version__,
        "author": __author__,
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        "platform": sys.platform
    }

def format_timestamp(timestamp: datetime) -> str:
    """Format timestamp for display."""
    return timestamp.strftime("%Y-%m-%d %H:%M:%S UTC")

def format_signal_level(signal_level: int) -> str:
    """Format signal level with appropriate emoji."""
    if signal_level >= -30:
        return f"🟢 {signal_level} dBm (Excellent)"
    elif signal_level >= -50:
        return f"🟡 {signal_level} dBm (Good)"
    elif signal_level >= -70:
        return f"🟠 {signal_level} dBm (Fair)"
    else:
        return f"🔴 {signal_level} dBm (Poor)"

def format_encryption(encryption: str) -> str:
    """Format encryption type with appropriate emoji."""
    encryption_icons = {
        "Open": "🔓",
        "WEP": "🔒",
        "WPA": "🔐",
        "WPA2": "🔐",
        "WPA3": "🔐"
    }
    icon = encryption_icons.get(encryption, "❓")
    return f"{icon} {encryption}"

def validate_interface(interface: str) -> bool:
    """Validate network interface name."""
    if not interface:
        return False
    
    # Basic validation - interface should start with common prefixes
    valid_prefixes = ["wlan", "wifi", "eth", "en", "wl"]
    return any(interface.lower().startswith(prefix) for prefix in valid_prefixes)

def get_sample_files() -> List[str]:
    """Get list of available sample files."""
    samples_dir = Path(__file__).parent.parent / "tests" / "samples"
    if samples_dir.exists():
        return [f.name for f in samples_dir.glob("*.txt")]
    return []

def create_sample_file(content: str, filename: str) -> str:
    """Create a sample file for testing."""
    samples_dir = Path(__file__).parent.parent / "tests" / "samples"
    samples_dir.mkdir(parents=True, exist_ok=True)
    
    sample_path = samples_dir / filename
    sample_path.write_text(content, encoding='utf-8')
    
    return str(sample_path)

def check_dependencies() -> Dict[str, bool]:
    """Check if required system dependencies are available."""
    import subprocess
    
    dependencies = {
        "iwlist": False,
        "nmcli": False,
        "iwconfig": False,
        "ip": False
    }
    
    for dep in dependencies.keys():
        try:
            result = subprocess.run(
                [dep, "--version"], 
                capture_output=True, 
                timeout=5
            )
            dependencies[dep] = result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            dependencies[dep] = False
    
    return dependencies

def get_system_info() -> Dict[str, Any]:
    """Get system information."""
    import platform
    
    return {
        "platform": platform.platform(),
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "dependencies": check_dependencies()
    }