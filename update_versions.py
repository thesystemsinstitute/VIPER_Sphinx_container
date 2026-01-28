#!/usr/bin/env python3
"""
Update package versions in sphinx-packages.rst with actual installed versions.
"""
import re
import subprocess
from pathlib import Path


def get_installed_versions():
    """Get all installed package versions from pip."""
    result = subprocess.run(
        ['pip', 'list', '--format=freeze'],
        capture_output=True,
        text=True,
        check=True
    )
    
    versions = {}
    for line in result.stdout.strip().split('\n'):
        if '==' in line:
            pkg, ver = line.split('==', 1)
            versions[pkg.lower()] = ver
            # Also store with underscores replaced by hyphens
            versions[pkg.lower().replace('_', '-')] = ver
    
    return versions


def update_rst_file(rst_path, versions):
    """Update the RST file with actual package versions."""
    with open(rst_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match version lines in the table
    # Matches lines like "     - Latest" or "     - 1.2.3"
    pattern = r'(\*\s*-\s+([a-zA-Z0-9_-]+)\s*\n\s+)-\s+(?:Latest|[\d.]+(?:\.\d+)?)'
    
    def replace_version(match):
        full_match = match.group(0)
        prefix = match.group(1)
        pkg_name = match.group(2).lower()
        
        # Try to find the version
        version = versions.get(pkg_name)
        if not version:
            # Try with underscores instead of hyphens
            version = versions.get(pkg_name.replace('-', '_'))
        if not version:
            # Try with hyphens instead of underscores
            version = versions.get(pkg_name.replace('_', '-'))
        
        if version:
            return f"{prefix}- {version}"
        else:
            # Keep the original if version not found
            return full_match
    
    updated_content = re.sub(pattern, replace_version, content)
    
    with open(rst_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✓ Updated versions in {rst_path}")


def main():
    """Main function."""
    print("Updating package versions in documentation...")
    
    # Get installed versions
    versions = get_installed_versions()
    print(f"✓ Found {len(versions)} installed packages")
    
    # Update the RST file
    rst_path = Path('/sphinx/docs/sphinx-packages.rst')
    if rst_path.exists():
        update_rst_file(rst_path, versions)
    else:
        print(f"✗ File not found: {rst_path}")
        return 1
    
    print("✓ Version update complete")
    return 0


if __name__ == '__main__':
    exit(main())
