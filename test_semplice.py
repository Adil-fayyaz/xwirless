#!/usr/bin/env python3
"""
X WIRELESS - Interfaccia Semplice
================================

Interfaccia semplificata per X WIRELESS
Creato da: Adil Fayyaz
Instagram: @Infinityx_20257
"""

import sys
import os
from pathlib import Path

def main():
    print("X WIRELESS - Interfaccia Semplice")
    print("=" * 40)
    print("Creato da: Adil Fayyaz")
    print("Instagram: @Infinityx_20257")
    print("SOLO PER SCOPI EDUCATIVI")
    print("=" * 40)
    print()
    
    # Test importazione
    try:
        print("Testando importazione moduli...")
        from xwirless.scanner import WiFiScanner
        from xwirless.parser import WiFiParser
        from xwirless.report import ReportGenerator
        print("OK: Moduli importati con successo")
    except Exception as e:
        print(f"ERRORE importazione: {e}")
        return
    
    # Test scanner
    try:
        print("\nTestando scanner...")
        scanner = WiFiScanner(dry_run=True)
        print("OK: Scanner inizializzato")
    except Exception as e:
        print(f"ERRORE scanner: {e}")
        return
    
    # Test parser
    try:
        print("Testando parser...")
        parser = WiFiParser()
        print("OK: Parser inizializzato")
    except Exception as e:
        print(f"ERRORE parser: {e}")
        return
    
    # Test report
    try:
        print("Testando report generator...")
        reporter = ReportGenerator(author_badge=True)
        print("OK: Report generator inizializzato")
    except Exception as e:
        print(f"ERRORE report: {e}")
        return
    
    print("\nTUTTI I TEST SUPERATI!")
    print("\nComandi disponibili:")
    print("python -m xwirless --help")
    print("python -m xwirless scan --sandbox tests/samples/sample_iwlist.txt --format json")
    print("python -m xwirless scan --dry-run --format md")
    print("python -m xwirless info")
    print("python -m xwirless version")

if __name__ == "__main__":
    main()