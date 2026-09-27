r"""
Adds a footer link to child-safety-standards.html on the homepage --
the page itself was created and deployed correctly, but nothing on
the site links to it yet.

Usage:
    python link_child_safety_footer.py <path-to-website-repo-root>
"""

import sys
from pathlib import Path


def fail(msg):
    print(f"FAILED: {msg}")
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        fail("Usage: python link_child_safety_footer.py <path-to-website-repo-root>")
    root = Path(sys.argv[1])
    if not root.exists():
        fail(f"{root} not found.")

    index_path = root / "index.html"
    if not index_path.exists():
        fail(f"{index_path} not found.")

    text = index_path.read_text(encoding="utf-8")
    if "child-safety-standards.html" in text:
        print("SKIP: already linked.")
        return

    old_footer = (
        '    <a href="/privacy-policy.html">Privacy Policy</a>\n'
        '    <a href="/terms-of-service.html">Terms of Service</a>\n'
        '    <a href="/community-guidelines.html">Community Guidelines</a>\n'
        '    <a href="/delete-account.html">Delete Account</a>'
    )
    if old_footer not in text:
        fail("Could not find the expected footer anchor -- paste the footer section and I'll adjust.")

    new_footer = (
        '    <a href="/privacy-policy.html">Privacy Policy</a>\n'
        '    <a href="/terms-of-service.html">Terms of Service</a>\n'
        '    <a href="/community-guidelines.html">Community Guidelines</a>\n'
        '    <a href="/child-safety-standards.html">Child Safety Standards</a>\n'
        '    <a href="/delete-account.html">Delete Account</a>'
    )
    text = text.replace(old_footer, new_footer, 1)

    index_path.write_text(text, encoding="utf-8", newline="\r\n")
    print(f"Patched: {index_path}")


if __name__ == "__main__":
    main()
