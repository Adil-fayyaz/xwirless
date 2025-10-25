#!/usr/bin/env python3
"""
X WIRELESS - Interfaccia Accattivante (ASCII Only)
=================================================

Interfaccia terminale con stile rosso e nero - Solo ASCII
Creato da: Adil Fayyaz
Instagram: @Infinityx_20257
"""

import sys
import os
import time
from pathlib import Path

def clear_screen():
    """Pulisce lo schermo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Stampa l'header con ASCII art."""
    clear_screen()
    
    # ASCII Art X WIRELESS (solo caratteri ASCII)
    ascii_art = """
    X     X    W     W    I    R    R    L    E    S    S
    X     X    W     W    I    R    R    L    E    S    S
    X     X    W     W    I    R    R    L    E    S    S
    X     X    W  W  W    I    RRRR     L    E    S    S
    X     X    W W W W    I    R   R    L    E    S    S
    XXXXXXX    W     W    I    R    R   LLLLL EEEEE SSSSS
"""
    
    print(ascii_art)
    
    # Informazioni autore
    author_info = """
    </> Author: Adil Fayyaz | Instagram: @Infinityx_20257
"""
    print(author_info)
    
    # Separatori
    separator = "="*80
    print(separator)
    
    # Telegram/Social
    social_info = """
    Telegram @Infinityx_20257 | GitHub: Adil-fayyaz/xwirless
"""
    print(social_info)
    
    print(separator)
    
    # Avviso
    warning = """
    [!] Educational Use Only - Authorized Networks Only
"""
    print(warning)
    
    print(separator)

def print_menu():
    """Stampa il menu principale."""
    print("\nOPTIONS:")
    print("-"*80)
    
    # Menu a due colonne
    menu_items = [
        ("[1]", "Scan Sandbox", "[11]", "System Info"),
        ("[2]", "Scan Dry-Run", "[12]", "Version Info"),
        ("[3]", "Generate Report", "[13]", "Database Stats"),
        ("[4]", "Test Database", "[14]", "Compare Scans"),
        ("[5]", "Show Inventory", "[15]", "Export Data"),
        ("[6]", "Network Analysis", "[16]", "Security Check"),
        ("[7]", "Signal Analysis", "[17]", "Encryption Check"),
        ("[8]", "Channel Scan", "[18]", "Protocol Info"),
        ("[9]", "Quality Report", "[19]", "Help & Examples"),
        ("[10]", "Full Scan", "[20]", "About Tool"),
    ]
    
    for left_num, left_item, right_num, right_item in menu_items:
        left = f"{left_num} {left_item:<20}"
        right = f"{right_num} {right_item}"
        print(f"    {left:<30} {right}")
    
    print("-"*80)
    print("    [00] EXIT")

def scan_sandbox():
    """Esegue scansione in modalità sandbox."""
    print("\nSCAN SANDBOX MODE")
    print("-"*50)
    
    try:
        from xwirless.scanner import WiFiScanner
        from xwirless.parser import WiFiParser
        from xwirless.report import ReportGenerator
        
        print("Initializing components...")
        scanner = WiFiScanner(dry_run=True)
        parser = WiFiParser()
        reporter = ReportGenerator(author_badge=True)
        
        print("Loading sample data...")
        sample_file = Path(__file__).parent / "tests" / "samples" / "sample_iwlist.txt"
        
        if sample_file.exists():
            sample_data = sample_file.read_text(encoding='utf-8')
            scan_result = parser.parse_scan_output(sample_data, "wlan0")
            
            print(f"Scan completed: {scan_result.total_networks} networks found")
            
            # Mostra risultati
            print("\nDISCOVERED NETWORKS:")
            for i, network in enumerate(scan_result.networks[:10], 1):
                print(f"    [{i:2d}] {network.ssid:<20} {network.bssid} {network.encryption}")
            
            if len(scan_result.networks) > 10:
                print(f"    ... and {len(scan_result.networks) - 10} more networks")
            
            print("\nGenerating report...")
            json_report = reporter.generate_json_report(scan_result)
            
            # Salva report
            output_dir = Path(__file__).parent / "output"
            output_dir.mkdir(exist_ok=True)
            (output_dir / "sandbox_report.json").write_text(json_report, encoding='utf-8')
            
            print("Report saved to: output/sandbox_report.json")
            print("Scan completed successfully!")
            
        else:
            print("Sample file not found!")
            
    except Exception as e:
        print(f"Error: {e}")

