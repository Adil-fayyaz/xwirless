#!/usr/bin/env python3
"""
X WIRELESS - Interfaccia Accattivante
===================================

Interfaccia terminale con stile rosso e nero
Creato da: Adil Fayyaz
Instagram: @Infinityx_20257
"""

import sys
import os
import time
from pathlib import Path

# Codici colore ANSI per rosso e nero
class Colors:
    RED = '\033[91m'
    BLACK = '\033[30m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BG_RED = '\033[101m'
    BG_BLACK = '\033[40m'
    CLEAR = '\033[2J'
    HOME = '\033[H'

def clear_screen():
    """Pulisce lo schermo e posiziona il cursore in alto."""
    print(Colors.CLEAR + Colors.HOME, end='')

def print_header():
    """Stampa l'header con ASCII art."""
    clear_screen()
    
    # ASCII Art X WIRELESS
    ascii_art = f"""
{Colors.RED}{Colors.BOLD}
    ██╗  ██╗    ██╗    ██╗███████╗██████╗ ██╗     ███████╗███████╗███████╗
    ╚██╗██╔╝    ██║    ██║██╔════╝██╔══██╗██║     ██╔════╝██╔════╝██╔════╝
     ╚███╔╝     ██║ █╗ ██║█████╗  ██████╔╝██║     █████╗  ███████╗███████╗
     ██╔██╗     ██║███╗██║██╔══╝  ██╔══██╗██║     ██╔══╝  ╚════██║╚════██║
    ██╔╝ ██╗    ╚███╔███╔╝███████╗██║  ██║███████╗███████╗███████║███████║
    ╚═╝  ╚═╝     ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝
{Colors.RESET}
"""
    
    print(ascii_art)
    
    # Informazioni autore
    author_info = f"""
{Colors.WHITE}{Colors.BOLD}    </> Author: Adil Fayyaz | Instagram: @Infinityx_20257{Colors.RESET}
"""
    print(author_info)
    
    # Separatori
    separator = f"{Colors.RED}{'='*80}{Colors.RESET}"
    print(separator)
    
    # Telegram/Social
    social_info = f"""
{Colors.RED}    Telegram @Infinityx_20257 | GitHub: Adil-fayyaz/xwirless{Colors.RESET}
"""
    print(social_info)
    
    print(separator)
    
    # Avviso
    warning = f"""
{Colors.WHITE}    [!] Educational Use Only - Authorized Networks Only{Colors.RESET}
"""
    print(warning)
    
    print(separator)

def print_menu():
    """Stampa il menu principale."""
    print(f"\n{Colors.RED}{Colors.BOLD}OPTIONS:{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*80}{Colors.RESET}")
    
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
        left = f"{Colors.WHITE}{left_num}{Colors.RESET} {Colors.WHITE}{left_item:<20}{Colors.RESET}"
        right = f"{Colors.WHITE}{right_num}{Colors.RESET} {Colors.WHITE}{right_item}{Colors.RESET}"
        print(f"    {left:<30} {right}")
    
    print(f"{Colors.WHITE}{'─'*80}{Colors.RESET}")
    print(f"    {Colors.WHITE}[00]{Colors.RESET} {Colors.RED}{Colors.BOLD}EXIT{Colors.RESET}")

def scan_sandbox():
    """Esegue scansione in modalità sandbox."""
    print(f"\n{Colors.RED}{Colors.BOLD}SCAN SANDBOX MODE{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*50}{Colors.RESET}")
    
    try:
        from xwirless.scanner import WiFiScanner
        from xwirless.parser import WiFiParser
        from xwirless.report import ReportGenerator
        
        print(f"{Colors.WHITE}Initializing components...{Colors.RESET}")
        scanner = WiFiScanner(dry_run=True)
        parser = WiFiParser()
        reporter = ReportGenerator(author_badge=True)
        
        print(f"{Colors.WHITE}Loading sample data...{Colors.RESET}")
        sample_file = Path(__file__).parent / "tests" / "samples" / "sample_iwlist.txt"
        
        if sample_file.exists():
            sample_data = sample_file.read_text(encoding='utf-8')
            scan_result = parser.parse_scan_output(sample_data, "wlan0")
            
            print(f"{Colors.WHITE}Scan completed: {Colors.RED}{scan_result.total_networks}{Colors.WHITE} networks found{Colors.RESET}")
            
            # Mostra risultati
            print(f"\n{Colors.RED}{Colors.BOLD}DISCOVERED NETWORKS:{Colors.RESET}")
            for i, network in enumerate(scan_result.networks[:10], 1):
                print(f"    {Colors.WHITE}[{i:2d}]{Colors.RESET} {Colors.WHITE}{network.ssid:<20}{Colors.RESET} {Colors.RED}{network.bssid}{Colors.RESET} {Colors.WHITE}{network.encryption}{Colors.RESET}")
            
            if len(scan_result.networks) > 10:
                print(f"    {Colors.WHITE}... and {len(scan_result.networks) - 10} more networks{Colors.RESET}")
            
            print(f"\n{Colors.WHITE}Generating report...{Colors.RESET}")
            json_report = reporter.generate_json_report(scan_result)
            
            # Salva report
            output_dir = Path(__file__).parent / "output"
            output_dir.mkdir(exist_ok=True)
            (output_dir / "sandbox_report.json").write_text(json_report, encoding='utf-8')
            
            print(f"{Colors.WHITE}Report saved to: {Colors.RED}output/sandbox_report.json{Colors.RESET}")
            print(f"{Colors.WHITE}Scan completed successfully!{Colors.RESET}")
            
        else:
            print(f"{Colors.RED}Sample file not found!{Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

def scan_dry_run():
    """Esegue scansione in modalità dry-run."""
    print(f"\n{Colors.RED}{Colors.BOLD}DRY-RUN SCAN MODE{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*50}{Colors.RESET}")
    
    try:
        from xwirless.scanner import WiFiScanner
        
        print(f"{Colors.WHITE}Initializing dry-run scanner...{Colors.RESET}")
        scanner = WiFiScanner(dry_run=True)
        
        print(f"{Colors.WHITE}Simulating network scan...{Colors.RESET}")
        interface = scanner.detect_interface()
        print(f"{Colors.WHITE}Detected interface: {Colors.RED}{interface}{Colors.RESET}")
        
        print(f"{Colors.WHITE}Simulating scan output...{Colors.RESET}")
        output = scanner.scan_networks(interface)
        
        print(f"{Colors.WHITE}Dry-run completed successfully!{Colors.RESET}")
        print(f"{Colors.WHITE}No actual commands were executed.{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

def generate_report():
    """Genera report completo."""
    print(f"\n{Colors.RED}{Colors.BOLD}GENERATE COMPLETE REPORT{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*50}{Colors.RESET}")
    
    try:
        from xwirless.scanner import WiFiScanner
        from xwirless.parser import WiFiParser
        from xwirless.report import ReportGenerator
        
        print(f"{Colors.WHITE}Initializing components...{Colors.RESET}")
        scanner = WiFiScanner(dry_run=True)
        parser = WiFiParser()
        reporter = ReportGenerator(author_badge=True)
        
        print(f"{Colors.WHITE}Loading sample data...{Colors.RESET}")
        sample_file = Path(__file__).parent / "tests" / "samples" / "sample_iwlist.txt"
        sample_data = sample_file.read_text(encoding='utf-8')
        scan_result = parser.parse_scan_output(sample_data, "wlan0")
        
        print(f"{Colors.WHITE}Generating JSON report...{Colors.RESET}")
        json_report = reporter.generate_json_report(scan_result)
        
        print(f"{Colors.WHITE}Generating Markdown report...{Colors.RESET}")
        md_report = reporter.generate_markdown_report(scan_result)
        
        print(f"{Colors.WHITE}Generating CSV report...{Colors.RESET}")
        csv_report = reporter.generate_csv_report(scan_result)
        
        # Salva report
        output_dir = Path(__file__).parent / "output"
        output_dir.mkdir(exist_ok=True)
        
        (output_dir / "complete_report.json").write_text(json_report, encoding='utf-8')
        (output_dir / "complete_report.md").write_text(md_report, encoding='utf-8')
        (output_dir / "complete_report.csv").write_text(csv_report, encoding='utf-8')
        
        print(f"{Colors.WHITE}Reports saved to:{Colors.RESET}")
        print(f"    {Colors.RED}output/complete_report.json{Colors.RESET}")
        print(f"    {Colors.RED}output/complete_report.md{Colors.RESET}")
        print(f"    {Colors.RED}output/complete_report.csv{Colors.RESET}")
        
        print(f"\n{Colors.WHITE}Report generation completed!{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

def test_database():
    """Test con database."""
    print(f"\n{Colors.RED}{Colors.BOLD}DATABASE TEST{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*50}{Colors.RESET}")
    
    try:
        from xwirless.scanner import WiFiScanner
        from xwirless.parser import WiFiParser
        from xwirless.db import InventoryDB
        
        print(f"{Colors.WHITE}Initializing database...{Colors.RESET}")
        db = InventoryDB("test_database.json")
        
        print(f"{Colors.WHITE}Loading sample data...{Colors.RESET}")
        scanner = WiFiScanner(dry_run=True)
        parser = WiFiParser()
        sample_file = Path(__file__).parent / "tests" / "samples" / "sample_iwlist.txt"
        sample_data = sample_file.read_text(encoding='utf-8')
        scan_result = parser.parse_scan_output(sample_data, "wlan0")
        
        print(f"{Colors.WHITE}Saving scan to database...{Colors.RESET}")
        scan_id = db.save_scan(scan_result)
        
        print(f"{Colors.WHITE}Scan saved with ID: {Colors.RED}{scan_id}{Colors.RESET}")
        
        # Mostra statistiche
        stats = db.get_statistics()
        print(f"\n{Colors.RED}{Colors.BOLD}DATABASE STATISTICS:{Colors.RESET}")
        print(f"    {Colors.WHITE}Total scans: {Colors.RED}{stats['total_scans']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Unique networks: {Colors.RED}{stats['unique_networks']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Last scan: {Colors.RED}{stats['last_scan_date'] or 'Never'}{Colors.RESET}")
        
        print(f"\n{Colors.WHITE}Database test completed!{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

def show_inventory():
    """Mostra inventario."""
    print(f"\n{Colors.RED}{Colors.BOLD}INVENTORY DATABASE{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*50}{Colors.RESET}")
    
    try:
        from xwirless.db import InventoryDB
        
        print(f"{Colors.WHITE}Loading database...{Colors.RESET}")
        db = InventoryDB("test_database.json")
        
        stats = db.get_statistics()
        print(f"\n{Colors.RED}{Colors.BOLD}INVENTORY STATISTICS:{Colors.RESET}")
        print(f"    {Colors.WHITE}Total scans: {Colors.RED}{stats['total_scans']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Unique networks: {Colors.RED}{stats['unique_networks']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Last scan: {Colors.RED}{stats['last_scan_date'] or 'Never'}{Colors.RESET}")
        
        # Mostra scansioni recenti
        scans = db.get_all_scans()
        if scans:
            print(f"\n{Colors.RED}{Colors.BOLD}RECENT SCANS:{Colors.RESET}")
            for scan in scans[-5:]:
                print(f"    {Colors.WHITE}{scan['id']}{Colors.RESET} - {Colors.RED}{scan['total_networks']}{Colors.WHITE} networks{Colors.RESET}")
        
        print(f"\n{Colors.WHITE}Inventory loaded successfully!{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

def system_info():
    """Mostra informazioni sistema."""
    print(f"\n{Colors.RED}{Colors.BOLD}SYSTEM INFORMATION{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*50}{Colors.RESET}")
    
    try:
        from xwirless.utils import get_system_info
        
        print(f"{Colors.WHITE}Gathering system information...{Colors.RESET}")
        info = get_system_info()
        
        print(f"\n{Colors.RED}{Colors.BOLD}SYSTEM DETAILS:{Colors.RESET}")
        print(f"    {Colors.WHITE}Platform: {Colors.RED}{info['platform']}{Colors.RESET}")
        print(f"    {Colors.WHITE}System: {Colors.RED}{info['system']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Release: {Colors.RED}{info['release']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Machine: {Colors.RED}{info['machine']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Python: {Colors.RED}{info['python_version']}{Colors.RESET}")
        
        print(f"\n{Colors.RED}{Colors.BOLD}DEPENDENCIES:{Colors.RESET}")
        deps = info['dependencies']
        for dep, available in deps.items():
            status = f"{Colors.WHITE}AVAILABLE{Colors.RESET}" if available else f"{Colors.RED}NOT AVAILABLE{Colors.RESET}"
            print(f"    {Colors.WHITE}{dep:<15}{Colors.RESET} {status}")
        
        print(f"\n{Colors.WHITE}System information gathered!{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

def version_info():
    """Mostra informazioni versione."""
    print(f"\n{Colors.RED}{Colors.BOLD}VERSION INFORMATION{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*50}{Colors.RESET}")
    
    try:
        from xwirless.utils import get_version_info
        
        print(f"{Colors.WHITE}Loading version information...{Colors.RESET}")
        version_info = get_version_info()
        
        print(f"\n{Colors.RED}{Colors.BOLD}TOOL DETAILS:{Colors.RESET}")
        print(f"    {Colors.WHITE}Version: {Colors.RED}{version_info['version']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Author: {Colors.RED}{version_info['author']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Email: {Colors.RED}{version_info['email']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Python: {Colors.RED}{version_info['python_version']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Platform: {Colors.RED}{version_info['platform']}{Colors.RESET}")
        
        print(f"\n{Colors.WHITE}Version information loaded!{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.RESET}")

def about_tool():
    """Mostra informazioni sul tool."""
    print(f"\n{Colors.RED}{Colors.BOLD}ABOUT X WIRELESS{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*50}{Colors.RESET}")
    
    about_text = f"""
{Colors.WHITE}X WIRELESS is an advanced Wi-Fi audit and inventory tool designed 
EXCLUSIVELY for educational purposes and testing on owned networks 
with written authorization.

{Colors.RED}KEY FEATURES:{Colors.RESET}
{Colors.WHITE}• Safe Wi-Fi network scanning
• Multiple output formats (JSON, Markdown, CSV)
• Inventory database with change tracking
• Comprehensive reporting system
• Safety-by-design with legal compliance
• Educational focus with no offensive capabilities

{Colors.RED}SAFETY FEATURES:{Colors.RESET}
{Colors.WHITE}• Mandatory legal warnings
• Dry-run mode for safe testing
• Sandbox mode with sample data
• Target validation (localhost/internal only)
• No cracking, deauth, or injection capabilities

{Colors.RED}LEGAL NOTICE:{Colors.RESET}
{Colors.WHITE}This tool is for EDUCATIONAL USE ONLY.
Only use on networks you OWN or have EXPLICIT WRITTEN AUTHORIZATION.
Always comply with applicable laws and regulations.

{Colors.RED}AUTHOR:{Colors.RESET}
{Colors.WHITE}Adil Fayyaz
Instagram: @Infinityx_20257
GitHub: https://github.com/Adil-fayyaz/xwirless
Email: adilfayyaz388@gmail.com

{Colors.RED}LICENSE:{Colors.RESET}
{Colors.WHITE}MIT License - Educational Use Only
{Colors.RESET}
"""
    
    print(about_text)

def main():
    """Funzione principale."""
    while True:
        print_header()
        print_menu()
        
        try:
            choice = input(f"\n{Colors.WHITE}Select option: {Colors.RESET}").strip()
            
            if choice == "00":
                print(f"\n{Colors.RED}{Colors.BOLD}Goodbye! Use X WIRELESS responsibly!{Colors.RESET}")
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
                print(f"\n{Colors.RED}Invalid option. Please try again.{Colors.RESET}")
            
            input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.RESET}")
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.RED}{Colors.BOLD}Goodbye!{Colors.RESET}")
            break
        except Exception as e:
            print(f"\n{Colors.RED}Error: {e}{Colors.RESET}")
            input(f"{Colors.WHITE}Press Enter to continue...{Colors.RESET}")

if __name__ == "__main__":
    main()
