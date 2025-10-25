"""
Command-line interface for X WIRELESS.
"""

import click
import logging
from typing import Optional
from pathlib import Path

from .scanner import WiFiScanner
from .parser import WiFiParser
from .report import ReportGenerator
from .db import InventoryDB
from .safety import SafetyValidator
from .utils import setup_logging, get_version_info, format_timestamp

logger = logging.getLogger(__name__)

@click.group()
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose logging')
@click.option('--log-file', help='Log to file')
@click.option('--dry-run', is_flag=True, help='Simulate execution without running commands')
@click.option('--sandbox', help='Use sample file for offline testing')
@click.pass_context
def cli_main(ctx, verbose, log_file, dry_run, sandbox):
    """X WIRELESS - Wi-Fi Audit & Inventory Tool
    
    Educational tool for Wi-Fi network auditing and inventory management.
    Created by Adil Fayyaz - Follow on Instagram: @Infinityx_20257
    """
    # Ensure context object exists
    ctx.ensure_object(dict)
    
    # Setup logging
    log_level = "DEBUG" if verbose else "INFO"
    setup_logging(log_level, log_file)
    
    # Store options in context
    ctx.obj['verbose'] = verbose
    ctx.obj['log_file'] = log_file
    ctx.obj['dry_run'] = dry_run
    ctx.obj['sandbox'] = sandbox
    
    # Check safety modes
    safety = SafetyValidator()
    safety.check_dry_run_mode(dry_run)
    safety.check_sandbox_mode(sandbox)

@cli_main.command()
@click.option('--interface', '-i', help='Wireless interface to use')
@click.option('--output', '-o', help='Output file path')
@click.option('--format', 'output_format', 
              type=click.Choice(['json', 'md', 'csv', 'all']), 
              default='md', help='Output format')
@click.option('--upload', is_flag=True, help='Upload report to GitHub Gist')
@click.option('--gist-token', help='GitHub token for Gist upload')
@click.option('--save-db', is_flag=True, help='Save scan to inventory database')
@click.option('--badge', is_flag=True, default=True, help='Include author badge in report')
@click.pass_context
def scan(ctx, interface, output, output_format, upload, gist_token, save_db, badge):
    """Perform Wi-Fi network scan."""
    try:
        # Initialize components
        scanner = WiFiScanner(dry_run=ctx.obj['dry_run'])
        parser = WiFiParser()
        reporter = ReportGenerator(author_badge=badge)
        
        # Detect interface if not provided
        if not interface:
            interface = scanner.detect_interface()
            if not interface:
                click.echo("❌ No wireless interface detected")
                return
        
        click.echo(f"🔍 Scanning networks on interface: {interface}")
        
        # Perform scan
        if ctx.obj['sandbox']:
            scan_output = scanner.scan_from_file(ctx.obj['sandbox'])
        else:
            scan_output = scanner.scan_networks(interface)
        
        # Parse results
        scan_result = parser.parse_scan_output(scan_output, interface)
        
        click.echo(f"✅ Found {scan_result.total_networks} networks")
        
        # Generate reports
        if output_format in ['json', 'all']:
            json_report = reporter.generate_json_report(scan_result)
            if output_format == 'json':
                click.echo(json_report)
            elif output:
                json_file = f"{output}.json" if not output.endswith('.json') else output
                Path(json_file).write_text(json_report, encoding='utf-8')
                click.echo(f"📄 JSON report saved: {json_file}")
        
        if output_format in ['md', 'all']:
            md_report = reporter.generate_markdown_report(scan_result)
            if output_format == 'md':
                click.echo(md_report)
            elif output:
                md_file = f"{output}.md" if not output.endswith('.md') else output
                Path(md_file).write_text(md_report, encoding='utf-8')
                click.echo(f"📄 Markdown report saved: {md_file}")
        
        if output_format in ['csv', 'all']:
            csv_report = reporter.generate_csv_report(scan_result)
            if output_format == 'csv':
                click.echo(csv_report)
            elif output:
                csv_file = f"{output}.csv" if not output.endswith('.csv') else output
                Path(csv_file).write_text(csv_report, encoding='utf-8')
                click.echo(f"📄 CSV report saved: {csv_file}")
        
        # Upload to Gist if requested
        if upload and gist_token:
            filename = f"xwirless_scan_{scan_result.timestamp.strftime('%Y%m%d_%H%M%S')}.md"
            gist_url = reporter.upload_to_gist(md_report, filename, gist_token)
            if gist_url:
                click.echo(f"🌐 Report uploaded: {gist_url}")
        
        # Save to database
        if save_db:
            db = InventoryDB()
            scan_id = db.save_scan(scan_result)
            click.echo(f"💾 Scan saved to database: {scan_id}")
        
    except Exception as e:
        click.echo(f"❌ Scan failed: {e}", err=True)
        logger.error(f"Scan error: {e}", exc_info=True)

