#!/usr/bin/env python3
"""
Test di esempio per X WIRELESS
==============================

Questo script dimostra come utilizzare X WIRELESS in modalità sandbox
per testare le funzionalità senza eseguire comandi di sistema reali.

Creato da: Adil Fayyaz
Instagram: @Infinityx_20257
"""

import sys
import os
from pathlib import Path

# Aggiungi il percorso del modulo xwirless
sys.path.insert(0, str(Path(__file__).parent))

def test_xwirless_sandbox():
    """Test X WIRELESS in modalità sandbox."""
    print("X WIRELESS Test - Modalita Sandbox")
    print("=" * 50)
    
    try:
        # Importa i moduli necessari
        from xwirless.scanner import WiFiScanner
        from xwirless.parser import WiFiParser
        from xwirless.report import ReportGenerator
        from xwirless.safety import SafetyValidator
        
        print("OK: Moduli importati con successo")
        
        # Test scanner in modalità sandbox
        scanner = WiFiScanner(dry_run=True)
        print("OK: Scanner inizializzato in modalita dry-run")
        
        # Test parser
        parser = WiFiParser()
        print("OK: Parser inizializzato")
        
        # Test report generator
        reporter = ReportGenerator(author_badge=True)
        print("OK: Report generator inizializzato")
        
        # Test safety validator
        safety = SafetyValidator()
        print("OK: Safety validator inizializzato")
        
        # Test con dati di esempio
        sample_file = Path(__file__).parent.parent / "tests" / "samples" / "sample_iwlist.txt"
        
        if sample_file.exists():
            print(f"OK: File di esempio trovato: {sample_file}")
            
            # Carica dati di esempio
            sample_data = sample_file.read_text(encoding='utf-8')
            print("OK: Dati di esempio caricati")
            
            # Parsing dei dati
            scan_result = parser.parse_scan_output(sample_data, "wlan0")
            print(f"OK: Parsing completato: {scan_result.total_networks} reti trovate")
            
            # Genera report JSON
            json_report = reporter.generate_json_report(scan_result)
            print("OK: Report JSON generato")
            
            # Genera report Markdown
            md_report = reporter.generate_markdown_report(scan_result)
            print("OK: Report Markdown generato")
            
            # Salva report di esempio
            output_dir = Path(__file__).parent / "output"
            output_dir.mkdir(exist_ok=True)
            
            (output_dir / "test_report.json").write_text(json_report, encoding='utf-8')
            (output_dir / "test_report.md").write_text(md_report, encoding='utf-8')
            
            print(f"OK: Report salvati in: {output_dir}")
            
            # Mostra statistiche
            print("\nStatistiche:")
            for i, network in enumerate(scan_result.networks[:3], 1):
                print(f"  {i}. {network.ssid} ({network.bssid}) - {network.encryption}")
            
            print("\nTest completato con successo!")
            print("Ricorda: Questo e solo per scopi educativi!")
            
        else:
            print("ERRORE: File di esempio non trovato")
            return False
            
    except ImportError as e:
        print(f"ERRORE di importazione: {e}")
        return False
    except Exception as e:
        print(f"ERRORE durante il test: {e}")
        return False
    
    return True

def show_usage_examples():
    """Mostra esempi di utilizzo."""
    print("\nEsempi di utilizzo:")
    print("=" * 30)
    
    examples = [
        "# Test in modalita sandbox",
        "python -m xwirless scan --sandbox tests/samples/sample_iwlist.txt --format json",
        "",
        "# Test in modalita dry-run",
        "python -m xwirless scan --dry-run --format md",
        "",
        "# Mostra informazioni di sistema",
        "python -m xwirless info",
        "",
        "# Mostra versione",
        "python -m xwirless version",
        "",
        "# Test completo con database",
        "python -m xwirless scan --sandbox tests/samples/sample_iwlist.txt --save-db --format all"
    ]
    
    for example in examples:
        print(example)

if __name__ == "__main__":
    print("X WIRELESS TEST")
    print("Creato da: Adil Fayyaz")
    print("Segui su Instagram: @Infinityx_20257")
    print("SOLO PER SCOPI EDUCATIVI - USO AUTORIZZATO SOLO")
    print()
    
    # Esegui test
    success = test_xwirless_sandbox()
    
    if success:
        show_usage_examples()
        print("\nTutto funziona correttamente!")
        print("Puoi ora utilizzare X WIRELESS per i tuoi test educativi")
    else:
        print("\nTest fallito. Controlla l'installazione.")
        sys.exit(1)