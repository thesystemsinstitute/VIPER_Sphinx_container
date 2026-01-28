#!/usr/bin/env python3
"""
Validate Manual links in sphinx-packages.rst and remove broken ones.
"""
import re
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse


def check_url(url, timeout=5):
    """Check if a URL is accessible (returns non-404 status)."""
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        # Accept 200-399 status codes
        return response.status_code < 400
    except requests.RequestException:
        try:
            # Try GET if HEAD fails (some servers don't support HEAD)
            response = requests.get(url, timeout=timeout, allow_redirects=True, stream=True)
            return response.status_code < 400
        except requests.RequestException:
            return False


def extract_manual_links(rst_path):
    """Extract all Manual links from the RST file."""
    with open(rst_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match Manual links: `Manual <URL>`_
    pattern = r'`Manual <([^>]+)>`_'
    matches = re.findall(pattern, content)
    
    return matches


def validate_and_fix_links(rst_path, max_workers=10):
    """Validate Manual links and remove broken ones."""
    with open(rst_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Extract all manual links first
    manual_links = {}
    for i, line in enumerate(lines):
        match = re.search(r'`Manual <([^>]+)>`_', line)
        if match:
            url = match.group(1)
            manual_links[i] = url
    
    print(f"Found {len(manual_links)} Manual links to validate")
    
    # Validate URLs in parallel
    broken_urls = set()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in set(manual_links.values())}
        
        completed = 0
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            completed += 1
            try:
                is_valid = future.result()
                if not is_valid:
                    broken_urls.add(url)
                    print(f"  [{completed}/{len(manual_links)}] ✗ Broken: {url}")
                else:
                    print(f"  [{completed}/{len(manual_links)}] ✓ Valid: {url}")
            except Exception as e:
                broken_urls.add(url)
                print(f"  [{completed}/{len(manual_links)}] ✗ Error checking {url}: {e}")
    
    # Replace broken links with N/A
    fixed_count = 0
    for line_num, url in manual_links.items():
        if url in broken_urls:
            # Replace the Manual link with N/A
            indent_match = re.match(r'^(\s+)', lines[line_num])
            indent = indent_match.group(1) if indent_match else '     '
            lines[line_num] = f'{indent}- N/A\n'
            fixed_count += 1
    
    # Write back
    with open(rst_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"\n✓ Removed {fixed_count} broken Manual links")
    print(f"✓ Kept {len(manual_links) - fixed_count} valid Manual links")


def main():
    """Main function."""
    print("=" * 60)
    print("Validating Manual links in documentation")
    print("=" * 60)
    
    rst_path = Path('/sphinx/docs/sphinx-packages.rst')
    
    if not rst_path.exists():
        print(f"✗ RST file not found: {rst_path}")
        return 1
    
    validate_and_fix_links(rst_path)
    
    print("\n" + "=" * 60)
    print("Manual link validation complete")
    print("=" * 60)
    return 0


if __name__ == '__main__':
    exit(main())