@cli_main.command()
@click.argument('scan_id_1')
@click.argument('scan_id_2')
@click.option('--output', '-o', help='Output file for comparison report')
@click.pass_context
def diff(ctx, scan_id_1, scan_id_2, output):
    """Compare two scans and show differences."""
    try:
        db = InventoryDB()
        comparison = db.compare_scans(scan_id_1, scan_id_2)
        
        click.echo(f"📊 Comparing scans: {scan_id_1} vs {scan_id_2}")
        click.echo(f"📅 Scan 1: {comparison['scan1_timestamp']}")
        click.echo(f"📅 Scan 2: {comparison['scan2_timestamp']}")
        click.echo("")
        
        # Summary
        summary = comparison['summary']
        click.echo("📈 Changes Summary:")
        click.echo(f"  • New networks: {summary['total_new']}")
        click.echo(f"  • Disappeared networks: {summary['total_disappeared']}")
        click.echo(f"  • Changed networks: {summary['total_changed']}")
        click.echo("")
        
        # New networks
        if comparison['new_networks']:
            click.echo("🆕 New Networks:")
            for bssid in comparison['new_networks']:
                click.echo(f"  • {bssid}")
            click.echo("")
        
        # Disappeared networks
        if comparison['disappeared_networks']:
            click.echo("❌ Disappeared Networks:")
            for bssid in comparison['disappeared_networks']:
                click.echo(f"  • {bssid}")
            click.echo("")
        
        # Changed networks
        if comparison['changed_networks']:
            click.echo("🔄 Changed Networks:")
            for change in comparison['changed_networks']:
                click.echo(f"  • {change['bssid']}:")
                for change_detail in change['changes']:
                    click.echo(f"    - {change_detail}")
            click.echo("")
        
        # Save comparison report
        if output:
            import json
            Path(output).write_text(json.dumps(comparison, indent=2), encoding='utf-8')
            click.echo(f"📄 Comparison report saved: {output}")
        
    except Exception as e:
        click.echo(f"❌ Comparison failed: {e}", err=True)
        logger.error(f"Comparison error: {e}", exc_info=True)

@cli_main.command()
@click.option('--scan-id', help='Show specific scan details')
@click.option('--network', help='Show specific network history')
@click.pass_context
def inventory(ctx, scan_id, network):
    """Show inventory database information."""
    try:
        db = InventoryDB()
        
        if scan_id:
            scan_data = db.get_scan(scan_id)
            if scan_data:
                click.echo(f"📊 Scan Details: {scan_id}")
                click.echo(f"📅 Timestamp: {scan_data['timestamp']}")
                click.echo(f"🔌 Interface: {scan_data['interface']}")
                click.echo(f"📡 Networks: {scan_data['total_networks']}")
            else:
                click.echo(f"❌ Scan not found: {scan_id}")
        
        elif network:
            network_data = db.get_network_history(network)
            if network_data:
                click.echo(f"📊 Network History: {network}")
                click.echo(f"🕐 First seen: {network_data['first_seen']}")
                click.echo(f"🕐 Last seen: {network_data['last_seen']}")
                click.echo(f"📊 Total scans: {network_data['total_scans']}")
                click.echo(f"📝 SSID history: {', '.join(network_data['ssid_history'])}")
            else:
                click.echo(f"❌ Network not found: {network}")
        
        else:
            stats = db.get_statistics()
            click.echo("📊 Database Statistics:")
            click.echo(f"  • Total scans: {stats['total_scans']}")
            click.echo(f"  • Unique networks: {stats['unique_networks']}")
            click.echo(f"  • Last scan: {stats['last_scan_date'] or 'Never'}")
            
            # Show recent scans
            scans = db.get_all_scans()
            if scans:
                click.echo("\n📅 Recent Scans:")
                for scan in scans[-5:]:  # Last 5 scans
                    click.echo(f"  • {scan['id']}: {scan['timestamp']} ({scan['total_networks']} networks)")
        
    except Exception as e:
        click.echo(f"❌ Inventory query failed: {e}", err=True)
        logger.error(f"Inventory error: {e}", exc_info=True)

@cli_main.command()
def version():
    """Show version information."""
    version_info = get_version_info()
    click.echo(f"X WIRELESS v{version_info['version']}")
    click.echo(f"Author: {version_info['author']}")
    click.echo(f"Python: {version_info['python_version']}")
    click.echo(f"Platform: {version_info['platform']}")

@cli_main.command()
def info():
    """Show system information and dependencies."""
    from .utils import get_system_info
    
    system_info = get_system_info()
    
    click.echo("🖥️  System Information:")
    click.echo(f"  • Platform: {system_info['platform']}")
    click.echo(f"  • System: {system_info['system']}")
    click.echo(f"  • Release: {system_info['release']}")
    click.echo(f"  • Machine: {system_info['machine']}")
    click.echo("")
    
    click.echo("🔧 Dependencies:")
    deps = system_info['dependencies']
    for dep, available in deps.items():
        status = "✅" if available else "❌"
        click.echo(f"  • {dep}: {status}")