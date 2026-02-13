#!/usr/bin/env python3
import argparse
import sys
from .utils import print_logo, print_contact, print_error
from .core import (
    discover_links, find_admin_pages, find_uploader_pages,
    login_bypass, file_upload
)

def main():
    print_logo()
    parser = argparse.ArgumentParser(
        description="bsb-Inquiry - Professional Web Security Testing Toolkit",
        epilog="For more information, visit https://github.com/Shawpon2"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)

    # Command: link
    parser_link = subparsers.add_parser("link", help="Discover all internal links of a website")
    parser_link.add_argument("url", help="Target URL (e.g., http://example.com)")

    # Command: admin
    parser_admin = subparsers.add_parser("admin", help="Find admin/login pages")
    parser_admin.add_argument("url", help="Target base URL")

    # Command: uploader
    parser_uploader = subparsers.add_parser("uploader", help="Find file upload pages")
    parser_uploader.add_argument("url", help="Target base URL")

    # Command: crack
    parser_crack = subparsers.add_parser("crack", help="Attempt login bypass on a login page")
    parser_crack.add_argument("url", help="Full URL of login page (e.g., http://example.com/login.php)")

    # Command: upload
    parser_upload = subparsers.add_parser("upload", help="Upload a file to an upload page")
    parser_upload.add_argument("url", help="Full URL of upload page")

    args = parser.parse_args()

    # Execute appropriate function
    if args.command == "link":
        discover_links(args.url)
    elif args.command == "admin":
        find_admin_pages(args.url)
    elif args.command == "uploader":
        find_uploader_pages(args.url)
    elif args.command == "crack":
        login_bypass(args.url)
    elif args.command == "upload":
        file_upload(args.url)
    else:
        # Should not happen due to required=True
        parser.print_help()
        sys.exit(1)

    print_contact()

if __name__ == "__main__":
    main()
