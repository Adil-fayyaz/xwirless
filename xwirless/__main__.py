#!/usr/bin/env python3
"""
X WIRELESS - Main CLI Entry Point
=================================

Command-line interface for the X WIRELESS Wi-Fi audit tool.
"""

import sys
import click
from datetime import datetime
from pathlib import Path

from .cli import cli_main
from .safety import SafetyValidator
from .utils import setup_logging, get_version_info

def main():
    """Main entry point for the CLI."""
    try:
        # Show legal warning and get confirmation
        safety = SafetyValidator()
        if not safety.show_legal_warning():
            click.echo("❌ Legal confirmation required. Exiting.")
            sys.exit(1)
        
        # Setup logging
        setup_logging()
        
        # Run CLI
        cli_main()
        
    except KeyboardInterrupt:
        click.echo("\n⚠️  Operation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        sys.exit(1)

if __name__ == "__main__":
    main()