#!/usr/bin/env python3
"""
Fix documentation links in sphinx-packages.rst based on what pdoc docs actually exist.
Removes API links for packages without generated pdoc documentation.
"""
import re
from pathlib import Path


def get_generated_packages(pdoc_dir):
    """Get set of package names that have generated pdoc documentation."""
    if not pdoc_dir.exists():
        return set()

    generated = set()
    for item in pdoc_dir.iterdir():
        if item.name == '__pycache__':
            continue
            
        if item.is_dir():
            # Directory exists - check if it has index.html
            index_file = item / 'index.html'
            if index_file.exists() and index_file.stat().st_size > 0:
                generated.add(item.name)
        elif item.is_file() and item.suffix == '.html':
            # Single HTML file (module-level doc) - but not index.html
            if item.stem != 'index' and item.stat().st_size > 0:
                generated.add(item.stem)

    return generated


def fix_api_links(rst_path, generated_packages):
    """Remove API links for packages without pdoc documentation."""
    with open(rst_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Process line by line, looking for API link lines
    removed_count = 0
    kept_count = 0
    removed_packages = []
    
    for i in range(len(lines)):
        line = lines[i]
        # Check if this is an API link line
        match = re.search(r'^\s+- `link <pdoc/([^/]+)/index\.html>`_', line)
        if match:
            pdoc_name = match.group(1)
            # Check if pdoc exists for this package
            if pdoc_name in generated_packages:
                # Keep the link
                kept_count += 1
            else:
                # Remove the API link (replace with empty line)
                lines[i] = '     - \n'
                removed_count += 1
                removed_packages.append(pdoc_name)
    
    # Write back
    with open(rst_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"✓ Kept {kept_count} API links for packages with pdoc documentation")
    print(f"✓ Removed {removed_count} API links for packages without pdoc documentation")
    if removed_packages:
        print(f"  Removed links for: {', '.join(removed_packages[:20])}")
        if len(removed_packages) > 20:
            print(f"  ... and {len(removed_packages) - 20} more")


def main():
    """Main function."""
    print("=" * 60)
    print("Fixing API documentation links")
    print("=" * 60)

    pdoc_dir = Path('/sphinx/docs/pdoc')
    rst_path = Path('/sphinx/docs/sphinx-packages.rst')

    if not pdoc_dir.exists():
        print(f"⚠ pdoc directory not found: {pdoc_dir}")
        print("  No API links will be removed")
        return 0

    if not rst_path.exists():
        print(f"✗ RST file not found: {rst_path}")
        return 1

    # Get list of packages with generated docs
    generated = get_generated_packages(pdoc_dir)
    print(f"✓ Found {len(generated)} packages with pdoc documentation")
    
    if generated:
        sorted_packages = sorted(list(generated))
        print(f"  Packages with pdoc: {', '.join(sorted_packages[:15])}")
        if len(generated) > 15:
            print(f"  ... and {len(generated) - 15} more")

    # Fix the RST file
    fix_api_links(rst_path, generated)

    print("=" * 60)
    print("✓ API link fix complete")
    print("=" * 60)
    return 0


if __name__ == '__main__':
    exit(main())
