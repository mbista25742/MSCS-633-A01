#!/usr/bin/env python3
"""
QR Code Generator

This script generates QR codes for given website URLs.
It uses the 'qrcode' library to create, display, and save QR codes as PNG images.

Usage:
    python3 qr_code_generator.py [url]

Arguments:
    url (str, optional): Website URL to encode in the QR code.
                        Defaults to 'http://example.com' if not provided.

Requirements:
    - Python 3.6+
    - qrcode library
    - PIL/Pillow library (dependency of qrcode)

Install requirements:
    pip install qrcode[pil]
"""

import argparse
import os
import sys
from typing import Optional
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image


def validate_url(url: str) -> str:
    """
    Validate and format the URL to ensure it has a proper scheme.
    
    Args:
        url (str): The URL to validate and format.
        
    Returns:
        str: Properly formatted URL with scheme if needed.
    """
    # Check if URL has a scheme (http://, https://, etc.)
    if not url.startswith(('http://', 'https://')):
        # Add default scheme if missing
        url = 'http://' + url
    return url


def generate_qr_code(url: str) -> None:
    """
    Generate a QR code for the given URL, display it, and save it to a file.
    
    Args:
        url (str): The URL to encode in the QR code.
        
    Returns:
        None
    """
    try:
        # Create output filename based on the URL
        # Remove protocol and special characters for the filename
        clean_url = url.replace('http://', '').replace('https://', '').replace('/', '_').replace(':', '_')
        output_filename = f"{clean_url}.png"
        
        # Create QR code instance with error correction
        qr = qrcode.QRCode(
            version=1,
            error_correction=ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        
        # Add data to the QR code
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image to a file
        img.save(output_filename)
        print(f"QR code successfully saved as '{output_filename}'")
        
        # Display the image
        img.show()
        print(f"QR code displayed for URL: {url}")
        
    except Exception as e:
        print(f"Error generating QR code: {e}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """
    Main function to handle command-line arguments and generate QR code.
    """
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description='Generate and display a QR code for a website URL.')
    
    parser.add_argument('url', nargs='?', default='https://www.bioxsystems.com/',
                        help='URL to encode in the QR code (default: https://www.bioxsystems.com/)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Validate and format URL
    url = validate_url(args.url)
    
    # Generate, display and save QR code
    generate_qr_code(url)


if __name__ == "__main__":
    main()