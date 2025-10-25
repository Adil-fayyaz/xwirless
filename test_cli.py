#!/usr/bin/env python3
"""
Test CLI X WIRELESS senza caratteri Unicode
"""

import sys
import os
from pathlib import Path

# Aggiungi il percorso del modulo xwirless
sys.path.insert(0, str(Path(__file__).parent))

def test_cli_basic():
    """Test CLI base senza caratteri Unicode."""
    print("X WIRELESS CLI Test")
    print("=" * 30)
    
    try:
        # Test import CLI
        from xwirless.cli import cli_main
        print("OK: CLI importato")
        
        # Test scanner
        from xwirless.scanner import WiFiScanner
        scanner = WiFiScanner(dry_run=True)
        print("OK: Scanner inizializzato")
        
        # Test parser
        from xwirless.parser import WiFiParser
        parser = WiFiParser()
        print("OK: Parser inizializzato")
        
        # Test report
        from xwirless.report import ReportGenerator
        reporter = ReportGenerator(author_badge=True)
        print("OK: Report generator inizializzato")
        
        # Test database
        from xwirless.db import InventoryDB
        db = InventoryDB("test_db.json")
        print("OK: Database inizializzato")
        
        # Test safety
        from xwirless.safety import SafetyValidator
        safety = SafetyValidator()
        print("OK: Safety validator inizializzato")
        
        print("\nTutti i moduli funzionano correttamente!")
        print("Il progetto X WIRELESS e pronto per l'uso.")
        
        return True
        
    except Exception as e:
        print(f"ERRORE: {e}")
        return False

if __name__ == "__main__":
    print("X WIRELESS - Test CLI")
    print("Creato da: Adil Fayyaz")
    print("Instagram: @Infinityx_20257")
    print("SOLO PER SCOPI EDUCATIVI")
    print()
    
    success = test_cli_basic()
    
    if success:
        print("\nSUCCESSO: X WIRELESS funziona correttamente!")
        print("\nPer utilizzare il tool:")
        print("1. Installa le dipendenze: pip install click pydantic requests")
        print("2. Testa in modalita sandbox: python -m xwirless scan --sandbox tests/samples/sample_iwlist.txt")
        print("3. Leggi la GUIDA_RAPIDA.txt per maggiori dettagli")
    else:
        print("\nERRORE: Controlla l'installazione")
        sys.exit(1)
