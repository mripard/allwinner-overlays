#! /usr/bin/env python3

import argparse
import struct

def generate_header(vid, pid, vstr, pstr, pver):
    return struct.pack(">"	# Big Endian
                       "4s"	# Magic
                       "B"	# Spec Version
                       "L"	# Vendor ID
                       "H"	# Product ID
                       "B"	# Product Version
                       "32s"	# Vendor String
                       "32s"	# Product String
                       "36x"	# Reserved
                       "16x",	# User Data
                       b'CHIP',
                       1,
                       vid,
                       pid,
                       pver,
                       bytes(vstr, 'utf-8'),
                       bytes(pstr, 'utf-8'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "DIP Header Generator")
    parser.add_argument('out', type = argparse.FileType('wb', 0),
                        help = "Output File")
    parser.add_argument('--version', type = int, default = 1,
                        help = "Version of the DIP spec implemented (default: 1)")
    parser.add_argument('--vid', type = int, required = True,
                        help = "Vendor ID")
    parser.add_argument('--pid', type = int, required = True,
                        help = "Product ID")
    parser.add_argument('--vendor', type = str, required = True,
                        help = "Vendor Description")
    parser.add_argument('--product', type = str, required = True,
                        help = "Product Description")
    parser.add_argument('--product-version', type = int, default = 1,
                        help = "Product Version (default: 1)")

    args = parser.parse_args()

    args.out.write(generate_header(args.vid, args.pid, args.vendor, args.product,
                    args.product_version))