def scan_dry_run():
    """Esegue scansione in modalità dry-run."""
    print("\nDRY-RUN SCAN MODE")
    print("-"*50)
    
    try:
        from xwirless.scanner import WiFiScanner
        
        print("Initializing dry-run scanner...")
        scanner = WiFiScanner(dry_run=True)
        
        print("Simulating network scan...")
        interface = scanner.detect_interface()
        print(f"Detected interface: {interface}")
        
        print("Simulating scan output...")
        output = scanner.scan_networks(interface)
        
        print("Dry-run completed successfully!")
        print("No actual commands were executed.")
        
    except Exception as e:
        print(f"Error: {e}")

def generate_report():
    """Genera report completo."""
    print("\nGENERATE COMPLETE REPORT")
    print("-"*50)
    
    try:
        from xwirless.scanner import WiFiScanner
        from xwirless.parser import WiFiParser
        from xwirless.report import ReportGenerator
        
        print("Initializing components...")
        scanner = WiFiScanner(dry_run=True)
        parser = WiFiParser()
        reporter = ReportGenerator(author_badge=True)
        
        print("Loading sample data...")
        sample_file = Path(__file__).parent / "tests" / "samples" / "sample_iwlist.txt"
        sample_data = sample_file.read_text(encoding='utf-8')
        scan_result = parser.parse_scan_output(sample_data, "wlan0")
        
        print("Generating JSON report...")
        json_report = reporter.generate_json_report(scan_result)
        
        print("Generating Markdown report...")
        md_report = reporter.generate_markdown_report(scan_result)
        
        print("Generating CSV report...")
        csv_report = reporter.generate_csv_report(scan_result)
        
        # Salva report
        output_dir = Path(__file__).parent / "output"
        output_dir.mkdir(exist_ok=True)
        
        (output_dir / "complete_report.json").write_text(json_report, encoding='utf-8')
        (output_dir / "complete_report.md").write_text(md_report, encoding='utf-8')
        (output_dir / "complete_report.csv").write_text(csv_report, encoding='utf-8')
        
        print("Reports saved to:")
        print("    output/complete_report.json")
        print("    output/complete_report.md")
        print("    output/complete_report.csv")
        
        print("\nReport generation completed!")
        
    except Exception as e:
        print(f"Error: {e}")

def test_database():
    """Test con database."""
    print("\nDATABASE TEST")
    print("-"*50)
    
    try:
        from xwirless.scanner import WiFiScanner
        from xwirless.parser import WiFiParser
        from xwirless.db import InventoryDB
        
        print("Initializing database...")
        db = InventoryDB("test_database.json")
        
        print("Loading sample data...")
        scanner = WiFiScanner(dry_run=True)
        parser = WiFiParser()
        sample_file = Path(__file__).parent / "tests" / "samples" / "sample_iwlist.txt"
        sample_data = sample_file.read_text(encoding='utf-8')
        scan_result = parser.parse_scan_output(sample_data, "wlan0")
        
        print("Saving scan to database...")
        scan_id = db.save_scan(scan_result)
        
        print(f"Scan saved with ID: {scan_id}")
        
        # Mostra statistiche
        stats = db.get_statistics()
        print("\nDATABASE STATISTICS:")
        print(f"    Total scans: {stats['total_scans']}")
        print(f"    Unique networks: {stats['unique_networks']}")
        print(f"    Last scan: {stats['last_scan_date'] or 'Never'}")
        
        print("\nDatabase test completed!")
        
    except Exception as e:
        print(f"Error: {e}")

