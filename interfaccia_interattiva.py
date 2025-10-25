#!/usr/bin/env python3
"""
X WIRELESS - Interfaccia Interattiva
===================================

Interfaccia user-friendly per X WIRELESS
Creato da: Adil Fayyaz
Instagram: @Infinityx_20257
"""

import sys
import os
from pathlib import Path

# Aggiungi il percorso del modulo
sys.path.insert(0, str(Path(__file__).parent))

def show_menu():
    """Mostra il menu principale."""
    print("\n" + "="*60)
    print("           X WIRELESS - INTERFACCIA INTERATTIVA")
    print("="*60)
    print("Creato da: Adil Fayyaz")
    print("Instagram: @Infinityx_20257")
    print("SOLO PER SCOPI EDUCATIVI - USO AUTORIZZATO SOLO")
    print("="*60)
    print()
    print("📋 MENU PRINCIPALE:")
    print("1. 🔍 Test Scansione (Modalità Sandbox)")
    print("2. 📊 Genera Report Completo")
    print("3. 💾 Test con Database")
    print("4. 📈 Mostra Inventario")
    print("5. 🔧 Informazioni Sistema")
    print("6. 📖 Mostra Versione")
    print("7. ❓ Aiuto e Esempi")
    print("0. 🚪 Esci")
    print()

def test_scan():
    """Test scansione in modalità sandbox."""
    print("\n🔍 TEST SCANSIONE - MODALITÀ SANDBOX")
    print("-" * 40)
    
    try:
        from xwirless.scanner import WiFiScanner
        from xwirless.parser import WiFiParser
        from xwirless.report import ReportGenerator
        
        # Inizializza componenti
        scanner = WiFiScanner(dry_run=True)
        parser = WiFiParser()
        reporter = ReportGenerator(author_badge=True)
        
        print("✅ Componenti inizializzati")
        
        # Carica dati di esempio
        sample_file = Path(__file__).parent / "tests" / "samples" / "sample_iwlist.txt"
        
        if sample_file.exists():
            print(f"📁 Caricando dati da: {sample_file.name}")
            sample_data = sample_file.read_text(encoding='utf-8')
            
            # Parsing
            scan_result = parser.parse_scan_output(sample_data, "wlan0")
            print(f"✅ Parsing completato: {scan_result.total_networks} reti trovate")
            
            # Mostra risultati
            print("\n📡 RETI TROVATE:")
            for i, network in enumerate(scan_result.networks[:5], 1):
                print(f"  {i}. {network.ssid} ({network.bssid}) - {network.encryption}")
            
            if len(scan_result.networks) > 5:
                print(f"  ... e altre {len(scan_result.networks) - 5} reti")
            
            print("\n✅ Test completato con successo!")
            
        else:
            print("❌ File di esempio non trovato")
            
    except Exception as e:
        print(f"❌ Errore: {e}")

def generate_report():
    """Genera report completo."""
    print("\n📊 GENERA REPORT COMPLETO")
    print("-" * 30)
    
    try:
        from xwirless.scanner import WiFiScanner
        from xwirless.parser import WiFiParser
        from xwirless.report import ReportGenerator
        
        scanner = WiFiScanner(dry_run=True)
        parser = WiFiParser()
        reporter = ReportGenerator(author_badge=True)
        
        # Carica dati
        sample_file = Path(__file__).parent / "tests" / "samples" / "sample_iwlist.txt"
        sample_data = sample_file.read_text(encoding='utf-8')
        scan_result = parser.parse_scan_output(sample_data, "wlan0")
        
        # Genera report
        print("📄 Generando report JSON...")
        json_report = reporter.generate_json_report(scan_result)
        
        print("📄 Generando report Markdown...")
        md_report = reporter.generate_markdown_report(scan_result)
        
        # Salva report
        output_dir = Path(__file__).parent / "output"
        output_dir.mkdir(exist_ok=True)
        
        (output_dir / "interactive_report.json").write_text(json_report, encoding='utf-8')
        (output_dir / "interactive_report.md").write_text(md_report, encoding='utf-8')
        
        print(f"✅ Report salvati in: {output_dir}")
        print("📁 File generati:")
        print("  - interactive_report.json")
        print("  - interactive_report.md")
        
    except Exception as e:
        print(f"❌ Errore: {e}")

