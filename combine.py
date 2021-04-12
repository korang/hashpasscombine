import sys
import os


# Filename of prepared hash file from dump. Should be username:ntlm2 hash.
filepath = 'cuthash.txt'

# Filename cracked hashes from hashhcat.
filepath2 = 'hascatfile.txt'

# Open prepared file from dump file.
with open(filepath, 'r') as fp:
    for line in fp:
        # Pull username and hash and split at colon.
        uname, hash1 = line.rstrip('\n').split(':')
        # Open hashcat file for processing.
        with open(filepath2, 'r') as fq:
            for line2 in fq:
                # Pull in hash and password from hashcat file.
                hash2, pass1 = line2.rstrip('\r\n').split(':')
                # Compare hash from hasscat file to hash from original dump file.
                if hash2 == hash1:
                    # Print out matches
                    print("USERNAME: "+uname,"Password: "+pass1)