def show_inventory():
    """Mostra inventario."""
    print("\nINVENTORY DATABASE")
    print("-"*50)
    
    try:
        from xwirless.db import InventoryDB
        
        print("Loading database...")
        db = InventoryDB("test_database.json")
        
        stats = db.get_statistics()
        print("\nINVENTORY STATISTICS:")
        print(f"    Total scans: {stats['total_scans']}")
        print(f"    Unique networks: {stats['unique_networks']}")
        print(f"    Last scan: {stats['last_scan_date'] or 'Never'}")
        
        # Mostra scansioni recenti
        scans = db.get_all_scans()
        if scans:
            print("\nRECENT SCANS:")
            for scan in scans[-5:]:
                print(f"    {scan['id']} - {scan['total_networks']} networks")
        
        print("\nInventory loaded successfully!")
        
    except Exception as e:
        print(f"Error: {e}")

def system_info():
    """Mostra informazioni sistema."""
    print("\nSYSTEM INFORMATION")
    print("-"*50)
    
    try:
        from xwirless.utils import get_system_info
        
        print("Gathering system information...")
        info = get_system_info()
        
        print("\nSYSTEM DETAILS:")
        print(f"    Platform: {info['platform']}")
        print(f"    System: {info['system']}")
        print(f"    Release: {info['release']}")
        print(f"    Machine: {info['machine']}")
        print(f"    Python: {info['python_version']}")
        
        print("\nDEPENDENCIES:")
        deps = info['dependencies']
        for dep, available in deps.items():
            status = "AVAILABLE" if available else "NOT AVAILABLE"
            print(f"    {dep:<15} {status}")
        
        print("\nSystem information gathered!")
        
    except Exception as e:
        print(f"Error: {e}")

def version_info():
    """Mostra informazioni versione."""
    print("\nVERSION INFORMATION")
    print("-"*50)
    
    try:
        from xwirless.utils import get_version_info
        
        print("Loading version information...")
        version_info = get_version_info()
        
        print("\nTOOL DETAILS:")
        print(f"    Version: {version_info['version']}")
        print(f"    Author: {version_info['author']}")
        print(f"    Email: {version_info['email']}")
        print(f"    Python: {version_info['python_version']}")
        print(f"    Platform: {version_info['platform']}")
        
        print("\nVersion information loaded!")
        
    except Exception as e:
        print(f"Error: {e}")

def about_tool():
    """Mostra informazioni sul tool."""
    print("\nABOUT X WIRELESS")
    print("-"*50)
    
    about_text = """
X WIRELESS is an advanced Wi-Fi audit and inventory tool designed 
EXCLUSIVELY for educational purposes and testing on owned networks 
with written authorization.

KEY FEATURES:
• Safe Wi-Fi network scanning
• Multiple output formats (JSON, Markdown, CSV)
• Inventory database with change tracking
• Comprehensive reporting system
• Safety-by-design with legal compliance
• Educational focus with no offensive capabilities

SAFETY FEATURES:
• Mandatory legal warnings
• Dry-run mode for safe testing
• Sandbox mode with sample data
• Target validation (localhost/internal only)
• No cracking, deauth, or injection capabilities

LEGAL NOTICE:
This tool is for EDUCATIONAL USE ONLY.
Only use on networks you OWN or have EXPLICIT WRITTEN AUTHORIZATION.
Always comply with applicable laws and regulations.

AUTHOR:
Adil Fayyaz
Instagram: @Infinityx_20257
GitHub: https://github.com/Adil-fayyaz/xwirless
Email: adilfayyaz388@gmail.com

LICENSE:
MIT License - Educational Use Only
"""
    
    print(about_text)

def main():
    """Funzione principale."""
    while True:
        print_header()
        print_menu()
        
        try:
            choice = input("\nSelect option: ").strip()
            
            if choice == "00":
                print("\nGoodbye! Use X WIRELESS responsibly!")
                break
            elif choice == "1":
                scan_sandbox()
            elif choice == "2":
                scan_dry_run()
            elif choice == "3":
                generate_report()
            elif choice == "4":
                test_database()
            elif choice == "5":
                show_inventory()
            elif choice == "11":
                system_info()
            elif choice == "12":
                version_info()
            elif choice == "20":
                about_tool()
            else:
                print("\nInvalid option. Please try again.")
            
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