def test_database():
    """Test con database."""
    print("\n💾 TEST CON DATABASE")
    print("-" * 20)
    
    try:
        from xwirless.scanner import WiFiScanner
        from xwirless.parser import WiFiParser
        from xwirless.db import InventoryDB
        
        scanner = WiFiScanner(dry_run=True)
        parser = WiFiParser()
        db = InventoryDB("interactive_test.json")
        
        # Carica e salva dati
        sample_file = Path(__file__).parent / "tests" / "samples" / "sample_iwlist.txt"
        sample_data = sample_file.read_text(encoding='utf-8')
        scan_result = parser.parse_scan_output(sample_data, "wlan0")
        
        scan_id = db.save_scan(scan_result)
        print(f"✅ Scansione salvata: {scan_id}")
        
        # Mostra statistiche
        stats = db.get_statistics()
        print(f"📊 Statistiche database:")
        print(f"  - Scansioni totali: {stats['total_scans']}")
        print(f"  - Reti uniche: {stats['unique_networks']}")
        
    except Exception as e:
        print(f"❌ Errore: {e}")

def show_inventory():
    """Mostra inventario."""
    print("\n📈 INVENTARIO DATABASE")
    print("-" * 25)
    
    try:
        from xwirless.db import InventoryDB
        
        db = InventoryDB("interactive_test.json")
        stats = db.get_statistics()
        
        print(f"📊 Statistiche:")
        print(f"  - Scansioni totali: {stats['total_scans']}")
        print(f"  - Reti uniche: {stats['unique_networks']}")
        print(f"  - Ultima scansione: {stats['last_scan_date'] or 'Mai'}")
        
        # Mostra scansioni recenti
        scans = db.get_all_scans()
        if scans:
            print(f"\n📅 Scansioni recenti:")
            for scan in scans[-3:]:
                print(f"  - {scan['id']}: {scan['total_networks']} reti")
        
    except Exception as e:
        print(f"❌ Errore: {e}")

def show_system_info():
    """Mostra informazioni sistema."""
    print("\n🔧 INFORMAZIONI SISTEMA")
    print("-" * 25)
    
    try:
        from xwirless.utils import get_system_info
        
        info = get_system_info()
        print(f"🖥️ Sistema: {info['system']}")
        print(f"🐍 Python: {info['python_version']}")
        print(f"📦 Piattaforma: {info['platform']}")
        
        print(f"\n🔧 Dipendenze:")
        deps = info['dependencies']
        for dep, available in deps.items():
            status = "✅" if available else "❌"
            print(f"  {status} {dep}")
        
    except Exception as e:
        print(f"❌ Errore: {e}")

def show_version():
    """Mostra versione."""
    print("\n📖 INFORMAZIONI VERSIONE")
    print("-" * 30)
    
    try:
        from xwirless.utils import get_version_info
        
        version_info = get_version_info()
        print(f"🔢 Versione: {version_info['version']}")
        print(f"👤 Autore: {version_info['author']}")
        print(f"📧 Email: {version_info['email']}")
        print(f"🐍 Python: {version_info['python_version']}")
        print(f"💻 Piattaforma: {version_info['platform']}")
        
    except Exception as e:
        print(f"❌ Errore: {e}")

def show_help():
    """Mostra aiuto ed esempi."""
    print("\n❓ AIUTO ED ESEMPI")
    print("-" * 20)
    print()
    print("🚀 COMANDI CLI DIRETTI:")
    print("  python -m xwirless --help")
    print("  python -m xwirless scan --sandbox tests/samples/sample_iwlist.txt")
    print("  python -m xwirless scan --dry-run --format md")
    print("  python -m xwirless info")
    print("  python -m xwirless version")
    print()
    print("📱 SU TERMUX (Android):")
    print("  Usa sempre --sandbox per test sicuri")
    print("  python -m xwirless scan --sandbox tests/samples/sample_iwlist.txt --format json")
    print()
    print("⚠️ IMPORTANTE:")
    print("  - Solo per scopi educativi")
    print("  - Solo su reti autorizzate")
    print("  - Rispetta le leggi locali")
    print()
    print("📞 Supporto:")
    print("  - Autore: Adil Fayyaz")
    print("  - Instagram: @Infinityx_20257")
    print("  - GitHub: https://github.com/Adil-fayyaz/xwirless")

def main():
    """Funzione principale."""
    while True:
        show_menu()
        
        try:
            choice = input("👉 Scegli un'opzione (0-7): ").strip()
            
            if choice == "0":
                print("\n👋 Arrivederci! Usa X WIRELESS responsabilmente!")
                break
            elif choice == "1":
                test_scan()
            elif choice == "2":
                generate_report()
            elif choice == "3":
                test_database()
            elif choice == "4":
                show_inventory()
            elif choice == "5":
                show_system_info()
            elif choice == "6":
                show_version()
            elif choice == "7":
                show_help()
            else:
                print("❌ Opzione non valida. Riprova.")
            
            input("\n⏎ Premi Invio per continuare...")
            
        except KeyboardInterrupt:
            print("\n\n👋 Arrivederci!")
            break
        except Exception as e:
            print(f"\n❌ Errore: {e}")
            input("⏎ Premi Invio per continuare...")

if __name__ == "__main__":
    main()
