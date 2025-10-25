#!/usr/bin/env python3
"""
X WIRELESS - Attractive Interface (English Only)
===============================================

Terminal interface with exact photo style - English Only
Created by: Adil Fayyaz
Instagram: @Infinityx_20257
"""

import sys
import os
import time
from pathlib import Path

# ANSI color codes for exact photo style
class Colors:
    YELLOW = '\033[93m'
    PINK = '\033[95m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_BLUE = '\033[94m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    CLEAR = '\033[2J'
    HOME = '\033[H'

def clear_screen():
    """Clear screen and position cursor at top."""
    print(Colors.CLEAR + Colors.HOME, end='')

def print_header():
    """Print header with ASCII art identical to photo."""
    clear_screen()
    
    # ASCII Art X WIRELESS (exact photo style)
    ascii_art = f"""
{Colors.YELLOW}    ██╗  ██╗    ██╗    ██╗███████╗██████╗ ██╗     ███████╗███████╗███████╗{Colors.RESET}
{Colors.PINK}    ╚██╗██╔╝    ██║    ██║██╔════╝██╔══██╗██║     ██╔════╝██╔════╝██╔════╝{Colors.RESET}
{Colors.YELLOW}     ╚███╔╝     ██║ █╗ ██║█████╗  ██████╔╝██║     █████╗  ███████╗███████╗{Colors.RESET}
{Colors.PINK}     ██╔██╗     ██║███╗██║██╔══╝  ██╔══██╗██║     ██╔══╝  ╚════██║╚════██║{Colors.RESET}
{Colors.YELLOW}    ██╔╝ ██╗    ╚███╔███╔╝███████╗██║  ██║███████╗███████╗███████║███████║{Colors.RESET}
{Colors.PINK}    ╚═╝  ╚═╝     ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝{Colors.RESET}
"""
    
    print(ascii_art)
    
    # Author information (exact photo style)
    author_info = f"""
{Colors.LIGHT_GREEN}    </>{Colors.WHITE} Author: Adil Fayyaz | Instagram: @Infinityx_20257{Colors.RESET}
"""
    print(author_info)
    
    # Separators (exact photo style)
    separator = f"{Colors.PINK}{'='*60}{Colors.RESET}"
    print(separator)
    
    # Telegram/Social (exact photo style)
    social_info = f"""
{Colors.WHITE}    Telegram @Infinityx_20257 | GitHub: Adil-fayyaz/xwirless{Colors.RESET}
"""
    print(social_info)
    
    print(separator)
    
    # Warning (exact photo style)
    warning = f"""
{Colors.LIGHT_GREEN}    [!] Educational Use Only - Authorized Networks Only{Colors.RESET}
"""
    print(warning)

def print_menu():
    """Print main menu identical to photo."""
    print(f"\n{Colors.PINK}options:{Colors.RESET}")
    
    # Two-column menu (exact photo style)
    menu_items = [
        ("[1]", "Scan Sandbox", "[12]", "System Info"),
        ("[2]", "Scan Dry-Run", "[13]", "Version Info"),
        ("[3]", "Generate Report", "[14]", "Database Stats"),
        ("[4]", "Test Database", "[15]", "Compare Scans"),
        ("[5]", "Show Inventory", "[16]", "Export Data"),
        ("[6]", "Network Analysis", "[17]", "Security Check"),
        ("[7]", "Signal Analysis", "[18]", "Encryption Check"),
        ("[8]", "Channel Scan", "[19]", "Protocol Info"),
        ("[9]", "Quality Report", "[20]", "Help & Examples"),
        ("[10]", "Full Scan", "[21]", "About Tool"),
        ("[11]", "Signal Monitor", "[22]", "Advanced Scan"),
    ]
    
    for left_num, left_item, right_num, right_item in menu_items:
        left = f"{Colors.LIGHT_GREEN}{left_num}{Colors.PINK} {left_item}{Colors.RESET}"
        right = f"{Colors.LIGHT_GREEN}{right_num}{Colors.PINK} {right_item}{Colors.RESET}"
        print(f"    {left:<25} {right}")
    
    # Separator and exit (exact photo style)
    print(f"\n{Colors.LIGHT_BLUE}{'─'*60}{Colors.RESET}")
    print(f"    {Colors.LIGHT_GREEN}[00]{Colors.PINK} EXIT{Colors.RESET}")

def scan_sandbox():
    """Execute sandbox mode scan."""
    print(f"\n{Colors.PINK}SCAN SANDBOX MODE{Colors.RESET}")
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
            
            print(f"{Colors.WHITE}Scan completed: {Colors.LIGHT_GREEN}{scan_result.total_networks}{Colors.WHITE} networks found{Colors.RESET}")
            
            # Show results
            print(f"\n{Colors.PINK}DISCOVERED NETWORKS:{Colors.RESET}")
            for i, network in enumerate(scan_result.networks[:10], 1):
                print(f"    {Colors.LIGHT_GREEN}[{i:2d}]{Colors.WHITE} {network.ssid:<20}{Colors.RESET} {Colors.PINK}{network.bssid}{Colors.RESET} {Colors.WHITE}{network.encryption}{Colors.RESET}")
            
            if len(scan_result.networks) > 10:
                print(f"    {Colors.WHITE}... and {len(scan_result.networks) - 10} more networks{Colors.RESET}")
            
            print(f"\n{Colors.WHITE}Generating report...{Colors.RESET}")
            json_report = reporter.generate_json_report(scan_result)
            
            # Save report
            output_dir = Path(__file__).parent / "output"
            output_dir.mkdir(exist_ok=True)
            (output_dir / "sandbox_report.json").write_text(json_report, encoding='utf-8')
            
            print(f"{Colors.WHITE}Report saved to: {Colors.LIGHT_GREEN}output/sandbox_report.json{Colors.RESET}")
            print(f"{Colors.WHITE}Scan completed successfully!{Colors.RESET}")
            
        else:
            print(f"{Colors.PINK}Sample file not found!{Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.PINK}Error: {e}{Colors.RESET}")

def scan_dry_run():
    """Execute dry-run mode scan."""
    print(f"\n{Colors.PINK}DRY-RUN SCAN MODE{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*50}{Colors.RESET}")
    
    try:
        from xwirless.scanner import WiFiScanner
        
        print(f"{Colors.WHITE}Initializing dry-run scanner...{Colors.RESET}")
        scanner = WiFiScanner(dry_run=True)
        
        print(f"{Colors.WHITE}Simulating network scan...{Colors.RESET}")
        interface = scanner.detect_interface()
        print(f"{Colors.WHITE}Detected interface: {Colors.LIGHT_GREEN}{interface}{Colors.RESET}")
        
        print(f"{Colors.WHITE}Simulating scan output...{Colors.RESET}")
        output = scanner.scan_networks(interface)
        
        print(f"{Colors.WHITE}Dry-run completed successfully!{Colors.RESET}")
        print(f"{Colors.WHITE}No actual commands were executed.{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.PINK}Error: {e}{Colors.RESET}")

def generate_report():
    """Generate complete report."""
    print(f"\n{Colors.PINK}GENERATE COMPLETE REPORT{Colors.RESET}")
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
        
        # Save reports
        output_dir = Path(__file__).parent / "output"
        output_dir.mkdir(exist_ok=True)
        
        (output_dir / "complete_report.json").write_text(json_report, encoding='utf-8')
        (output_dir / "complete_report.md").write_text(md_report, encoding='utf-8')
        (output_dir / "complete_report.csv").write_text(csv_report, encoding='utf-8')
        
        print(f"{Colors.WHITE}Reports saved to:{Colors.RESET}")
        print(f"    {Colors.LIGHT_GREEN}output/complete_report.json{Colors.RESET}")
        print(f"    {Colors.LIGHT_GREEN}output/complete_report.md{Colors.RESET}")
        print(f"    {Colors.LIGHT_GREEN}output/complete_report.csv{Colors.RESET}")
        
        print(f"\n{Colors.WHITE}Report generation completed!{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.PINK}Error: {e}{Colors.RESET}")

def test_database():
    """Test with database."""
    print(f"\n{Colors.PINK}DATABASE TEST{Colors.RESET}")
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
        
        print(f"{Colors.WHITE}Scan saved with ID: {Colors.LIGHT_GREEN}{scan_id}{Colors.RESET}")
        
        # Show statistics
        stats = db.get_statistics()
        print(f"\n{Colors.PINK}DATABASE STATISTICS:{Colors.RESET}")
        print(f"    {Colors.WHITE}Total scans: {Colors.LIGHT_GREEN}{stats['total_scans']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Unique networks: {Colors.LIGHT_GREEN}{stats['unique_networks']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Last scan: {Colors.LIGHT_GREEN}{stats['last_scan_date'] or 'Never'}{Colors.RESET}")
        
        print(f"\n{Colors.WHITE}Database test completed!{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.PINK}Error: {e}{Colors.RESET}")

def show_inventory():
    """Show inventory."""
    print(f"\n{Colors.PINK}INVENTORY DATABASE{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*50}{Colors.RESET}")
    
    try:
        from xwirless.db import InventoryDB
        
        print(f"{Colors.WHITE}Loading database...{Colors.RESET}")
        db = InventoryDB("test_database.json")
        
        stats = db.get_statistics()
        print(f"\n{Colors.PINK}INVENTORY STATISTICS:{Colors.RESET}")
        print(f"    {Colors.WHITE}Total scans: {Colors.LIGHT_GREEN}{stats['total_scans']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Unique networks: {Colors.LIGHT_GREEN}{stats['unique_networks']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Last scan: {Colors.LIGHT_GREEN}{stats['last_scan_date'] or 'Never'}{Colors.RESET}")
        
        # Show recent scans
        scans = db.get_all_scans()
        if scans:
            print(f"\n{Colors.PINK}RECENT SCANS:{Colors.RESET}")
            for scan in scans[-5:]:
                print(f"    {Colors.WHITE}{scan['id']}{Colors.RESET} - {Colors.LIGHT_GREEN}{scan['total_networks']}{Colors.WHITE} networks{Colors.RESET}")
        
        print(f"\n{Colors.WHITE}Inventory loaded successfully!{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.PINK}Error: {e}{Colors.RESET}")

def system_info():
    """Show system information."""
    print(f"\n{Colors.PINK}SYSTEM INFORMATION{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*50}{Colors.RESET}")
    
    try:
        from xwirless.utils import get_system_info
        
        print(f"{Colors.WHITE}Gathering system information...{Colors.RESET}")
        info = get_system_info()
        
        print(f"\n{Colors.PINK}SYSTEM DETAILS:{Colors.RESET}")
        print(f"    {Colors.WHITE}Platform: {Colors.LIGHT_GREEN}{info['platform']}{Colors.RESET}")
        print(f"    {Colors.WHITE}System: {Colors.LIGHT_GREEN}{info['system']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Release: {Colors.LIGHT_GREEN}{info['release']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Machine: {Colors.LIGHT_GREEN}{info['machine']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Python: {Colors.LIGHT_GREEN}{info['python_version']}{Colors.RESET}")
        
        print(f"\n{Colors.PINK}DEPENDENCIES:{Colors.RESET}")
        deps = info['dependencies']
        for dep, available in deps.items():
            status = f"{Colors.LIGHT_GREEN}AVAILABLE{Colors.RESET}" if available else f"{Colors.PINK}NOT AVAILABLE{Colors.RESET}"
            print(f"    {Colors.WHITE}{dep:<15}{Colors.RESET} {status}")
        
        print(f"\n{Colors.WHITE}System information gathered!{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.PINK}Error: {e}{Colors.RESET}")

def version_info():
    """Show version information."""
    print(f"\n{Colors.PINK}VERSION INFORMATION{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*50}{Colors.RESET}")
    
    try:
        from xwirless.utils import get_version_info
        
        print(f"{Colors.WHITE}Loading version information...{Colors.RESET}")
        version_info = get_version_info()
        
        print(f"\n{Colors.PINK}TOOL DETAILS:{Colors.RESET}")
        print(f"    {Colors.WHITE}Version: {Colors.LIGHT_GREEN}{version_info['version']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Author: {Colors.LIGHT_GREEN}{version_info['author']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Email: {Colors.LIGHT_GREEN}{version_info['email']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Python: {Colors.LIGHT_GREEN}{version_info['python_version']}{Colors.RESET}")
        print(f"    {Colors.WHITE}Platform: {Colors.LIGHT_GREEN}{version_info['platform']}{Colors.RESET}")
        
        print(f"\n{Colors.WHITE}Version information loaded!{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.PINK}Error: {e}{Colors.RESET}")

def about_tool():
    """Show tool information."""
    print(f"\n{Colors.PINK}ABOUT X WIRELESS{Colors.RESET}")
    print(f"{Colors.WHITE}{'─'*50}{Colors.RESET}")
    
    about_text = f"""
{Colors.WHITE}X WIRELESS is an advanced Wi-Fi audit and inventory tool designed 
EXCLUSIVELY for educational purposes and testing on owned networks 
with written authorization.

{Colors.PINK}KEY FEATURES:{Colors.RESET}
{Colors.WHITE}• Safe Wi-Fi network scanning
• Multiple output formats (JSON, Markdown, CSV)
• Inventory database with change tracking
• Comprehensive reporting system
• Safety-by-design with legal compliance
• Educational focus with no offensive capabilities

{Colors.PINK}SAFETY FEATURES:{Colors.RESET}
{Colors.WHITE}• Mandatory legal warnings
• Dry-run mode for safe testing
• Sandbox mode with sample data
• Target validation (localhost/internal only)
• No cracking, deauth, or injection capabilities

{Colors.PINK}LEGAL NOTICE:{Colors.RESET}
{Colors.WHITE}This tool is for EDUCATIONAL USE ONLY.
Only use on networks you OWN or have EXPLICIT WRITTEN AUTHORIZATION.
Always comply with applicable laws and regulations.

{Colors.PINK}AUTHOR:{Colors.RESET}
{Colors.WHITE}Adil Fayyaz
Instagram: @Infinityx_20257
GitHub: https://github.com/Adil-fayyaz/xwirless
Email: adilfayyaz388@gmail.com

{Colors.PINK}LICENSE:{Colors.RESET}
{Colors.WHITE}MIT License - Educational Use Only
{Colors.RESET}
"""
    
    print(about_text)

def main():
    """Main function."""
    while True:
        print_header()
        print_menu()
        
        try:
            choice = input(f"\n{Colors.WHITE}Select option: {Colors.RESET}").strip()
            
            if choice == "00":
                print(f"\n{Colors.PINK}Goodbye! Use X WIRELESS responsibly!{Colors.RESET}")
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
            elif choice == "12":
                system_info()
            elif choice == "13":
                version_info()
            elif choice == "21":
                about_tool()
            else:
                print(f"\n{Colors.PINK}Invalid option. Please try again.{Colors.RESET}")
            
            input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.RESET}")
            
        except KeyboardInterrupt:
            print(f"\n\n{Colors.PINK}Goodbye!{Colors.RESET}")
            break
        except Exception as e:
            print(f"\n{Colors.PINK}Error: {e}{Colors.RESET}")
            input(f"{Colors.WHITE}Press Enter to continue...{Colors.RESET}")

if __name__ == "__main__":
    main()
