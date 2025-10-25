"""
Safety validation and legal compliance module.
"""

import click
import sys
from typing import Optional

class SafetyValidator:
    """Handles safety checks and legal confirmations."""
    
    LEGAL_WARNING = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                              ⚠️  LEGAL WARNING ⚠️                            ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  X WIRELESS - Wi-Fi Audit & Inventory Tool                                   ║
║  Created by: Adil Fayyaz                                                    ║
║  Follow on Instagram: @Infinityx_20257                                      ║
║                                                                              ║
║  ⚠️  IMPORTANT LEGAL NOTICE:                                                 ║
║                                                                              ║
║  This tool is designed EXCLUSIVELY for:                                     ║
║  • Educational purposes                                                     ║
║  • Testing on networks you OWN                                              ║
║  • Testing with EXPLICIT WRITTEN AUTHORIZATION                             ║
║                                                                              ║
║  ❌ PROHIBITED USES:                                                        ║
║  • Unauthorized network access                                              ║
║  • Cracking, deauth attacks, or packet injection                            ║
║  • Any illegal network activities                                           ║
║                                                                              ║
║  By using this tool, you agree to:                                          ║
║  • Use it only on authorized networks                                       ║
║  • Comply with all applicable laws                                          ║
║  • Accept full responsibility for your actions                             ║
║                                                                              ║
║  The authors are NOT responsible for misuse of this tool.                   ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

    def __init__(self):
        self.confirmation_phrase = "I CONFIRM I OWN OR AM AUTHORIZED TO TEST THESE NETWORKS"
    
    def show_legal_warning(self) -> bool:
        """Display legal warning and get user confirmation."""
        click.echo(self.LEGAL_WARNING)
        click.echo("\n" + "="*80)
        click.echo("To proceed, you must type the following confirmation phrase:")
        click.echo(f"'{self.confirmation_phrase}'")
        click.echo("="*80)
        
        user_input = click.prompt("\nType the confirmation phrase", type=str)
        
        if user_input.strip() == self.confirmation_phrase:
            click.echo("✅ Legal confirmation received. Proceeding...")
            return True
        else:
            click.echo("❌ Confirmation phrase does not match. Access denied.")
            return False
    
    def validate_target(self, target: str) -> bool:
        """Validate that target is safe (localhost or internal CIDR)."""
        if target in ["localhost", "127.0.0.1", "::1"]:
            return True
        
        # Check for internal CIDR ranges
        internal_ranges = [
            "10.0.0.0/8",
            "172.16.0.0/12", 
            "192.168.0.0/16",
            "169.254.0.0/16"  # Link-local
        ]
        
        # Simple CIDR check (for basic validation)
        if "/" in target:
            network = target.split("/")[0]
            if any(network.startswith(prefix.split(".")[0]) for prefix in internal_ranges):
                return True
        
        return False
    
    def check_dry_run_mode(self, dry_run: bool) -> None:
        """Check if running in dry-run mode."""
        if dry_run:
            click.echo("🔍 Running in DRY-RUN mode - no actual commands will be executed")
    
    def check_sandbox_mode(self, sandbox_file: Optional[str]) -> None:
        """Check if running in sandbox mode."""
        if sandbox_file:
            click.echo(f"📁 Running in SANDBOX mode with file: {sandbox_file}")
