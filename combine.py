#!/usr/bin/python

import sys
import os
import argparse

parser = argparse.ArgumentParser(description="Parse and match values from a NTLM hash dump to cracked passwords from Hashcat")
parser.add_argument("Input_Hash_File", help="The dump file you pulled from the DC in name\\domain:hash format")
parser.add_argument("Cracked_Hash_File", help="The output from hashcat in hash:pass format")
arguments = parser.parse_args()

orighashfile = arguments.Input_Hash_File
crackedhashfile = arguments.Cracked_Hash_File

# Open prepared file from dump file.
with open(orighashfile, 'r') as fp:
    for line in fp:
        # Pull username and hash and split at colon.
        uname, hash1 = line.rstrip('\n').split(':')
        # Open hashcat file for processing.
        with open(crackedhashfile, 'r') as fq:
            for line2 in fq:
                # Pull in hash and password from hashcat file.
                hash2, pass1 = line2.rstrip('\r\n').split(':')
                # Compare hash from hashcat file to hash from original dump file.
                if hash2 == hash1:
                    # Print out matches
                    print("USERNAME: "+uname,"Password: "+pass1)
