<<<<<<< HEAD
#!/usr/bin/python

import sys
import os
import argparse
=======
import os
import sys
import argparse

# Define Dictionary objects.
orighashdict = {}
crackedhashdict = {}
>>>>>>> upstream/main

parser = argparse.ArgumentParser(description="Parse and match values from a NTLM hash dump to cracked passwords from Hashcat")
parser.add_argument("Input_Hash_File", help="The dump file you pulled from the DC in name\\domain:hash format")
parser.add_argument("Cracked_Hash_File", help="The output from hashcat in hash:pass format")
<<<<<<< HEAD
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
=======

arguments = parser.parse_args()
orighashfile = arguments.Input_Hash_File
crackedhashfile = arguments.Cracked_Hash_File

# Filename of prepared hash file from dump. Should be username:ntlm2 hash.
# Import original hash file into dictionary object.
with open(orighashfile, "r") as origin:
    for line in origin:
        # Set HASH as key and username as value.
        (val, key) = line.rstrip('\n').split(':')
        orighashdict[key] = val

# Import cracked Hash file inot dictionary object.
with open(crackedhashfile, "r") as hashf:
    for line in hashf:
        # Set HASH as key and cracked password as value.
        (key, val) = line.rstrip('\n').split(':')
        crackedhashdict[key] = val

#set keys for dictionary compare.
k1 = set(orighashdict.keys())
k2 = set(crackedhashdict.keys())

# Find keys(hashes) that match in both files.
common_keys = set(k1).intersection(set(k2))

for key in common_keys:
    if orighashdict[key] != crackedhashdict[key]:
        
        # Print user:pass to screen
        print (orighashdict[key] + ":" + crackedhashdict[key])


>>>>>>> upstream/main
